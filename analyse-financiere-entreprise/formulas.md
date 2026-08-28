# Formules et Seuils d'Interprétation — Diagnostic Financier en 8 Étapes

## Table des matières
1. [Étape 1 — Marges](#étape-1--marges)
2. [Étape 2 — Actif économique](#étape-2--actif-économique)
3. [Étape 3 — ROIC](#étape-3--roic)
4. [Étape 4 — Financement](#étape-4--financement)
5. [Étape 5 — Cash-flows](#étape-5--cash-flows)
6. [Étape 6 — WACC](#étape-6--wacc)
7. [Étape 7 — EVA](#étape-7--eva)
8. [Étape 8 — Valorisation](#étape-8--valorisation)
9. [Benchmarks sectoriels](#benchmarks-sectoriels)

---

## Étape 1 — Marges

### Formules

| Indicateur | Formule |
|---|---|
| Marge brute | (CA – Coût des ventes) / CA |
| Marge EBITDA | EBITDA / CA |
| Marge opérationnelle (EBIT) | Résultat opérationnel / CA |
| Marge nette | Résultat net / CA |
| Croissance du CA | (CA_n – CA_n-1) / CA_n-1 |
| Coût des ventes en % | Coût des ventes / CA |
| R&D en % | Frais de R&D / CA |
| Frais commerciaux en % | Frais commerciaux / CA |
| Frais admin en % | Frais administratifs / CA |

### Interprétation

- **Effet ciseau positif** : le CA croît plus vite que les coûts → marge s'améliore.
- **Effet ciseau négatif** : les coûts croissent plus vite que le CA → marge se dégrade. Signal d'alerte.
- **Marge opérationnelle stable** : analyser quelle ligne de coûts compense l'autre (ex: hausse coût des ventes compensée par baisse R&D ou admin).
- **Comparaison sectorielle** : les marges varient drastiquement par secteur. Luxe ~20%+ marge op, distribution ~2-5%, industrie ~5-10%, tech ~15-25%.

### Signaux d'alerte
- Marge nette < 0 pendant 2+ ans
- Marge opérationnelle en baisse continue sur 3 ans
- Coût des ventes en % du CA en hausse → perte de pricing power

---

## Étape 2 — Actif économique

### Formules

| Indicateur | Formule |
|---|---|
| BFR | Stocks + Créances clients – Dettes fournisseurs |
| BFR en jours de CA | BFR / CA × 365 |
| Rotation des stocks (jours) | Stocks / Coût des ventes × 365 |
| Délai clients (jours) | Créances clients / CA × 365 |
| Délai fournisseurs (jours) | Dettes fournisseurs / Achats × 365 |
| Actif économique | BFR + Immobilisations nettes |
| Degré d'usure | Immobilisations nettes / Immobilisations brutes |
| Intensité capitalistique | Actif économique / CA |
| Ratio investissement | CAPEX / Amortissements |

### Interprétation

- **BFR négatif** : l'entreprise est financée par ses fournisseurs (ex: grande distribution, Valeo). Très favorable.
- **BFR élevé et croissant** : la croissance consomme du cash, attention au piège de la croissance.
- **Degré d'usure < 30%** : outil industriel vieillissant, sous-investissement probable.
- **CAPEX / Amortissements > 1** : l'entreprise investit pour renouveler et développer son outil.
- **CAPEX / Amortissements < 1** : l'entreprise laisse vieillir son outil. Acceptable court terme, risqué long terme.

---

## Étape 3 — ROIC

### Formules

| Indicateur | Formule |
|---|---|
| NOPAT | Résultat opérationnel × (1 – Taux d'imposition effectif) |
| ROIC (ROCE) | NOPAT / Capitaux employés |
| Capitaux employés | Capitaux propres + Dettes financières nettes = Actif économique |
| Décomposition DuPont | ROIC = (NOPAT / CA) × (CA / Capitaux employés) |
| Taux de marge après impôts | NOPAT / CA |
| Rotation de l'actif | CA / Capitaux employés |

### Interprétation

- **ROIC > 15%** : excellente rentabilité (pharma, luxe, tech).
- **ROIC 8-15%** : bonne rentabilité.
- **ROIC 5-8%** : rentabilité moyenne, attention si le WACC est proche.
- **ROIC < 5%** : faible rentabilité, risque de destruction de valeur.
- **Forte marge × faible rotation** : modèle luxe/pharma (Hermès, LVMH).
- **Faible marge × forte rotation** : modèle distribution (Carrefour : marge ~2% mais rotation ~4x).
- Exemple cours : Nokia avait 31% de ROIC grâce à rotation de 4,4x. Volkswagen seulement 2% avec marge et rotation faibles.

---

## Étape 4 — Financement

### Formules

| Indicateur | Formule | Norme |
|---|---|---|
| Gearing (levier financier) | Dettes financières nettes / Capitaux propres | < 100% |
| Capacité de remboursement | Dettes financières nettes / EBITDA | < 3,5x |
| Couverture des intérêts | EBIT / Charges financières nettes | > 3x |
| Dettes financières nettes | Dettes financières brutes – Trésorerie et équivalents | — |

### Interprétation

- **Gearing > 100%** : l'entreprise a plus de dettes que de capitaux propres. Fragile. Les banques ne devraient théoriquement pas prêter plus que ce que les actionnaires ont mis.
- **Dette nette / EBITDA > 3,5x** : il faudrait plus de 3,5 ans d'EBITDA pour rembourser la dette. Zone de danger.
- **Dette nette / EBITDA > 5x** : situation très tendue, risque de défaut.
- **Trésorerie nette positive** (dette nette négative) : l'entreprise a plus de cash que de dettes. Position de force.
- **Couverture des intérêts < 2x** : les bénéfices couvrent à peine les intérêts. Très fragile.

---

## Étape 5 — Cash-flows

### Formules

| Indicateur | Formule |
|---|---|
| Cash-flow opérationnel | EBITDA – Impôts cash – Variation du BFR |
| Free Cash-Flow (FCF) | Cash-flow opérationnel – CAPEX |
| FCF Yield | FCF / Capitalisation boursière |
| Conversion cash | FCF / EBITDA |
| Cash-flow de financement | Emprunts nouveaux – Remboursements – Dividendes ± Augmentation de capital |

### Interprétation

- **FCF positif et récurrent** : l'entreprise peut autofinancer sa croissance, rembourser ses dettes, verser des dividendes. Idéal.
- **FCF négatif récurrent** : "la croissance tue le cash" — l'entreprise investit plus qu'elle ne génère. Soutenable uniquement si financé et si le ROIC futur le justifie.
- **FCF Yield > 5%** : action potentiellement attractive.
- **Conversion cash (FCF/EBITDA) > 50%** : bonne conversion du profit en cash.
- **Configuration saine** : flux opérationnel positif, flux d'investissement négatif (on investit), flux de financement qui équilibre.
- **Signal d'alerte** : flux opérationnel négatif → l'activité ne génère pas de cash. Problème fondamental.

### Patterns à identifier
- **Entreprise mature** : FCF largement positif, investissements modérés, dividendes généreux.
- **Entreprise en croissance** : FCF négatif ou faible car CAPEX élevé, mais CFO en croissance.
- **Entreprise en difficulté** : CFO faible/négatif, financement par dette croissante, FCF très négatif.

---

## Étape 6 — WACC

### Formules

```
WACC = (E/V) × Ke + (D/V) × Kd × (1 – T)
```

Où :
- E = Capitalisation boursière (valeur de marché des capitaux propres)
- D = Dettes financières nettes
- V = E + D
- T = Taux effectif d'imposition

**Coût des capitaux propres (MEDAF / CAPM) :**

```
Ke = Rf + β × (Rm – Rf)
```

| Paramètre | Source | Valeur typique (Europe, 2024-2025) |
|---|---|---|
| Rf (taux sans risque) | OAT 10 ans / Bund 10 ans | 2,5 – 3,5% |
| β (bêta) | Boursorama, Reuters, Yahoo Finance | Variable par entreprise |
| Rm – Rf (prime de risque) | Consensus / Damodaran | 5 – 7% |

**Coût de la dette :**

```
Kd = Charges financières / Dettes financières brutes moyennes
```

Ou taux des dernières émissions obligataires.

### Interprétation

- **WACC typique entreprise européenne** : 7-10%.
- **WACC élevé (>12%)** : entreprise perçue comme risquée (petite taille, secteur cyclique, fort endettement, pays émergent).
- **WACC bas (<7%)** : entreprise perçue comme sûre (utilities, grande taille, faible beta).
- Plus le β est élevé, plus l'action est sensible aux mouvements de marché, plus le Ke est élevé.

### Proxys si données manquantes
- Si pas de beta disponible : utiliser le beta sectoriel moyen (Damodaran publie ces données).
- Si entreprise non cotée : utiliser le beta de sociétés comparables cotées, ajusté du levier financier.

---

## Étape 7 — EVA

### Formules

| Indicateur | Formule |
|---|---|
| Spread | ROIC – WACC |
| EVA | (ROIC – WACC) × Capitaux employés |
| MVA (Market Value Added) | Capitalisation boursière – Capitaux propres comptables |

### Interprétation

- **ROIC > WACC** → EVA positive → Création de valeur. L'entreprise génère des surprofits au-delà de l'exigence des pourvoyeurs de fonds.
- **ROIC < WACC** → EVA négative → Destruction de valeur. Les actionnaires auraient été mieux rémunérés ailleurs.
- **ROIC = WACC** → Ni création ni destruction. L'entreprise rémunère exactement le coût de ses ressources.

### Corrélation statistique
Le ratio ROIC/WACC explique environ 2/3 des variations de valorisation boursière (R² ≈ 0,66). Ce n'est pas juste théorique : les entreprises avec un fort spread ont un PBR élevé.

### Cas remarquables (exemples du cours)
- **Coca-Cola** : ROIC > 20%, EVA très positive. Maintenue grâce au marketing massif (20-30% du CA en pub), présence physique mondiale, accords exclusifs d'embouteillage.
- **Peugeot** (cas historique) : Capitalisation boursière 2,2 Mds vs capitaux propres comptables 13,8 Mds → massive destruction de valeur (PBR ≈ 0,16).
- **Atos** (2012) : WACC 12%, ROIC 14,6% → création de valeur positive.

---

## Étape 8 — Valorisation

### Méthode 1 : Patrimoniale (ANR)

```
ANR = Actifs réévalués – Dettes
```

Inclure : plus-values latentes sur immobilier, marques non comptabilisées, brevets.
Exclure : goodwill si non justifié par des cash-flows.

### Méthode 2 : Multiples comparables

| Multiple | Formule | Usage |
|---|---|---|
| PER | Cours / BPA | Le plus courant. < 10 = value, 10-20 = fair, > 25 = growth |
| PBR | Capitalisation / Capitaux propres | < 1 = destruction de valeur perçue, > 1 = création |
| EV/EBITDA | (Capi + Dette nette) / EBITDA | Comparable cross-border (neutralise fiscalité et structure financière) |
| EV/CA | (Capi + Dette nette) / CA | Pour entreprises déficitaires ou en forte croissance |

**Application :** Identifier 3-5 sociétés comparables (même secteur, même taille, même zone géographique). Calculer la médiane des multiples. Appliquer au sujet.

### Méthode 3 : DCF (Discounted Cash-Flow)

```
Valeur d'entreprise = Σ(t=1 à n) [FCF_t / (1 + WACC)^t] + VT / (1 + WACC)^n
```

**Valeur terminale (Gordon-Shapiro) :**

```
VT = FCF_n × (1 + g) / (WACC – g)
```

- g = taux de croissance perpétuelle (typiquement 1,5 – 2,5%, ne jamais dépasser le PIB nominal long terme).

**Valeur des capitaux propres :**

```
Valeur CP = Valeur d'entreprise – Dette financière nette
Prix cible par action = Valeur CP / Nombre d'actions
```


**Analyse de sensibilité :** Toujours faire varier WACC (±0,5-1%) et g (±0,5%) pour montrer la fourchette de valorisation.

### Recommandation

| Décote/Surcote | Recommandation |
|---|---|
| Prix cible > cours actuel + 15% | **BUY** (Acheter) |
| Prix cible dans ±15% du cours | **HOLD** (Conserver) |
| Prix cible < cours actuel – 15% | **SELL** (Vendre) |

Toujours accompagner de scénarios Bull / Base / Bear avec pondération.

---

## Benchmarks sectoriels (ordres de grandeur)

| Secteur | Marge op. typique | ROIC typique | EV/EBITDA typique | PER typique |
|---|---|---|---|---|
| Luxe | 20-30% | 15-25% | 15-25x | 25-35x |
| Pharma | 15-25% | 12-20% | 12-18x | 18-25x |
| Tech / Software | 15-30% | 15-30% | 15-25x | 25-40x |
| Industrie | 5-12% | 8-14% | 7-12x | 12-18x |
| Distribution | 2-5% | 8-15% | 6-10x | 10-18x |
| Telecom / Utilities | 15-25% | 5-10% | 6-9x | 10-15x |
| Banque | N/A (marge d'intérêt) | 8-12% (ROE) | N/A | 7-12x |
| Agroalimentaire | 3-8% | 6-12% | 8-12x | 15-20x |
| Automobile | 3-8% | 5-10% | 3-6x | 5-10x |
| Énergie | 5-15% | 8-15% | 5-8x | 8-14x |

Ces benchmarks sont des ordres de grandeur indicatifs. Toujours vérifier avec les données actuelles du secteur via web search.

---

## Glossaire rapide

| Terme | Définition |
|---|---|
| NOPAT | Net Operating Profit After Tax — Résultat opérationnel après impôts |
| ROIC | Return On Invested Capital — Rentabilité des capitaux investis |
| ROCE | Return On Capital Employed — Synonyme de ROIC |
| WACC | Weighted Average Cost of Capital — Coût moyen pondéré du capital |
| EVA | Economic Value Added — (ROIC – WACC) × Capitaux employés |
| FCF | Free Cash-Flow — Flux de trésorerie libre |
| BFR | Besoin en Fonds de Roulement |
| CAPEX | Capital Expenditures — Investissements en immobilisations |
| EBITDA | Earnings Before Interest, Taxes, Depreciation and Amortization |
| EBIT | Earnings Before Interest and Taxes — Résultat opérationnel |
| PER | Price Earnings Ratio — Cours / BPA |
| PBR | Price to Book Ratio — Capitalisation / Capitaux propres |
| DCF | Discounted Cash-Flow — Flux de trésorerie actualisés |
| ANR | Actif Net Réévalué |
| BPA | Bénéfice Par Action |
| Gearing | Levier financier — Dette nette / Capitaux propres |