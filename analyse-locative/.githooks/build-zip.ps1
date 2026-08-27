# Régénère analyse-locative.zip à partir des sources du skill.
#
# Usage manuel : powershell -NoProfile -ExecutionPolicy Bypass -File .githooks/build-zip.ps1
# Invoqué automatiquement par le hook pre-commit quand une source change.
#
# N'utilise pas Compress-Archive : sur Windows PowerShell 5.1, cette cmdlet stocke les
# chemins avec des antislashs (ex. "references\calculs.md"), ce qui viole la norme ZIP
# (séparateur "/" requis) et fait échouer l'import dans Claude.ai. On construit donc
# l'archive entrée par entrée en forçant le séparateur.

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$dest = Join-Path $repoRoot "analyse-locative.zip"

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$filesToZip = @(
    "SKILL.md",
    "references/calculs.md",
    "examples/README.md",
    "examples/en-tetes.tsv",
    "examples/sortie-t2-ancien.tsv",
    "examples/sortie-t3-neuf.tsv",
    "examples/t2-ancien-saint-etienne.md",
    "examples/t3-neuf-angers.md"
)

if (Test-Path $dest) {
    Remove-Item $dest -Force
}

$fs = [System.IO.File]::Open($dest, [System.IO.FileMode]::Create)
$archive = New-Object System.IO.Compression.ZipArchive($fs, [System.IO.Compression.ZipArchiveMode]::Create)

foreach ($entryName in $filesToZip) {
    $osPath = $entryName.Replace('/', [System.IO.Path]::DirectorySeparatorChar)
    $fullPath = Join-Path $repoRoot $osPath
    $entry = $archive.CreateEntry($entryName, [System.IO.Compression.CompressionLevel]::Optimal)
    $stream = $entry.Open()
    $bytes = [System.IO.File]::ReadAllBytes($fullPath)
    $stream.Write($bytes, 0, $bytes.Length)
    $stream.Close()
}

$archive.Dispose()
$fs.Close()

$size = (Get-Item $dest).Length
Write-Host "analyse-locative.zip régénéré ($size octets)."
