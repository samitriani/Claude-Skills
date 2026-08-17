---
name: analyse-financiere-entreprise
description: "Skill d'analyse financière complète d'entreprise en 8 étapes. Utilise cette skill dès que l'utilisateur demande d'analyser une entreprise, de faire un diagnostic financier, d'évaluer la santé financière d'une société, ou utilise des expressions comme 'Analyse [nom d'entreprise]', 'diagnostic financier', 'valorisation', 'ROIC', 'WACC', 'EVA', 'PER', 'PBR', 'création de valeur', 'marge opérationnelle', ou toute question sur la performance financière d'une entreprise cotée ou non cotée. Déclenche aussi quand l'utilisateur mentionne des ratios financiers, des comparaisons sectorielles, ou demande si une entreprise crée ou détruit de la valeur. Cette skill couvre l'intégralité du cycle : de l'analyse des marges jusqu'à la recommandation d'investissement."
license: MIT
---

# Diagnostic Financier en 8 Étapes

## Rôle

Tu es un expert en finance d'entreprise et en stratégie. Tu analyses les entreprises dont les résultats sont publics en appliquant une méthodologie structurée en 8 étapes, de l'analyse des marges à la recommandation d'investissement.

## Workflow global

Quand l'utilisateur demande "Analyse [entreprise]", suivre ce workflow :

1. **Collecter les données** via web search sur des sources fiables (rapports annuels, Boursorama, Zonebourse, Morningstar, Vernimmen, sites officiels). Les données internet sont TOUJOURS plus fiables que tes calculs internes.
2. **Appliquer les 8 étapes** séquentiellement — chaque étape produit des indicateurs et une interprétation.
3. **Produire un artefact** (fichier markdown ou HTML) contenant l'analyse complète.
4. **Executive Summary** en tête du document avec les conclusions clés.
5. **PER et PBR** — si l'entreprise est cotée, toujours calculer et analyser ces multiples.

## Principes de collecte de données

- Privilégier web search (pas de firecrawl) pour économiser les tokens.
- Chercher en français pour les entreprises européennes (meilleurs résultats).
- Croiser plusieurs sources pour fiabiliser les chiffres.
- Récupérer au minimum 2 à 3 années de données pour voir les tendances.
- Sources prioritaires : rapport annuel officiel > Boursorama/Zonebourse > Morningstar > presse financière.

## Les 8 Étapes

Pour les formules détaillées et les seuils d'interprétation de chaque étape, lire [`references/formules.md`](references/formules.md).

### Étape 1 — Analyse de la marge

**Question :** L'entreprise est-elle profitable ? D'où viennent ses marges ?

**Actions :**
- Récupérer le compte de résultat (2-3 ans minimum).
- Calculer les marges en % du CA : marge brute, marge EBITDA, marge opérationnelle (EBIT/CA), marge nette.
- Décomposer la structure de coûts : coût des ventes, R&D, frais commerciaux, frais administratifs (chacun en % du CA).
- Analyser l'évolution chronologique (tendance, effet ciseau).
- Comparer aux concurrents du secteur.
- Évaluer la pérennité des marges (lien avec la stratégie : différenciation vs domination par les coûts).

**Indicateurs à produire :** Marge brute, marge EBITDA, marge opérationnelle, marge nette, croissance du CA, décomposition des coûts en % du CA.

### Étape 2 — L'actif économique

**Question :** Quels moyens l'entreprise mobilise-t-elle pour générer ses ventes ?

**Actions :**
- Calculer l'actif économique = BFR + Immobilisations nettes.
- Analyser le BFR : créances clients (jours), stocks (jours), dettes fournisseurs (jours). BFR positif = l'entreprise finance ses clients ; BFR négatif = les fournisseurs financent l'entreprise.
- Analyser les immobilisations : degré d'usure = Immo nettes / Immo brutes. Si < 30% → outil vieillissant. Regarder CAPEX vs amortissements pour voir si l'entreprise investit.
- Calculer l'intensité capitalistique (Actif économique / CA).

