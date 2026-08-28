#!/bin/sh
# Régénère le zip de chaque skill dont un fichier source fait partie du commit en cours.
# Équivalent macOS/Linux de build-zip.ps1 — utilise la commande native `zip`, qui ne
# souffre pas du bug d'antislashs de Compress-Archive sous Windows.
#
# Usage manuel (reconstruit tout, sans condition) :
#   .githooks/build-zip.sh --force
# Invoqué automatiquement par le hook pre-commit (voir .githooks/pre-commit).

set -e

repo_root=$(git rev-parse --show-toplevel)
cd "$repo_root"

force=0
[ "$1" = "--force" ] && force=1

if [ "$force" -eq 0 ]; then
    staged=$(git diff --cached --name-only --diff-filter=ACMR)
fi

# Un skill par appel : dossier, nom du zip, puis fichiers sources (chemins relatifs au dossier).
build_skill() {
    skill_dir="$1"
    zip_name="$2"
    shift 2

    needs=0
    if [ "$force" -eq 1 ]; then
        needs=1
    else
        for rel in "$@"; do
            if printf '%s\n' "$staged" | grep -qx "$skill_dir/$rel"; then
                needs=1
                break
            fi
        done
    fi
    [ "$needs" -eq 0 ] && return 0

    echo "pre-commit: régénération de $skill_dir/$zip_name..."
    ( cd "$skill_dir" && rm -f "$zip_name" && zip -q -X "$zip_name" "$@" )

    if [ "$force" -eq 0 ]; then
        git add "$skill_dir/$zip_name"
    fi
}

build_skill "analyse-locative" "analyse-locative.zip" \
    "SKILL.md" "references/calculs.md" "examples/README.md" \
    "examples/en-tetes.tsv" "examples/sortie-t2-ancien.tsv" "examples/sortie-t3-neuf.tsv" \
    "examples/t2-ancien-saint-etienne.md" "examples/t3-neuf-angers.md"

build_skill "analyse-financiere-entreprise" "analyse-financiere-entreprise.zip" \
    "SKILL.md" "formulas.md" "examples/README.md" \
    "examples/Analyse-Financiere-OCTO-Technology.md" "examples/Analyse-Financiere-Sopra-Steria.md"

build_skill "generation-cours" "generation-cours.zip" \
    "SKILL.md" "examples/README.md" "examples/lean-portfolio-management-au-dela-de-safe.md"
