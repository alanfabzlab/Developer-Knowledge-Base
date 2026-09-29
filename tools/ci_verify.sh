#!/usr/bin/env bash
# ci_verify.sh "<título>" <comando...>
#
# Corre un verificador y, si falla, deja el motivo en anotaciones del check.
#
# El log de un job solo se descarga autenticado, así que un workflow que se
# limita a fallar obliga a abrir el navegador para saber qué pasó. Las
# anotaciones que se emiten con `::error::` sí aparecen junto al commit, y en
# la Checks de un pull request: el fallo se lee sin entrar al log.
set -uo pipefail

title=$1
shift

out=$(mktemp)
rc=0
"$@" >"$out" 2>&1 || rc=$?
cat "$out"

if [ $rc -ne 0 ]; then
    # Una línea por discrepancia, que es lo que hay que ir a mirar. Se acotan
    # porque GitHub rechaza anotaciones enormes y porque nadie lee 400 líneas
    # dentro de una X roja.
    detail=$(grep -E '^(---|  )' "$out" \
             | grep -vE 'Traceback|^  File "' | head -25)
    if [ -n "$detail" ]; then
        echo "::error title=$title::$(printf '%s' "$detail" | wc -l | tr -d ' ') lineas; las primeras:" >&2
        while IFS= read -r line; do
            echo "::error title=$title::${line}" >&2
        done <<<"$detail"
    else
        echo "::error title=$title::el verificador fallo sin detail (exit $rc)" >&2
    fi
    # El final del log es el resumen, y es lo que de verdad resume.
    tail -1 "$out" | while IFS= read -r line; do
        [ -n "$line" ] && echo "::error title=$title::$line" >&2
    done
fi

rm -f "$out"
exit $rc
