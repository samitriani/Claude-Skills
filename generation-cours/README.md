# Cours Approfondi

Skill Claude pour produire un cours écrit complet et sourcé (8-10k mots, 8 modules) sur n'importe quel sujet — pas un résumé Wikipédia allongé, un support structuré comme un vrai syllabus, avec les controverses incluses et rien comblé par du contenu plausible.

---

## Ce que fait le skill

Sur une commande comme `Fais-moi un cours sur [sujet]`, il déroule un pipeline en 5 phases :

1. **Cadrage** — infère l'angle depuis le contexte, ne pose qu'une question si un choix structurant reste ambigu (ex. angle technique vs stratégique).
2. **Recherche en 4 couches** (15 à 25 recherches) — canon académique, état de l'art récent, retours d'expérience opérationnels, controverses. Chaque couche apporte quelque chose que les autres n'ont pas.
3. **Plan, validé avant écriture** — **point d'arrêt obligatoire** : le plan est présenté en chat et attend une validation avant que le moindre module ne soit rédigé.
4. **Rédaction module par module** — pas de trame fixe imposée (la forme se décide selon le sujet), mais quatre exigences de fond systématiques : objectif clair, exemple concret nommé, erreurs fréquentes quand la recherche en a fait remonter, controverses traitées dans le module concerné plutôt que reléguées en fin de cours. Des schémas Mermaid s'insèrent quand un concept est intrinsèquement visuel. Écrit en plusieurs passes pour éviter la dégradation de qualité sur un texte long produit d'une traite.
5. **Ancrage et livraison** — glossaire, questions de compréhension, bibliographie hiérarchisée, puis remise du fichier.

## Installation

L'installation diffère selon l'application utilisée.

### Claude.ai (app de bureau, web, mobile)

1. Télécharge [`generation-cours.zip`](generation-cours.zip) depuis ce dépôt (clique sur le fichier, puis *Download raw file*).
2. Dans l'app : **Réglages → Capacités (Capabilities) → Skills**. Sur un compte Team/Enterprise, un administrateur doit parfois activer Skills au niveau de l'organisation avant que l'option n'apparaisse.
3. **Créer/Importer un skill** → sélectionne `generation-cours.zip`.
4. Active le skill (bascule on) — globalement ou pour la conversation en cours.

Skills est réservé aux plans payants (Pro, Max, Team, Enterprise) ; l'intitulé exact des menus peut varier selon les déploiements.

Le zip contient uniquement `SKILL.md` et `examples/` — pas `README.md` ni `LICENSE`, qui ne servent qu'à la publication GitHub. **Si tu modifies `SKILL.md` ou les fichiers `examples/`, régénère le zip avant de le réimporter** — voir [Régénérer le zip](#régénérer-le-zip) plus bas.

### Claude Code (CLI, IDE, app de bureau)

Copier le dossier dans le répertoire des skills de Claude :

```bash
git clone https://github.com/<votre-compte>/generation-cours.git ~/.claude/skills/generation-cours
```

Le nom du dossier doit correspondre au champ `name` du frontmatter de `SKILL.md` (minuscules, chiffres et tirets uniquement) — c'est déjà le cas ici. Le nom du dépôt GitHub, lui, est libre.

Le skill se déclenche ensuite sur des formulations comme « fais-moi un cours sur X », « j'ai besoin de monter en compétences sur X », « explique-moi X en profondeur », « forme-moi sur X » — même sans le mot « cours ». Il ne se déclenche pas sur une simple question factuelle ou une explication courte.

## Utilisation

```
Fais-moi un cours sur les transformers
J'ai besoin de monter en compétences sur le RGPD
Explique-moi la cryptographie post-quantique en profondeur
Je dois maîtriser Kubernetes pour mon prochain poste
```

Aucun paramètre à fournir au-delà du sujet — le skill infère l'angle et ne pose une question que si un choix structurant reste ambigu (typiquement : angle technique, stratégique ou opérationnel).

## Ce qui distingue ce skill d'un résumé généré