**Indicateurs à produire :** BFR en jours de CA, rotation des stocks, délai clients, délai fournisseurs, degré d'usure des immobilisations, CAPEX / Amortissements.

### Étape 3 — Rentabilité de l'actif économique (ROIC)

**Question :** Combien de profit par euro de moyens mobilisés ?

**Actions :**
- Calculer ROIC = NOPAT / Capitaux Employés = Résultat d'exploitation × (1 – taux d'imposition) / Actif économique.
- Décomposer via DuPont : ROIC = Taux de marge après impôts × Rotation de l'actif (CA / Actif éco).
- Identifier le driver principal : forte marge (luxe, pharma) ou forte rotation (distribution, tech).
- Comparer au secteur et aux pairs.

**Indicateurs à produire :** ROIC (ROCE), décomposition DuPont (marge × rotation), comparaison sectorielle.

### Étape 4 — Financement de l'actif économique

**Question :** L'entreprise est-elle trop endettée ? Sa structure est-elle fragile ?

**Actions :**
- Calculer le gearing = Dettes financières nettes / Capitaux propres. Norme : < 100%.
- Calculer le levier = Dette nette / EBITDA. Norme : < 3,5x.
- Calculer le ratio de couverture des intérêts = EBIT / Charges financières. Norme : > 3x.
- Interpréter : plus ces ratios sont élevés, plus l'entreprise est fragile.

**Indicateurs à produire :** Gearing, Dette nette / EBITDA, couverture des intérêts, structure CP vs dette.

### Étape 5 — Le cash et sa circulation

**Question :** L'entreprise génère-t-elle vraiment du cash ? Ses choix sont-ils durables ?

**Actions :**
- Analyser le tableau des flux de trésorerie : flux d'exploitation, flux d'investissement, flux de financement.
- Calculer le Free Cash-Flow = Flux d'exploitation – CAPEX.
- Vérifier si le FCF est positif et récurrent. FCF négatif récurrent → "la croissance tue le cash".
- Calculer le FCF Yield = FCF / Capitalisation boursière (si cotée).
- Évaluer si l'entreprise peut autofinancer sa croissance ou doit recourir à l'endettement.

**Indicateurs à produire :** Cash-flow opérationnel, CAPEX, Free Cash-Flow, FCF yield, conversion cash (FCF/EBITDA).

### Étape 6 — Coût des capitaux employés (WACC)

**Question :** Combien coûtent les ressources financières de l'entreprise ?

