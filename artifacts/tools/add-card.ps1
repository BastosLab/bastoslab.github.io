<#
.SYNOPSIS  Append a card to assets/projects.js (the Lab page card list).
.EXAMPLE   .\artifacts\tools\add-card.ps1 -Name "foo docs" -Description "The documentation of foo for bar." -Url "https://foo.readthedocs.io/" -Tags docs
Cards render two per row in list order; add a project's docs and replication cards next to each other.
#>
param(
  [Parameter(Mandatory)][string]$Name,
  [Parameter(Mandatory)][string]$Description,
  [Parameter(Mandatory)][string]$Url,
  [string[]]$Tags = @()
)
$ErrorActionPreference = 'Stop'
if ($Url -notmatch '^https://') { throw "Url must start with https:// (got '$Url')" }
$file = Join-Path $PSScriptRoot '..\..\assets\projects.js' | Resolve-Path
$text = [IO.File]::ReadAllText($file)
if ($text.Contains("name: " + (ConvertTo-Json $Name -Compress))) { throw "A card named '$Name' already exists" }
$q = { param($s) ConvertTo-Json ([string]$s) -Compress }   # JSON string literal == valid JS string literal
$tagList = ($Tags | ForEach-Object { & $q $_ }) -join ', '
$entry = "{name: $(& $q $Name), description: $(& $q $Description), url: $(& $q $Url), tags: [$tagList]}"
$rx = [regex]'(\})(\s*)(\r?\n)\];\s*$'
if (-not $rx.IsMatch($text)) { throw "Could not find the end of the PROJECTS list in $file" }
$new = $rx.Replace($text, { param($m) "$($m.Groups[1].Value),$($m.Groups[3].Value)  $entry$($m.Groups[3].Value)];" + $m.Groups[3].Value })
[IO.File]::WriteAllText($file, $new)
Write-Host "Added card '$Name' to $file"
