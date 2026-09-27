[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
# Publish one HTML file to OpenArtifacts over HTTPS with the license key Copilot
# supplies in the environment.

function Show-Usage {
  [Console]::Error.WriteLine('Usage: openartifacts-publish.ps1 publish <html-file> <title> [docId]')
  [Console]::Error.WriteLine('       openartifacts-publish.ps1 unshare <docId>')
  exit 1
}

$KEY = [Environment]::GetEnvironmentVariable('COPILOT_PLUS_LICENSE_KEY')
if (-not $KEY) {
  [Console]::Error.WriteLine('Publishing to OpenArtifacts needs a Copilot Plus license key. Add it in Copilot Settings and try again.')
  exit 1
}
$API_HOST = [Environment]::GetEnvironmentVariable('OPENARTIFACTS_API_HOST')
if (-not $API_HOST) { $API_HOST = 'https://api.openartifacts.ai' }
$API_HOST = $API_HOST.TrimEnd('/')

$COMMAND = if ($args.Count -ge 1) { [string]$args[0] } else { '' }
$DOC_ID = ''
switch ($COMMAND) {
  'publish' {
    if ($args.Count -ne 3 -and $args.Count -ne 4) { Show-Usage }
    $HTML_FILE = [string]$args[1]
    $TITLE = [string]$args[2]
    if ($args.Count -eq 4) { $DOC_ID = [string]$args[3] }
    if (-not (Test-Path -LiteralPath $HTML_FILE -PathType Leaf)) {
      [Console]::Error.WriteLine("HTML file not found: $HTML_FILE")
      exit 1
    }
  }
  'unshare' {
    if ($args.Count -ne 2) { Show-Usage }
    $DOC_ID = [string]$args[1]
  }
  default { Show-Usage }
}
if ($DOC_ID -and $DOC_ID -notmatch '^[0-9abcdefghjkmnpqrstvwxyz]{16}$') {
  [Console]::Error.WriteLine("Invalid OpenArtifacts document id: $DOC_ID")
  exit 1
}

$headers = @{ Authorization = "Bearer $KEY" }
try {
  if ($COMMAND -eq 'unshare') {
    $null = Invoke-WebRequest -UseBasicParsing -Method Delete -Uri "$API_HOST/api/v1/docs/$DOC_ID" -Headers $headers
    [Console]::Out.WriteLine('{"docId":"' + $DOC_ID + '","status":"unshared"}')
  } else {
    $html = [System.IO.File]::ReadAllText($HTML_FILE, (New-Object System.Text.UTF8Encoding($false)))
    $body = @{ title = $TITLE; html = $html } | ConvertTo-Json -Compress -Depth 2
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($body)
    $method = if ($DOC_ID) { 'Put' } else { 'Post' }
    $uri = if ($DOC_ID) { "$API_HOST/api/v1/docs/$DOC_ID" } else { "$API_HOST/api/v1/docs" }
    $response = Invoke-WebRequest -UseBasicParsing -Method $method -Uri $uri -Headers $headers -ContentType 'application/json; charset=utf-8' -Body $bytes
    [Console]::Out.WriteLine([string]$response.Content)
  }
} catch {
  $status = $null
  $detail = ''
  if ($_.Exception.Response) {
    try { $status = [int]$_.Exception.Response.StatusCode } catch { $status = $null }
    try {
      $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
      $detail = $reader.ReadToEnd()
    } catch { $detail = '' }
  }
  if (-not $detail -and $_.ErrorDetails) { $detail = [string]$_.ErrorDetails.Message }
  if ($COMMAND -eq 'unshare' -and $status -eq 404 -and $detail -match '"not_found"') {
    # The API's structured not_found means the page is already gone, which is the outcome asked for.
    [Console]::Out.WriteLine('{"docId":"' + $DOC_ID + '","status":"unshared"}')
    exit 0
  }
  if ($status) {
    [Console]::Error.WriteLine("OpenArtifacts returned HTTP $status")
    if ($detail) { [Console]::Error.WriteLine($detail) }
  } elseif ($detail) {
    [Console]::Error.WriteLine($detail)
  } else {
    [Console]::Error.WriteLine("Could not reach OpenArtifacts at $API_HOST. " + $_.Exception.Message)
  }
  exit 1
}
exit 0