- **La structure vient de syllabi existants**, pas d'une improvisation : recherche explicite de plans de cours, tables des matières de manuels de référence, syllabus MIT/Stanford, avant de construire le plan.
- **Les controverses sont une couche de recherche à part entière** (3-4 recherches dédiées) — un cours qui présente un domaine comme consensuel alors qu'il ne l'est pas est considéré comme un cours faux par ce skill, pas comme un cours incomplet.
- **Aucun chiffre sans source**, format inline (`62 % des projets échouent [McKinsey, 2025]`).
- **Statut épistémique marqué** : `[débattu]` quand les experts ne sont pas d'accord, `[émergent]` quand c'est trop récent pour être validé — plutôt que de présenter tout le contenu au même niveau de certitude.
- **Aucune zone comblée par du contenu plausible.** Une zone mal documentée est signalée comme telle, avec ce qui manque, plutôt qu'étirée pour atteindre le volume cible.
- **Le plan est validé avant la rédaction.** Écrire 9000 mots dans la mauvaise direction est traité comme le pire échec possible du skill — pas un point de détail.
- **Pas de gabarit rigide par module.** La forme (analogie ou non, formalisme ou non) suit ce que le sujet exige plutôt qu'un schéma imposé identique pour les 8 modules — mais quatre exigences de fond restent systématiques (voir ci-dessus).
- **Schémas seulement quand ils apportent quelque chose.** Un bloc Mermaid intégré au texte quand un concept est intrinsèquement visuel (flux, hiérarchie, chronologie, comparaison) — jamais systématique, jamais en annexe.

## Mécanique d'exécution et portabilité

Ce skill écrit un fichier `.md` et le remet à l'utilisateur. L'emplacement exact et le mécanisme de remise dépendent de l'environnement d'exécution (dossier de sortie conventionnel sur certains déploiements Claude, répertoire de travail courant ailleurs) — `SKILL.md` documente ce choix comme une adaptation à l'environnement plutôt que de figer un chemin spécifique à une seule plateforme.

## Limites

- **8-10k mots reste un volume par défaut, pas une contrainte de qualité.** Le skill privilégie explicitement 6 modules denses plutôt que 8 dont 2 sont creux.
- **La qualité dépend directement du volume de recherche.** Le skill vise 15 à 25 recherches ; en dessous, le résultat se rapproche d'une paraphrase de mémoire — un des anti-patterns que `SKILL.md` liste explicitement.
- **Un sujet mal couvert publiquement produit un cours qui le dit.** Si les recherches ne remontent que des sources de faible fiabilité (Tier C dans la hiérarchie des sources), c'est traité comme une information sur la maturité du domaine, pas masqué.
- **Pas un cours interactif ni un support pédagogique évalué** : c'est un document de référence à lire, avec des questions de compréhension en fin de parcours, pas un outil de suivi d'apprentissage.

## Structure du dépôt

```
generation-cours/
├── SKILL.md                                          # le skill lui-même
├── README.md
├── LICENSE
├── generation-cours.zip                              # package pour l'upload Claude.ai
├── .githooks/
│   ├── pre-commit                                    # régénère et ajoute le zip quand une source change
│   └── build-zip.ps1                                 # construction du zip sous Windows
└── examples/
    ├── README.md
    └── lean-portfolio-management-au-dela-de-safe.md  # cours complet en 8 modules
```

## Régénérer le zip

Un hook `pre-commit` régénère `generation-cours.zip` automatiquement dès que `SKILL.md` ou un fichier de `examples/` fait partie du commit.

**Activation (une fois par clone)** — git ne suit pas `.git/hooks/`, il faut donc pointer explicitement vers le dossier versionné du dépôt :

```bash
git config core.hooksPath .githooks
```

Le hook ([`.githooks/pre-commit`](.githooks/pre-commit)) utilise `zip` sur macOS/Linux, et [`.githooks/build-zip.ps1`](.githooks/build-zip.ps1) via PowerShell sur Windows (faute de `zip`). **Ne pas utiliser `Compress-Archive`** : sous Windows PowerShell 5.1, elle stocke les chemins avec des antislashs, ce qui viole la norme ZIP et fait échouer l'import dans Claude.ai.

**Régénération manuelle** (si le hook n'est pas actif) :

```bash
# macOS / Linux
cd generation-cours
zip -r generation-cours.zip SKILL.md examples/
```

```powershell
# Windows
powershell -NoProfile -ExecutionPolicy Bypass -File .githooks\build-zip.ps1
```

## Contribuer

Les contributions utiles en priorité :

- des exemples sur d'autres profils de sujet (un sujet réglementaire pur, un sujet où les sources sont majoritairement Tier C, un sujet avec un fort désaccord d'experts) ;
- des retours sur la robustesse du point d'arrêt Phase 3 dans des environnements où l'interaction en plusieurs tours est contrainte.

## Licence

MIT — voir [LICENSE](LICENSE).
