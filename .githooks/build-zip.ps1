# Régénère le zip de chaque skill dont un fichier source fait partie du commit en cours.
#
# Usage manuel (reconstruit tout, sans condition) :
#   powershell -NoProfile -ExecutionPolicy Bypass -File .githooks/build-zip.ps1 -Force
# Invoqué automatiquement par le hook pre-commit, sans argument, quand du contenu
# sous un dossier de skill est déjà détecté dans le commit (voir .githooks/pre-commit).
#
# N'utilise pas Compress-Archive : sur Windows PowerShell 5.1, cette cmdlet stocke les
# chemins avec des antislashs (ex. "references\formules.md"), ce qui viole la norme ZIP
# (séparateur "/" requis) et fait échouer l'import dans Claude.ai. On construit donc
# chaque archive entrée par entrée en forçant le séparateur.

param(
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot

# Un skill = un dossier + le nom du zip à produire (à sa racine) + la liste de
# ses fichiers sources, chemins relatifs au dossier du skill.
$skills = @(
    @{
        Dir  = "analyse-locative"
        Zip  = "analyse-locative.zip"
        Files = @(
            "SKILL.md",
            "references/calculs.md",
            "examples/README.md",
            "examples/en-tetes.tsv",
            "examples/sortie-t2-ancien.tsv",
            "examples/sortie-t3-neuf.tsv",
            "examples/t2-ancien-saint-etienne.md",
            "examples/t3-neuf-angers.md"
        )
    },
    @{
        Dir  = "analyse-financiere-entreprise"
        Zip  = "analyse-financiere-entreprise.zip"
        Files = @(
            "SKILL.md",
            "formulas.md",
            "examples/README.md",
            "examples/Analyse-Financiere-OCTO-Technology.md",
            "examples/Analyse-Financiere-Sopra-Steria.md"
        )
    },
    @{
        Dir  = "generation-cours"
        Zip  = "generation-cours.zip"
        Files = @(
            "SKILL.md",
            "examples/README.md",
            "examples/lean-portfolio-management-au-dela-de-safe.md"
        )
    }
)

if ($Force) {
    $staged = $null  # ignoré : tout reconstruit
} else {
    $staged = git -C $repoRoot diff --cached --name-only --diff-filter=ACMR
}

foreach ($skill in $skills) {
    $skillDir = $skill.Dir
    $zipName = $skill.Zip
    $sourceFiles = $skill.Files

    $needsRebuild = $Force -or ($staged | Where-Object {
        $rel = $_
        $sourceFiles | ForEach-Object { "$skillDir/$_" } | Where-Object { $_ -eq $rel }
    }).Count -gt 0

    if (-not $needsRebuild) { continue }

    $dest = Join-Path $repoRoot "$skillDir/$zipName"
    Write-Host "pre-commit: régénération de $skillDir/$zipName..."

    Add-Type -AssemblyName System.IO.Compression
    Add-Type -AssemblyName System.IO.Compression.FileSystem

    if (Test-Path $dest) {
        Remove-Item $dest -Force
    }

    $fs = [System.IO.File]::Open($dest, [System.IO.FileMode]::Create)
    $archive = New-Object System.IO.Compression.ZipArchive($fs, [System.IO.Compression.ZipArchiveMode]::Create)

    foreach ($entryName in $sourceFiles) {
        $osPath = $entryName.Replace('/', [System.IO.Path]::DirectorySeparatorChar)
        $fullPath = Join-Path $repoRoot "$skillDir/$osPath"
        $entry = $archive.CreateEntry($entryName, [System.IO.Compression.CompressionLevel]::Optimal)
        $stream = $entry.Open()
        $bytes = [System.IO.File]::ReadAllBytes($fullPath)
        $stream.Write($bytes, 0, $bytes.Length)
        $stream.Close()
    }

    $archive.Dispose()
    $fs.Close()

    $size = (Get-Item $dest).Length
    Write-Host "  -> $skillDir/$zipName ($size octets)"

    if (-not $Force) {
        git -C $repoRoot add "$skillDir/$zipName" | Out-Null
    }
}
