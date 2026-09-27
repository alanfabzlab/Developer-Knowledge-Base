#!/bin/sh
# Publish one HTML file to OpenArtifacts over HTTPS with the license key Copilot
# supplies in the environment. Needs only sh, curl, and awk.
usage() {
  printf '%s\n' "Usage: sh openartifacts-publish.sh publish <html-file> <title> [docId]" >&2
  printf '%s\n' "       sh openartifacts-publish.sh unshare <docId>" >&2
  exit 1
}

KEY=$COPILOT_PLUS_LICENSE_KEY
[ -n "$KEY" ] || {
  printf '%s\n' "Publishing to OpenArtifacts needs a Copilot Plus license key. Add it in Copilot Settings and try again." >&2
  exit 1
}
API_HOST=$OPENARTIFACTS_API_HOST
[ -n "$API_HOST" ] || API_HOST="https://api.openartifacts.ai"
API_HOST=$(printf '%s' "$API_HOST" | sed 's,/*$,,')

COMMAND=$1
DOC_ID=
case "$COMMAND" in
  publish)
    [ "$#" -eq 3 ] || [ "$#" -eq 4 ] || usage
    HTML_FILE=$2
    TITLE=$3
    [ "$#" -eq 4 ] && DOC_ID=$4
    [ -f "$HTML_FILE" ] || {
      printf '%s\n' "HTML file not found: $HTML_FILE" >&2
      exit 1
    }
    ;;
  unshare)
    [ "$#" -eq 2 ] || usage
    DOC_ID=$2
    ;;
  *)
    usage
    ;;
esac
if [ -n "$DOC_ID" ] && ! printf '%s' "$DOC_ID" | grep -Eq '^[0-9abcdefghjkmnpqrstvwxyz]{16}$'; then
  printf '%s\n' "Invalid OpenArtifacts document id: $DOC_ID" >&2
  exit 1
fi

# stdin -> one JSON string literal. Bytes pass through untouched except the escapes
# JSON requires: backslash, quote, tab, CR, LF, and every other control character as
# \u00XX. Only NUL is dropped (awk cannot carry it, and HTML never contains it). A
# sentinel byte keeps a trailing newline in the file from being lost. Backslashes are
# joined in rather than substituted because awk implementations disagree on
# backslashes inside gsub replacements.
json_string() {
  { cat; printf 'x'; } | LC_ALL=C tr -d '\000' | LC_ALL=C awk '
    BEGIN { ORS = ""; bs = sprintf("%c", 92); printf "\"" }
    NR > 1 { printf "%s\\n", prev }
    {
      n = split($0, parts, /\\/)
      line = parts[1]
      for (i = 2; i <= n; i++) line = line bs bs parts[i]
      gsub(/"/, "\\\"", line)
      gsub(/\t/, "\\t", line)
      gsub(/\r/, "\\r", line)
      for (c = 1; c < 32; c++) {
        if (c != 9 && c != 10 && c != 13) gsub(sprintf("%c", c), sprintf("\\u%04x", c), line)
      }
      prev = line
    }
    END { printf "%s\"", substr(prev, 1, length(prev) - 1) }
  '
}

HEADERS=$(mktemp) || exit 1
BODY=$(mktemp) || exit 1
RESPONSE=$(mktemp) || exit 1
trap 'rm -f "$HEADERS" "$BODY" "$RESPONSE"' EXIT
printf 'Authorization: Bearer %s\n' "$KEY" > "$HEADERS"

if [ "$COMMAND" = unshare ]; then
  STATUS=$(curl -sS -o "$RESPONSE" -w '%{http_code}' -X DELETE -H "@$HEADERS" "$API_HOST/api/v1/docs/$DOC_ID")
  CURL_STATUS=$?
else
  {
    printf '{"title":'
    printf '%s' "$TITLE" | json_string
    printf ',"html":'
    json_string < "$HTML_FILE"
    printf '}'
  } > "$BODY"
  if [ -n "$DOC_ID" ]; then
    METHOD=PUT
    URL="$API_HOST/api/v1/docs/$DOC_ID"
  else
    METHOD=POST
    URL="$API_HOST/api/v1/docs"
  fi
  STATUS=$(curl -sS -o "$RESPONSE" -w '%{http_code}' -X "$METHOD" -H "@$HEADERS" -H 'Content-Type: application/json; charset=utf-8' --data-binary "@$BODY" "$URL")
  CURL_STATUS=$?
fi

if [ "$CURL_STATUS" -ne 0 ]; then
  printf '%s\n' "Could not reach OpenArtifacts at $API_HOST." >&2
  exit 1
fi
# The API answers a structured not_found when the page is already gone, which is the
# outcome asked for. Any other 404 is an error.
if [ "$COMMAND" = unshare ] && [ "$STATUS" = 404 ] && grep -q '"not_found"' "$RESPONSE"; then
  STATUS=204
fi
case "$STATUS" in
  2??)
    if [ "$COMMAND" = unshare ]; then
      printf '{"docId":"%s","status":"unshared"}\n' "$DOC_ID"
    else
      cat "$RESPONSE"
      printf '\n'
    fi
    exit 0
    ;;
  *)
    printf '%s\n' "OpenArtifacts returned HTTP $STATUS" >&2
    cat "$RESPONSE" >&2
    printf '\n' >&2
    exit 1
    ;;
esac
