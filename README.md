# Claude Skills

Monorepo regroupant plusieurs [Claude Skills](https://www.anthropic.com/news/skills) — des capacités packagées que Claude peut charger à la demande pour dérouler un pipeline de travail précis plutôt que d'improviser à chaque fois.

---

## Skills disponibles

| Skill | Ce qu'il fait |
|---|---|
| [`analyse-locative/`](analyse-locative) | Analyse d'investissement locatif en France (rentabilité, cash-flow, fiscalité, contexte de marché INSEE) à partir d'une annonce ou d'un descriptif de bien. |
| [`analyse-financiere-entreprise/`](analyse-financiere-entreprise) | Diagnostic financier en 8 étapes d'une entreprise cotée ou non cotée (marges, ROIC, WACC, EVA, valorisation) jusqu'à une recommandation BUY / HOLD / SELL argumentée. |
| [`generation-cours/`](generation-cours) | Génération d'un cours écrit complet et sourcé (8-10k mots, 8 modules) sur n'importe quel sujet, avec recherche en 4 couches et point d'arrêt de validation du plan avant rédaction. |

Chaque skill est autonome : son propre `SKILL.md`, son `README.md`, sa `LICENSE`, ses `examples/` et son zip packagé pour Claude.ai. Voir le README de chaque sous-dossier pour le détail de son fonctionnement, ses limites et son installation.

## Installation

L'installation diffère selon l'application utilisée — le détail exact (formulations qui déclenchent le skill, structure du zip) est documenté dans le README de chaque skill. Le principe général :

### Claude.ai (app de bureau, web, mobile)

Chaque skill se télécharge indépendamment via son zip (`<skill>/<skill>.zip`), puis s'importe dans **Réglages → Capacités (Capabilities) → Skills**. Réservé aux plans payants (Pro, Max, Team, Enterprise).

### Claude Code (CLI, IDE, app de bureau)

Cloner ce dépôt une fois, puis copier le(s) skill(s) voulu(s) vers le répertoire des skills de Claude :

```bash
git clone https://github.com/samitriani/Claude-Skills.git
cp -r Claude-Skills/analyse-locative ~/.claude/skills/analyse-locative
cp -r Claude-Skills/analyse-financiere-entreprise ~/.claude/skills/analyse-financiere-entreprise
cp -r Claude-Skills/generation-cours ~/.claude/skills/generation-cours
```

Le nom de chaque dossier copié doit correspondre au champ `name` du frontmatter de son `SKILL.md` — c'est déjà le cas ici. Copier uniquement les skills qui t'intéressent, pas besoin des trois.

## Régénérer les zips

Chaque skill embarque son propre zip (`<skill>/<skill>.zip`), le format attendu par l'import Claude.ai. Un hook `pre-commit`, partagé entre les trois skills, régénère automatiquement le zip d'un skill dès qu'un de ses fichiers sources fait partie du commit en cours.

**Activation (une fois par clone)** — git ne suit pas `.git/hooks/`, il faut donc pointer explicitement vers le dossier versionné du dépôt :

```bash
git config core.hooksPath .githooks
```

Le hook ([`.githooks/pre-commit`](.githooks/pre-commit)) détecte les fichiers modifiés sous chaque dossier de skill, puis délègue à :
- [`.githooks/build-zip.sh`](.githooks/build-zip.sh) sur macOS/Linux, via la commande native `zip` ;
- [`.githooks/build-zip.ps1`](.githooks/build-zip.ps1) sur Windows, via PowerShell.

**Ne pas utiliser `Compress-Archive`** : sous Windows PowerShell 5.1, cette cmdlet stocke les chemins avec des antislashs (`references\formules.md`), ce qui viole la norme ZIP (séparateur `/` requis) et fait échouer l'import dans Claude.ai (« Zip file contains path with invalid characters »). `build-zip.ps1` construit donc chaque archive entrée par entrée en forçant le séparateur.

La liste exacte des fichiers sources embarqués dans chaque zip est définie dans `build-zip.ps1`/`build-zip.sh` — voir le README du skill concerné pour la commande de régénération manuelle (utile si le hook n'est pas actif, ou pour ne reconstruire qu'un seul skill) :

```bash
# reconstruit tout, sans condition de commit
powershell -NoProfile -ExecutionPolicy Bypass -File .githooks/build-zip.ps1 -Force   # Windows
.githooks/build-zip.sh --force                                                        # macOS/Linux
```

## Structure du dépôt

```
Claude Skills/
├── README.md                            # ce fichier
├── LICENSE
├── .githooks/                           # hook pre-commit partagé, régénère les zips des 3 skills
│   ├── pre-commit
│   ├── build-zip.ps1                    # Windows
│   └── build-zip.sh                     # macOS/Linux
├── analyse-locative/
├── analyse-financiere-entreprise/
└── generation-cours/
```

## Licence

MIT — voir [LICENSE](LICENSE). Chaque skill embarque également sa propre copie de la licence.
