#!/usr/bin/env bash
# ci_verify.sh "<título>" <comando...>
#
# Corre un verificador y, si falla, deja el motivo en anotaciones del commit.
#
# El log de un job solo se descarga autenticado, así que un workflow que se
# limita a fallar obliga a abrir el navegador para saber qué pasó. Las
# anotaciones que se emiten con `::error::` sí aparecen junto al commit, y en
# la Checks de un pull request: el fallo se lee sin entrar al log.
#
# Se escriben por stdout y no por stderr porque las anotaciones de un job se
# leen de ahí, y se limpian los caracteres que rompen el formato: `%` abre una
# propiedad, `\r` parte la línea y una línea sin fin de línea trunca el
# comando. Un mensaje de error de shell viene con las dos cosas.
set -uo pipefail

title=$1
shift

# Una anotación por línea de detalle, acotada: GitHub rechaza mensajes
# enormes, y nadie lee 400 líneas dentro de una X roja.
annotate() {
    printf '::error title=%s::%s\n' "$title" "$1" |
        tr -d '\r' | cut -c1-240
}

out=$(mktemp)
rc=0
"$@" >"$out" 2>&1 || rc=$?
cat "$out"

if [ $rc -ne 0 ]; then
    # El final del log es el resumen, y es lo que de verdad resume.
    summary=$(tail -1 "$out" | tr -d '\r')
    [ -n "$summary" ] && annotate "$summary"

    # Una línea por discrepancia, que es lo que hay que ir a mirar.
    detail=$(grep -E '^(---|  )' "$out" | grep -vE 'Traceback|^  File "')
    if [ -n "$detail" ]; then
        annotate "$(printf '%s\n' "$detail" | wc -l | tr -d ' ') lineas con el detalle; las primeras:"
        printf '%s\n' "$detail" | head -20 | while IFS= read -r line; do
            annotate "${line}"
        done
    else
        annotate "el verificador fallo sin detalle (exit $rc)"
    fi
fi

rm -f "$out"
exit $rc
