<#
.SYNOPSIS  Screenshot a page (unscrolled) in headless Edge, without a server.
.EXAMPLE   .\artifacts\tools\preview.ps1 -Page lab/index.html -Theme light -Out $env:TEMP\lab.png
Limits: only the top of the page is captured. Scrolled states (the zoom effect) could not be captured or probed
reliably in headless Edge on the machine this was written on, so check zoom by scrolling in a real browser.
Use -Height 1300 to see a whole short page such as /lab/.
#>
param(
  [string]$Page = 'index.html',
  [ValidateSet('dark', 'light')][string]$Theme = 'dark',
  [string]$Out = (Join-Path $env:TEMP 'bastoslab-preview.png'),
  [int]$Width = 1200, [int]$Height = 800
)
$ErrorActionPreference = 'Stop'
$edge = @('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', 'C:\Program Files\Microsoft\Edge\Application\msedge.exe') | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $edge) { throw 'msedge.exe not found' }
$site = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$tmp = Join-Path $env:TEMP ('bastoslab-preview-' + [guid]::NewGuid().ToString('N'))
try {
  # Work on a copy so the injected theme line never touches the repo.
  robocopy $site $tmp /E /XD .git artifacts /NFL /NDL /NJH /NJS | Out-Null
  $path = Join-Path $tmp $Page
  $html = [IO.File]::ReadAllText($path) -replace '</body>', "<script>document.documentElement.dataset.theme='$Theme'</script></body>"
  [IO.File]::WriteAllText($path, $html, (New-Object Text.UTF8Encoding $false))
  $ErrorActionPreference = 'Continue'   # Edge writes harmless task-manager errors to stderr; PS 5.1 would treat them as fatal
  & $edge --headless --disable-gpu "--window-size=$Width,$Height" --timeout=3000 "--screenshot=$Out" ('file:///' + ($path -replace '\\', '/')) 2>$null | Out-Null
  if (-not (Test-Path $Out)) { throw "No screenshot written to $Out" }
  Write-Host "Screenshot: $Out"
} finally { Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue }
