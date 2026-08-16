# Analyse Locative

Skill Claude pour rechercher des biens immobiliers locatifs en France, les situer avec des données INSEE, estimer leurs loyers de marché et calculer leurs indicateurs de rendement — puis produire un tableau prêt à coller dans un tableur ainsi qu'une analyse avec un verdict par bien et une recommandation.

**Périmètre : France.** Frais de notaire, taxe foncière, assurance PNO, encadrement des loyers, interdictions de location liées au DPE : tout le modèle de calcul est spécifique au droit français.

---

## Ce que fait le skill

Sur une commande comme `Analyse locative Saint-Étienne T2 80000 apport 5000`, il :

1. **cherche des biens réellement en vente** sur les plateformes immobilières (LeBonCoin, SeLoger, PAP, Bien'ici…) ;
2. **situe la ville avec des données INSEE** : démographie, revenu médian, part de locataires, indice des prix immobiliers ;
3. **estime un loyer de marché** pour chacun, et **qualifie la solidité de cette estimation** ;
4. **calcule** frais de notaire, coût total, emprunt, mensualités sur 20 et 25 ans, rendement brut, rendement net et cashflow ;
5. **génère un bloc de 19 colonnes séparées par des tabulations**, à coller directement dans Google Sheets, Excel ou LibreOffice ;
6. **produit une analyse complète** : un verdict (🟢/🟡/🔴) par bien selon des règles fixes, et une recommandation de synthèse croisée avec le contexte INSEE.

## Installation

L'installation diffère selon l'application utilisée.

### Claude.ai (app de bureau, web, mobile)

1. Télécharge [`analyse-locative.zip`](analyse-locative.zip) depuis ce dépôt (clique sur le fichier, puis *Download raw file*).
2. Dans l'app : **Réglages → Capacités (Capabilities) → Skills**. Sur un compte Team/Enterprise, un administrateur doit parfois activer Skills au niveau de l'organisation avant que l'option n'apparaisse.
3. **Créer/Importer un skill** → sélectionne `analyse-locative.zip`.
4. Active le skill (bascule on) — globalement ou pour la conversation en cours.

Skills est réservé aux plans payants (Pro, Max, Team, Enterprise) ; l'intitulé exact des menus peut varier selon les déploiements.

Le zip contient uniquement `SKILL.md`, `references/` et `examples/` — pas `README.md` ni `LICENSE`, qui ne servent qu'à la publication GitHub. **Si tu modifies `SKILL.md` ou les fichiers `references/`/`examples/`, régénère le zip avant de le réimporter** (une archive périmée fera tourner l'ancienne version du skill) — voir [Régénérer le zip](#régénérer-le-zip) plus bas.

### Claude Code (CLI, IDE, app de bureau)

Copier le dossier dans le répertoire des skills de Claude :

```bash
git clone https://github.com/<votre-compte>/analyse-locative.git ~/.claude/skills/analyse-locative
```

Le nom du dossier doit correspondre au champ `name` du frontmatter de `SKILL.md` (minuscules, chiffres et tirets uniquement) — c'est déjà le cas ici. Le nom du dépôt GitHub, lui, est libre.

Le skill se déclenche ensuite sur toute formulation commençant par « Analyse locative ».

## Utilisation

```
Analyse locative Saint-Étienne
Analyse locative Mulhouse 70000
Analyse locative Lyon T3
Analyse locative Angers T3 neuf 200000 apport 20000
Analyse locative Reims studio 60000
Analyse locative Nantes pour un apport de 20000
```

Les paramètres se combinent librement, dans n'importe quel ordre, en langage naturel. Seule la ville est obligatoire.

### Paramètres

| Paramètre | Valeurs | Défaut |
|-----------|---------|--------|
| Ville | toute commune française | **obligatoire** |
| Type de bien | `studio`, `T1`, `T2`, `T3`, `T4`, `T5`, `maison`, `immeuble` | `T2` |
| Budget max | montant en € | aucun — demandé si absent |
| Apport | montant en €, ou `0` pour un financement à 110 % | 10 % du coût total |
| État | `ancien` ou `neuf` | `ancien` |
| Frais de notaire | déduits de l'état du bien | 8 % ancien / 2,5 % neuf |
| Taux de crédit | recherché sur le web, sinon 3,5 % | — |

## Format de sortie

19 colonnes séparées par des tabulations, sans ligne d'en-tête :

| # | Colonne | # | Colonne |
|---|---------|---|---------|
| 1 | Ville | 11 | **Fiabilité loyer** |
| 2 | Adresse / Description | 12 | Charges copro /mois (€) |
| 3 | Surface (m²) | 13 | Taxe foncière /mois (€) |
| 4 | Prix achat (€) | 14 | Assurance PNO /mois (€) |
| 5 | Frais notaire (€) | 15 | Vacance loc. /mois (€) |
| 6 | Coût total (€) | 16 | Rendement brut (%) |
| 7 | Emprunt nécessaire (€) | 17 | Rendement net (%) |
| 8 | Mensualité 20 ans (€) | 18 | Cashflow /mois 25 ans (€) |
| 9 | Mensualité 25 ans (€) | 19 | Lien annonce |
| 10 | Loyer HC (€) | | |

Une ligne d'en-tête prête à coller est fournie dans [`examples/en-tetes.tsv`](examples/en-tetes.tsv).

### La colonne « Fiabilité loyer »

Le loyer est la variable qui pèse le plus sur le rendement, et c'est aussi la plus incertaine. La colonne 11 dit d'où vient le chiffre :

| Valeur | Signification | Confiance |
|--------|---------------|-----------|
| `Loyer en place` | Bien vendu loué, loyer contractuel connu | Élevée |
| `Annonce réelle` | Loyer relevé sur une annonce de location comparable en ligne | Bonne |
| `Estimation marché` | Extrapolation depuis un prix moyen au m² | À vérifier |

Une ligne `Estimation marché` peut se tromper d'un point de rendement dans un sens comme dans l'autre. Le skill cite les annonces comparables utilisées pour les lignes `Annonce réelle`, ce qui permet de contrôler le raisonnement.

## Contexte marché (INSEE)

Avant le tableau, le skill affiche un bloc de contexte propre à la ville — une donnée de commune, pas de bien, donc **non intégrée au TSV** pour ne pas dupliquer la même valeur sur chaque ligne :

```
Contexte marché — Saint-Étienne (INSEE)
- Population : 171 000 hab. (stable, -0,1 %/an sur 2016-2022)
- Revenu médian mensuel du ménage : 1 650 € (FiLoSoFi 2022)
- Part de locataires dans le parc de logements : 54 %
- Indice des prix immobiliers : +2,1 % sur 1 an, +6,4 % sur 5 ans (Notaires-INSEE)
- Taux d'effort locatif type : 25,5 % (loyer moyen retenu ÷ revenu médian)
```

Le **taux d'effort locatif** (loyer ÷ revenu médian du ménage) situe le loyer par rapport au pouvoir d'achat local : sous 25 %, une marge de revalorisation est probable ; au-delà de 33 %, le loyer est considéré comme tendu pour le ménage médian de la commune.

## Analyse et verdicts

Au-delà du tableau, le skill livre une analyse structurée : chaque bien reçoit un verdict selon des règles fixes, pas une impression qualitative.

| Verdict | Condition |
|---------|-----------|
| 🟢 Prioritaire | Cashflow 25 ans ≥ 0 € et loyer fiable (`Loyer en place` ou `Annonce réelle`) et pas de DPE F/G non budgété |
| 🟡 À creuser | Cashflow entre −150 € et 0 €, ou loyer estimé avec un rendement net ≥ 5 %, ou DPE F sans budget travaux |
| 🔴 À écarter | Cashflow < −150 €/mois, ou DPE G non budgété, ou prix anormalement bas et inexpliqué |

Ces verdicts alimentent une **recommandation de synthèse** en prose (pas une liste) : quels biens visiter en priorité et pourquoi, lesquels écarter, et un croisement avec le contexte INSEE (une ville en déclin démographique tempère un verdict par ailleurs favorable ; un taux d'effort déjà élevé limite la marge de revalorisation). Si aucun bien n'atteint 🟢, le skill le dit explicitement plutôt que de forcer un classement flatteur.

Le détail des règles est dans [`references/calculs.md`](references/calculs.md#9-verdicts-et-recommandation).

## Ce que les calculs n'incluent pas

Les chiffres produits sont volontairement simples et légèrement optimistes. Avant toute décision, retrancher :

- **l'assurance emprunteur** — 10 à 35 €/mois pour 100 000 € empruntés ; c'est le principal écart avec une simulation bancaire réelle ;
- **les frais de garantie et de dossier** — 1 % à 1,5 % du montant emprunté, plus 500 à 1 500 € ;
- **les frais de gestion locative** — 6 % à 9 % des loyers en agence ;
- **la provision pour travaux** — usuellement 5 % du loyer annuel ;
- **la fiscalité** — le « rendement net » est un net de charges, **avant impôt**.

Le détail complet est dans [`references/calculs.md`](references/calculs.md).

## Contraintes réglementaires signalées

Le skill ne les calcule pas mais les mentionne quand elles s'appliquent :

- **DPE** — les logements classés G sont interdits à la location en métropole depuis le 1ᵉʳ janvier 2025, les F le seront au 1ᵉʳ janvier 2028, les E au 1ᵉʳ janvier 2034.
- **Encadrement des loyers** — applicable dans plusieurs agglomérations, avec une liste qui évolue.
- **Zone tendue** — impacte préavis et évolution des loyers entre deux locations.

## Structure du dépôt

```
analyse-locative/
├── SKILL.md                          # le skill lui-même
├── README.md
├── LICENSE
├── analyse-locative.zip              # package pour l'upload Claude.ai (SKILL.md + references/ + examples/)
├── .githooks/
│   ├── pre-commit                    # régénère et ajoute le zip quand une source change
│   └── build-zip.ps1                 # construction du zip sous Windows (contourne le bug Compress-Archive)
├── examples/
│   ├── README.md
│   ├── t2-ancien-saint-etienne.md    # session complète, ancien
│   ├── t3-neuf-angers.md             # session complète, neuf
│   ├── en-tetes.tsv
│   ├── sortie-t2-ancien.tsv
│   └── sortie-t3-neuf.tsv
└── references/
    └── calculs.md                    # formules, hypothèses, limites
```

## Régénérer le zip

Un hook `pre-commit` régénère `analyse-locative.zip` automatiquement dès que `SKILL.md`, `references/calculs.md` ou un fichier de `examples/` fait partie du commit — sans lui, une archive périmée ferait tourner une version obsolète du skill dans Claude.ai.

**Activation (une fois par clone)** — git ne suit pas `.git/hooks/`, il faut donc pointer explicitement vers le dossier versionné du dépôt :

```bash
git config core.hooksPath .githooks
```

Le hook ([`.githooks/pre-commit`](.githooks/pre-commit)) détecte les fichiers sources modifiés, régénère le zip et l'ajoute au commit en cours. Sur macOS/Linux il utilise la commande `zip` ; sur Windows, faute de `zip`, il appelle [`.githooks/build-zip.ps1`](.githooks/build-zip.ps1) via PowerShell.

**Pourquoi pas `Compress-Archive`** : sous Windows PowerShell 5.1, cette cmdlet stocke les chemins avec des antislashs (`references\calculs.md`), ce qui viole la norme ZIP (séparateur `/` requis) et fait échouer l'import dans Claude.ai avec l'erreur *« Zip file contains path with invalid characters »*. `build-zip.ps1` construit donc l'archive entrée par entrée via l'API .NET en forçant le bon séparateur.

**Régénération manuelle** (si le hook n'est pas actif, par exemple juste après un clone avant d'avoir lancé la commande ci-dessus) :

```bash
# macOS / Linux
cd analyse-locative
zip -r analyse-locative.zip SKILL.md references/ examples/
```

```powershell
# Windows
powershell -NoProfile -ExecutionPolicy Bypass -File .githooks\build-zip.ps1
```

Vérifier ensuite qu'aucune entrée ne contient de `\` :

```bash
unzip -l analyse-locative.zip
```

## Avertissement

Ce skill produit une **première sélection chiffrée et un classement indicatif**, pas une étude d'investissement. Les verdicts et la recommandation de synthèse sont fondés sur des règles reproductibles appliquées aux données trouvées — pas sur le profil, la fiscalité ou les objectifs personnels de l'utilisateur. Ils ne constituent **ni un conseil en investissement, ni une recommandation d'achat**. Avant tout engagement : visiter le bien, lire les PV d'assemblée générale, vérifier charges et taxe foncière auprès du vendeur, faire simuler le financement réel par une banque ou un courtier, et valider le régime fiscal avec un professionnel.

## Contribuer

Les contributions utiles en priorité :

- affiner les fourchettes de charges et de taxe foncière par ville ;
- ajouter le calcul de l'assurance emprunteur et des frais de garantie ;
- modéliser les régimes fiscaux (micro-foncier, réel, LMNP) pour un rendement net-net ;
- brancher la base DVF pour fiabiliser les prix au m² ;
- passer du contexte INSEE communal à une granularité IRIS (quartier) dans les grandes villes.

## Licence

MIT — voir [LICENSE](LICENSE).
