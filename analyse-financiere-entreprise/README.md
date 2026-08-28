# Diagnostic Financier en 8 Étapes

Skill Claude pour analyser la santé financière d'une entreprise cotée ou non cotée à partir de ses données publiques — marges, structure de bilan, rentabilité (ROIC), financement, cash-flows, coût du capital (WACC), création de valeur (EVA) et valorisation (patrimoniale, multiples, DCF) — jusqu'à une recommandation BUY / HOLD / SELL argumentée.

---

## Ce que fait le skill

Sur une commande comme `Analyse [entreprise]`, il :

1. **collecte les données publiques** de l'entreprise (rapport annuel, Boursorama, Zonebourse, Morningstar, presse financière — et pappers.fr/societe.com pour les PME françaises non cotées), sur 2 à 3 ans minimum ;
2. **applique 8 étapes séquentielles**, chacune produisant des indicateurs chiffrés et une interprétation, pas juste des chiffres bruts :
   1. Analyse de la marge
   2. Actif économique (BFR, immobilisations)
   3. Rentabilité de l'actif économique (ROIC, décomposition DuPont)
   4. Financement (gearing, levier, couverture des intérêts)
   5. Cash et sa circulation (Free Cash-Flow, FCF yield)
   6. Coût des capitaux employés (WACC, MEDAF)
   7. Création de valeur (EVA, spread ROIC-WACC)
   8. Valeur d'entreprise (patrimoniale, multiples, DCF)
3. **produit un artefact markdown structuré**, avec un Executive Summary en tête ;
4. **conclut par une recommandation BUY / HOLD / SELL** avec prix cible et scénarios Bull / Base / Bear.

## Installation

L'installation diffère selon l'application utilisée.

### Claude.ai (app de bureau, web, mobile)

1. Télécharge [`analyse-financiere-entreprise.zip`](analyse-financiere-entreprise.zip) depuis ce dépôt (clique sur le fichier, puis *Download raw file*).
2. Dans l'app : **Réglages → Capacités (Capabilities) → Skills**. Sur un compte Team/Enterprise, un administrateur doit parfois activer Skills au niveau de l'organisation avant que l'option n'apparaisse.
3. **Créer/Importer un skill** → sélectionne `analyse-financiere-entreprise.zip`.
4. Active le skill (bascule on) — globalement ou pour la conversation en cours.

Skills est réservé aux plans payants (Pro, Max, Team, Enterprise) ; l'intitulé exact des menus peut varier selon les déploiements.

Le zip contient uniquement `SKILL.md`, `formulas.md` et `examples/` — pas `README.md` ni `LICENSE`, qui ne servent qu'à la publication GitHub. **Si tu modifies `SKILL.md`, `formulas.md` ou `examples/`, régénère le zip avant de le réimporter** — voir [Régénérer le zip](#régénérer-le-zip) plus bas.

### Claude Code (CLI, IDE, app de bureau)

Ce skill fait partie du monorepo **Claude Skills**, qui regroupe plusieurs skills dans un seul dépôt GitHub. Cloner le dépôt, puis copier uniquement ce sous-dossier vers l'emplacement attendu par Claude Code (le nom du dossier de destination doit correspondre au champ `name` du frontmatter de `SKILL.md`) :

```bash
git clone https://github.com/samitriani/Claude-Skills.git
cp -r Claude-Skills/analyse-financiere-entreprise ~/.claude/skills/analyse-financiere-entreprise
```

Le skill se déclenche ensuite sur toute formulation commençant par « Analyse [entreprise] », ou sur des expressions comme « diagnostic financier », « valorisation », « ROIC », « WACC », « EVA », « création de valeur ».

## Utilisation

```
Analyse Sopra Steria
Diagnostic financier de [entreprise]
Est-ce que [entreprise] crée de la valeur ?
Valorisation de [entreprise]
```

Aucun paramètre à fournir au-delà du nom de l'entreprise — le skill collecte lui-même les données publiques nécessaires.

## Principes de collecte de données

