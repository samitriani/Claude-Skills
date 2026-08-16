# Exemple — Diagnostic financier complet

> **Donnée entièrement fictive.** « Auréa Industries » n'existe pas ; tous les chiffres (compte de résultat, bilan, cours de bourse) sont inventés pour que les 8 étapes s'enchaînent de façon cohérente. Ils servent uniquement à illustrer le format de sortie et la logique des calculs. Dans une exécution réelle, chaque chiffre est sourcé (rapport annuel officiel, Boursorama, Zonebourse…) et cité comme tel.

## Demande

```
Analyse Auréa Industries
```

## Hypothèse de données collectées (Étape 0 — avant les 8 étapes)

Équipementier industriel fictif, coté, spécialisé dans les machines de production sur-mesure — un positionnement premium qui explique des marges supérieures à la moyenne du secteur « Industrie » générique.

**Compte de résultat (M€) :**

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Chiffre d'affaires | 850 | 920 | 980 |
| Coût des ventes | −570 | −607 | −637 |
| **Marge brute** | 280 | 313 | 343 |
| R&D | −51 | −55 | −59 |
| Frais commerciaux | −68 | −74 | −78 |
| Frais administratifs | −43 | −46 | −49 |
| **EBIT (résultat opérationnel)** | 118 | 138 | 157 |
| Dotations aux amortissements | 45 | 48 | 50 |
| **EBITDA** | 163 | 186 | 207 |
| Charges financières nettes | −14 | −13 | −12 |
| Résultat avant impôt | 104 | 125 | 145 |
| Impôt (taux effectif 25 %) | −26 | −31,25 | −36,25 |
| **Résultat net** | 78 | 93,75 | 108,75 |

**Bilan 2025 (M€) :** stocks 140, créances clients 160, dettes fournisseurs 130, immobilisations brutes 900, amortissements cumulés 380, capitaux propres 480, dettes financières nettes 210, CAPEX 2025 = 58.

**Marché :** capitalisation boursière 1 450 M€, 40 M d'actions en circulation, β = 1,05.

---

# Analyse Financière — Auréa Industries
## Date de l'analyse : 16 août 2026

## Executive Summary

- Croissance solide (+8,2 % en 2024, +6,5 % en 2025) portée par un **effet ciseau positif** : la marge opérationnelle progresse de 13,9 % à 16,0 % en deux ans.
- **ROIC de 17,1 %, très supérieur au WACC de 8,5 %** → EVA positive de +59,3 M€ : l'entreprise crée nettement de la valeur pour ses actionnaires.
- Structure financière saine : gearing 43,8 %, dette nette/EBITDA 1,0x, couverture des intérêts 13,1x — aucune fragilité de bilan.
- FCF robuste (92 M€, FCF yield 6,3 %) mais conversion cash (44,4 %) juste sous le seuil des 50 %, à surveiller.
- **Valorisation par DCF (≈35,8 €) quasiment alignée sur le cours actuel (36,25 €)** → recommandation **HOLD**, la création de valeur semble déjà largement intégrée dans le cours.

## 1. Analyse de la marge

| Indicateur | 2023 | 2024 | 2025 |
|---|---|---|---|
| Marge brute | 32,9 % | 34,0 % | 35,0 % |
| Marge EBITDA | 19,2 % | 20,2 % | 21,1 % |
| Marge opérationnelle (EBIT) | 13,9 % | 15,0 % | 16,0 % |
| Marge nette | 9,2 % | 10,2 % | 11,1 % |
| Coût des ventes en % du CA | 67,1 % | 66,0 % | 65,0 % |
| R&D en % du CA | 6,0 % | 6,0 % | 6,0 % |
| Frais commerciaux en % du CA | 8,0 % | 8,0 % | 8,0 % |
| Frais admin en % du CA | 5,0 % | 5,0 % | 5,0 % |

