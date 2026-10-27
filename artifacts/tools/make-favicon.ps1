<#
.SYNOPSIS  Rebuild assets/favicon.png: the symbol-only half of assets/logo.png on a dark purple rounded square.
The logo is a transparent PNG with white lettering. The symbol sits left of a transparent column gap and the text
right of it, so the crop is "everything left of the first empty column run after x=17". Re-run after replacing logo.png.
#>
param([string]$BadgeColor = '#24103f', [int]$Size = 256)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$assets = (Resolve-Path (Join-Path $PSScriptRoot '..\..\assets')).Path
$src = [Drawing.Bitmap]::FromFile("$assets\logo.png")
try {
  # Column occupancy -> end of the symbol = start of the first run of >=8 empty columns after content begins.
  $occ = for ($x = 0; $x -lt $src.Width; $x++) { $n = 0; for ($y = 0; $y -lt $src.Height; $y++) { if ($src.GetPixel($x, $y).A -gt 40) { $n++ } }; $n }
  $x0 = ($occ | ForEach-Object { $_ }).IndexOf(($occ | Where-Object { $_ -gt 0 } | Select-Object -First 1))
  $x1 = $null; $run = 0
  for ($x = $x0; $x -lt $occ.Count; $x++) {
    if ($occ[$x] -eq 0) { $run++; if ($run -ge 8) { $x1 = $x - $run; break } } else { $run = 0 }
  }
  if ($null -eq $x1) { throw 'No gap between symbol and text found; crop manually.' }
  $w = $x1 - $x0 + 1
  $minY = $src.Height; $maxY = 0
  for ($x = $x0; $x -le $x1; $x++) { for ($y = 0; $y -lt $src.Height; $y++) { if ($src.GetPixel($x, $y).A -gt 40) { if ($y -lt $minY) { $minY = $y }; if ($y -gt $maxY) { $maxY = $y } } } }
  $h = $maxY - $minY + 1
  $side = [Math]::Max($w, $h); $k = $Size / ($side * 1.16)
  $o = New-Object Drawing.Bitmap $Size, $Size
  $g = [Drawing.Graphics]::FromImage($o); $g.SmoothingMode = 'AntiAlias'; $g.InterpolationMode = 'HighQualityBicubic'; $g.Clear([Drawing.Color]::Transparent)
  $r = [int]($Size * 0.1875); $p = New-Object Drawing.Drawing2D.GraphicsPath
  $p.AddArc(0, 0, $r, $r, 180, 90); $p.AddArc($Size - $r, 0, $r, $r, 270, 90); $p.AddArc($Size - $r, $Size - $r, $r, $r, 0, 90); $p.AddArc(0, $Size - $r, $r, $r, 90, 90); $p.CloseFigure()
  $g.FillPath((New-Object Drawing.SolidBrush ([Drawing.ColorTranslator]::FromHtml($BadgeColor))), $p)
  $dw = $w * $k; $dh = $h * $k
  $g.DrawImage($src, [Drawing.RectangleF]::new(($Size - $dw) / 2, ($Size - $dh) / 2, $dw, $dh), [Drawing.RectangleF]::new($x0, $minY, $w, $h), 'Pixel')
  $o.Save("$assets\favicon.png", [Drawing.Imaging.ImageFormat]::Png); $g.Dispose(); $o.Dispose()
  Write-Host "Wrote $assets\favicon.png (symbol x=$x0..$x1, y=$minY..$maxY)"
} finally { $src.Dispose() }