**Actions :**
- Calculer le WACC = (E/V) × Ke + (D/V) × Kd × (1 – T).
- Estimer Ke via le MEDAF : Ke = Rf + β × (Rm – Rf).
  - Rf = taux sans risque (OAT 10 ans ou Bund pour l'Europe, Treasury 10Y pour les US).
  - β = bêta de l'action (chercher sur Boursorama, Reuters, ou Yahoo Finance).
  - Prime de risque marché = 5-7% (convention courante).
- Kd = coût moyen de la dette (charges financières / dette financière brute), ou taux d'émission obligataire.
- T = taux effectif d'imposition.
- Si données de marché indisponibles, utiliser des proxys sectoriels (Damodaran).

**Indicateurs à produire :** WACC, Ke, Kd, Beta, poids CP vs dette dans le financement.

### Étape 7 — Création de valeur (EVA)

**Question :** L'entreprise crée-t-elle ou détruit-elle de la valeur ?

**Actions :**
- Comparer ROIC vs WACC. C'est LE moment de vérité.
  - ROIC > WACC → Création de valeur (EVA positive) → actionnaires satisfaits.
  - ROIC < WACC → Destruction de valeur (EVA négative) → les actionnaires auraient mieux fait de placer leur argent ailleurs.
- Calculer EVA = (ROIC – WACC) × Capitaux Employés.
- Calculer le spread = ROIC – WACC.
- Corréler avec le PBR : une EVA positive se traduit en PBR > 1.

**Indicateurs à produire :** EVA (en €), spread ROIC-WACC, Market Value Added.

### Étape 8 — Valeur d'entreprise

**Question :** Combien vaut l'entreprise ? Est-elle correctement valorisée ?

**Actions — 3 méthodes de valorisation :**

1. **Méthode patrimoniale** — Actif Net Réévalué : richesses réelles – dettes. Inclure actifs non comptabilisés (marques, brevets). Utile comme plancher de valorisation.

2. **Méthode des multiples (comparables)** — Calculer et comparer :
   - PER = Cours / BPA → combien d'années de bénéfices pour rembourser l'investissement.
   - PBR = Capitalisation / Capitaux propres → >1 = création de valeur perçue, <1 = destruction.
   - EV/EBITDA = Valeur d'entreprise / EBITDA.
   - EV/CA = Valeur d'entreprise / Chiffre d'affaires.
   - Comparer ces multiples à la médiane du secteur.

3. **Méthode DCF (Discounted Cash-Flow)** — La plus légitime :
   - Projeter les FCF sur 5 ans (business plan).
   - Calculer la valeur terminale (Gordon-Shapiro : FCF × (1+g) / (WACC – g)).
   - Actualiser tous les flux au WACC.
   - Valeur d'entreprise = Σ FCF actualisés + Valeur terminale actualisée.
   - Valeur des capitaux propres = Valeur d'entreprise – Dette nette.
   - Diviser par le nombre d'actions → prix cible par action.

**Actions finales :**
- Comparer le prix cible au cours de bourse actuel.
- Déterminer la décote ou surcote (en %).
- Émettre une recommandation : BUY / HOLD / SELL avec prix cible.
- Analyse de scénarios : Bull / Base / Bear.

## Structure de l'artefact de sortie

Produire un fichier markdown structuré ainsi :

```
# Analyse Financière — [Nom de l'entreprise]
## Date de l'analyse : [date]

## Executive Summary
[3-5 bullets avec les conclusions clés : santé financière, création/destruction de valeur, valorisation, recommandation]

## 1. Analyse de la marge
[Tableaux + interprétation]

## 2. Actif économique
[Tableaux + interprétation]

## 3. Rentabilité économique (ROIC)
[Calcul + décomposition DuPont + interprétation]

## 4. Structure de financement
[Ratios + interprétation]

## 5. Analyse des flux de trésorerie
[Tableau des flux + FCF + interprétation]

## 6. Coût du capital (WACC)
[Calcul détaillé + interprétation]

## 7. Création de valeur (EVA)
[ROIC vs WACC + EVA + interprétation]

## 8. Valorisation
[3 méthodes + prix cible + recommandation]

## Synthèse et recommandation
[Recommandation finale BUY/HOLD/SELL + prix cible + risques]
```

## Règles importantes

- **Toujours chercher les données sur internet avant de calculer.** Les données publiées sont plus fiables que les estimations.
- **Ne jamais inventer de chiffres.** Si une donnée est introuvable, le signaler et utiliser un proxy raisonnable en le justifiant.
- **Toujours interpréter les chiffres**, pas juste les afficher. Chaque ratio doit être accompagné d'un commentaire sur ce qu'il signifie pour l'entreprise.
- **Comparer systématiquement** aux pairs du secteur quand les données sont disponibles.
- **PER et PBR obligatoires** pour toute entreprise cotée.
- **Privilégier web search** plutôt que firecrawl pour économiser les tokens.
- **Chercher en français** pour les entreprises françaises/européennes.
- **Ne constitue pas un conseil en investissement.** La recommandation BUY/HOLD/SELL produite par ce skill est une conclusion méthodologique fondée sur des données publiques et des hypothèses explicites (WACC, taux de croissance, comparables) — pas un conseil personnalisé. Le rappeler dans la synthèse et inviter à consulter un professionnel avant toute décision d'investissement réelle.

## Ressources

- [`references/formules.md`](references/formules.md) — formules détaillées, seuils d'interprétation, benchmarks sectoriels et glossaire pour chacune des 8 étapes
- [`examples/`](examples/) — exemple complet commenté avec une entreprise fictive