**Interprétation.** Effet ciseau positif net : le coût des ventes recule de 2,1 points de CA en deux ans (gain de pricing power ou d'échelle industrielle) pendant que les autres postes restent parfaitement stables en proportion. La marge opérationnelle de 16,0 % dépasse largement la fourchette « Industrie » générique (5-12 %, voir [`references/formules.md`](../references/formules.md#benchmarks-sectoriels)), cohérent avec un positionnement premium sur-mesure plutôt que sur des équipements standards.

## 2. Actif économique

| Indicateur | Valeur 2025 |
|---|---|
| BFR | 170 M€ |
| BFR en jours de CA | 63,3 jours |
| Rotation des stocks | 80,2 jours |
| Délai clients | 59,6 jours |
| Délai fournisseurs | 74,5 jours |
| Degré d'usure (Immo nettes / brutes) | 57,8 % |
| Actif économique | 690 M€ |
| Intensité capitalistique (Actif éco / CA) | 70,4 % |
| CAPEX / Amortissements | 1,16x |

**Interprétation.** Le BFR (63 jours de CA) est structurellement positif : Auréa finance son cycle de production avant l'encaissement client, cohérent avec du sur-mesure industriel à cycle long. Le délai fournisseurs (74,5 j) reste supérieur au délai clients (59,6 j), ce qui limite la tension sur le BFR. Le degré d'usure de 57,8 % indique un outil industriel en bon état ; un CAPEX/Amortissements de 1,16x confirme un investissement de renouvellement légèrement supérieur à l'usure, pas de sous-investissement.

## 3. Rentabilité économique (ROIC)

```
NOPAT = EBIT × (1 − 25 %) = 157 × 0,75 = 117,75 M€
ROIC  = NOPAT / Actif économique = 117,75 / 690 = 17,1 %

Décomposition DuPont :
  Taux de marge après impôts = NOPAT / CA        = 117,75 / 980 = 12,0 %
  Rotation de l'actif        = CA / Actif éco     = 980 / 690   = 1,42x
  ROIC = 12,0 % × 1,42 = 17,0 % (≈ 17,1 %, écart d'arrondi)
```

**Interprétation.** Le ROIC de 17,1 % dépasse la fourchette haute « Industrie » (8-14 %) et se rapproche des niveaux tech/pharma. Le driver est mixte : une marge après impôts confortable (12,0 %) combinée à une rotation d'actif honnête (1,42x) — ni un modèle luxe pur (forte marge, faible rotation), ni un modèle distribution pur (l'inverse), mais un équilibre cohérent avec le positionnement premium de niche.

## 4. Structure de financement

| Indicateur | Valeur | Norme | Lecture |
|---|---|---|---|
| Gearing | 43,8 % | < 100 % | Sain, large marge |
| Dette nette / EBITDA | 1,0x | < 3,5x | Très sain |
| Couverture des intérêts | 13,1x | > 3x | Excellent |

**Interprétation.** Aucun signal de fragilité financière. Avec un levier aussi faible (1,0x EBITDA), Auréa dispose d'une capacité d'endettement inexploitée si elle voulait financer une acquisition ou accélérer ses investissements sans diluer ses actionnaires.

## 5. Analyse des flux de trésorerie

| Indicateur | Valeur 2025 |
|---|---|
| Cash-flow opérationnel (CFO) | 150 M€ |
| CAPEX | 58 M€ |
| Free Cash-Flow (FCF) | 92 M€ |
| FCF Yield (FCF / capitalisation) | 6,3 % |
| Conversion cash (FCF / EBITDA) | 44,4 % |

**Interprétation.** FCF largement positif et un FCF yield de 6,3 % (> seuil de 5 % pour une action potentiellement attractive) — configuration saine d'entreprise mature capable d'autofinancer sa croissance. La conversion cash de 44,4 % reste sous le seuil des 50 % considéré comme une bonne conversion : à surveiller si elle continue de se dégrader, mais pas un signal d'alerte à ce niveau.

## 6. Coût du capital (WACC)

```
Ke (MEDAF) = Rf + β × (Rm − Rf) = 3,0 % + 1,05 × 6,0 % = 9,3 %
Kd après impôt = 4,0 % × (1 − 25 %) = 3,0 %

E = 1 450 M€ (capitalisation)   D = 210 M€ (dette nette)   V = 1 660 M€

WACC = (1450/1660) × 9,3 % + (210/1660) × 3,0 %
     = 8,12 % + 0,38 %
     = 8,5 %
```

**Interprétation.** WACC de 8,5 %, dans la fourchette basse-médiane des entreprises européennes (7-10 %) — cohérent avec le profil de risque modéré (bêta 1,05, endettement faible) établi à l'Étape 4.

## 7. Création de valeur (EVA)

```
Spread = ROIC − WACC = 17,1 % − 8,5 % = 8,6 points
EVA    = Spread × Capitaux employés = 8,6 % × 690 = 59,3 M€
MVA    = Capitalisation − Capitaux propres comptables = 1450 − 480 = 970 M€
```