- Web search privilégié (pas de scraping lourd) pour économiser les tokens.
- Recherche en français pour les entreprises françaises/européennes.
- Recoupement de plusieurs sources pour fiabiliser les chiffres.
- Minimum 2 à 3 années de données pour dégager une tendance.
- Ordre de priorité des sources : rapport annuel officiel > Boursorama/Zonebourse > Morningstar > presse financière (pappers.fr/societe.com en plus pour une PME française non cotée).
- **Aucun chiffre inventé.** Une donnée introuvable est signalée comme telle, avec un proxy raisonnable justifié si nécessaire (ex. bêta sectoriel Damodaran à défaut du bêta de l'entreprise).

## Format de sortie

Un document markdown structuré en 8 sections (une par étape) précédées d'un Executive Summary, suivies d'une synthèse et recommandation. Le détail exact du gabarit est dans [`SKILL.md`](SKILL.md#structure-de-lartefact-de-sortie).

## Ce que l'analyse n'est pas

- **Pas un conseil en investissement personnalisé.** La recommandation BUY/HOLD/SELL découle d'une méthodologie et d'hypothèses explicites (WACC, taux de croissance, comparables retenus) — pas d'une connaissance du profil de risque ou des objectifs de l'utilisateur.
- **Sensible aux hypothèses.** Le prix cible DCF varie significativement avec le WACC et le taux de croissance perpétuel retenus — toujours regarder la fourchette de sensibilité, pas seulement le chiffre central.
- **Aussi fiable que les données trouvées.** Une entreprise peu couverte par la presse financière ou non cotée aura des données plus incertaines (bêta proxy, comparables approximatifs) — le skill le signale plutôt que de présenter un chiffre unique comme certain.

Le détail des formules, seuils d'interprétation et limites de chaque étape est dans [`formulas.md`](formulas.md).

## Structure du dépôt

```
analyse-financiere-entreprise/             (sous-dossier du monorepo Claude Skills)
├── SKILL.md                                # le skill lui-même
├── formulas.md                             # formules, seuils, benchmarks sectoriels, glossaire
├── README.md
├── LICENSE
├── analyse-financiere-entreprise.zip       # package pour l'upload Claude.ai
└── examples/
    ├── README.md
    ├── Analyse-Financiere-OCTO-Technology.md   # entreprise non cotée
    └── Analyse-Financiere-Sopra-Steria.md      # grand groupe coté
```

Le hook qui régénère `analyse-financiere-entreprise.zip` (`.githooks/`) vit à la racine du monorepo, pas dans ce sous-dossier — voir [`../README.md`](../README.md#régénérer-les-zips).

## Régénérer le zip

Ce hook est partagé entre les skills du monorepo : un seul `.githooks/pre-commit`, à la racine, régénère le zip de **chaque** skill dès qu'un de ses fichiers sources fait partie du commit.

**Activation (une fois par clone)**, depuis la racine du monorepo :

```bash
git config core.hooksPath .githooks
```

Détail du fonctionnement et des raisons de ne pas utiliser `Compress-Archive` sous Windows : voir [`../README.md#régénérer-les-zips`](../README.md#régénérer-les-zips).

**Régénération manuelle de ce skill seul** (sans passer par le hook), depuis la racine du monorepo :

```bash
# macOS / Linux
cd analyse-financiere-entreprise
zip -r analyse-financiere-entreprise.zip SKILL.md formulas.md examples/
```

```powershell
# Windows
powershell -NoProfile -ExecutionPolicy Bypass -File .githooks\build-zip.ps1 -Force
```

## Avertissement

Ce skill produit un **diagnostic méthodologique fondé sur des données publiques et des hypothèses explicites**, pas un conseil en investissement personnalisé. La recommandation BUY/HOLD/SELL et le prix cible sont indicatifs, sensibles aux hypothèses retenues (WACC, croissance perpétuelle, comparables), et ne remplacent pas l'avis d'un professionnel avant toute décision d'investissement réelle.

## Contribuer

Les contributions utiles en priorité :

- ajouter des exemples sur d'autres profils d'entreprise (forte croissance FCF négatif, entreprise en difficulté, secteur bancaire au ROE plutôt qu'au ROIC) ;
- affiner les benchmarks sectoriels avec des données de marché à jour ;
- documenter les ajustements spécifiques aux entreprises non cotées (décote d'illiquidité, bêta déliévré/relevéré).

## Licence

MIT — voir [LICENSE](LICENSE).