**Interprétation.** ROIC largement supérieur au WACC → **création de valeur nette et significative**. Le MVA de 970 M€ — près de deux fois les capitaux propres comptables — confirme que le marché valorise déjà cette création de valeur bien au-delà de l'actif net comptable, ce qui se retrouvera dans un PBR élevé à l'Étape 8.

## 8. Valorisation

**Multiples (2025) :**

| Multiple | Calcul | Valeur | Benchmark secteur |
|---|---|---|---|
| PER | 36,25 € / 2,72 € (BPA) | 13,3x | 12-18x (industrie) |
| PBR | 1450 / 480 | 3,02x | > 1 = création de valeur perçue |
| EV/EBITDA | 1660 / 207 | 8,0x | 7-12x (industrie) |
| EV/CA | 1660 / 980 | 1,69x | — |

Les trois multiples se situent dans ou légèrement au-dessus de la fourchette « industrie », cohérent avec la prime de qualité déjà identifiée.

**DCF :**

```
FCF projetés (g = 5 %/an, 5 ans) : 96,6 / 101,4 / 106,5 / 111,8 / 117,4 M€
Actualisés au WACC (8,5 %)       : 89,0 / 86,1 / 83,4 / 80,7 / 78,1 M€
Σ FCF actualisés                 = 417,3 M€

Valeur terminale (Gordon-Shapiro, g = 2 %) :
  VT = 117,4 × 1,02 / (8,5 % − 2 %) = 1 842 M€
  VT actualisée                     = 1 225,5 M€

Valeur d'entreprise = 417,3 + 1 225,5 = 1 642,8 M€
Valeur des capitaux propres = 1 642,8 − 210 (dette nette) = 1 432,8 M€
Prix cible par action = 1 432,8 / 40 = 35,8 €
```

**Décote/surcote vs cours actuel (36,25 €) : −1,2 %** — quasiment à sa juste valeur, dans la fourchette ±15 % → **HOLD**.

**Sensibilité (illustrative) :** une variation de ±0,5 point de WACC et ±0,5 point de g fait bouger le prix cible dans une fourchette approximative de 32 € à 41 €.

**Scénarios (illustratifs) :**

| Scénario | Hypothèses | Prix cible approx. | Lecture |
|---|---|---|---|
| Bull | g = 3 %, WACC = 8,0 % | ≈ 42 € | BUY |
| Base | g = 2 %, WACC = 8,5 % | ≈ 36 € | HOLD |
| Bear | g = 1,5 %, WACC = 9,5 % | ≈ 29 € | SELL |

## Synthèse et recommandation

**Recommandation : HOLD, prix cible ≈ 36 € (cours actuel : 36,25 €).**

Auréa Industries est une entreprise financièrement solide qui crée nettement de la valeur (ROIC 17,1 % vs WACC 8,5 %), sans fragilité de bilan et avec un FCF robuste. Le problème n'est pas la qualité du dossier mais son prix : le marché semble déjà avoir intégré cette création de valeur dans le cours, comme le confirment un PBR de 3,0x et une valorisation DCF quasiment alignée sur le cours actuel. Le scénario Bull (croissance plus soutenue, coût du capital en baisse) justifierait un renforcement, mais sur les hypothèses centrales, il n'y a pas de marge de sécurité suffisante pour recommander un achat.

**Risques principaux :** dégradation de la conversion cash sous le seuil des 50 %, sensibilité du prix cible aux hypothèses de croissance perpétuelle et de WACC (fourchette 32-41 € selon les scénarios), absence de vérification par des données de marché réelles dans cet exemple fictif.

---

## Ce que cet exemple illustre

- **La cohérence de bout en bout** : chaque étape réutilise les résultats des précédentes (Actif économique → ROIC → EVA ; WACC → EVA et DCF), jusqu'à la recommandation finale.
- **Un cas nuancé plutôt qu'extrême** : ni franc BUY ni franc SELL — le cas le plus fréquent en pratique, où la qualité de l'entreprise et son prix sont globalement alignés.
- **La discipline de sourcing** : dans une exécution réelle, chaque chiffre du tableau d'hypothèses (Étape 0) serait remplacé par une donnée réellement trouvée et sourcée (rapport annuel, Boursorama, Zonebourse…), jamais inventée comme ici à des fins d'illustration.
