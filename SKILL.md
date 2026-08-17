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

1. **Étape 0 — Collecter et vérifier les données** (ci-dessous). Ne jamais entamer les calculs sur des données non vérifiées.
2. **Appliquer les 8 étapes** séquentiellement — chaque étape produit des indicateurs et une interprétation.
3. **Passer les contrôles de cohérence**, de préférence via `scripts/verifier_coherence.py` (§ 0.6) — **avant** d'écrire l'Étape 6 et la restitution.
4. **Produire un artefact** (fichier markdown ou HTML) contenant l'analyse complète.
5. **Executive Summary** en tête du document avec les conclusions clés.
6. **PER et PBR** — si l'entreprise est cotée, toujours calculer et analyser ces multiples.

## Étape 0 — Collecte et vérification des données

Cette étape n'est pas un préliminaire optionnel : **la quasi-totalité des erreurs d'un diagnostic financier vient d'un input faux, pas d'un calcul faux.** Un chiffre erroné en entrée se propage silencieusement dans 5 étapes en aval sans qu'aucune ne le conteste.

### 0.1 — Hiérarchie des sources

| Niveau | Sources | Usage |
|---|---|---|
| **1 — Primaire officielle** | Comptes sociaux déposés au greffe (PDF complet : bilan, compte de résultat, **annexe**, rapport du commissaire aux comptes) via [data.inpi.fr](https://data.inpi.fr) (RNE, gratuit, officiel), Pappers ou Infogreffe. Pour les cotées : URD / rapport annuel, communiqués AMF | **La seule source qui tranche.** Seul niveau donnant le détail poste par poste |
| **2 — Agrégateurs** | Pappers, Societe.com, Infonet | Point d'entrée normal. Republient le niveau 1 avec des ratios pré-calculés (BFR, EBITDA, CAF, ROE) — précieux, mais **agrégés** : le détail disparaît |
| **3 — Marché et presse** | Boursorama, Zonebourse, presse financière | Cours, bêta, capitalisation, transactions, contexte. Indispensable — ces données n'existent pas dans les comptes sociaux |
| **4 — Communication de l'entreprise** | Site institutionnel, communiqués | Contexte qualitatif **uniquement**. Un « 200+ consultants » affiché sur un site est du marketing, jamais une donnée d'effectif — ne pas le mélanger avec l'INSEE |

Chercher en français pour les entreprises françaises et européennes. Récupérer au minimum 2 à 3 exercices pour dégager une tendance.

**Réserve à connaître** : les petites entreprises peuvent demander la **confidentialité** de leurs comptes déposés. Pour une micro-entreprise, le détail peut simplement ne pas exister publiquement — c'est une réponse valide, pas un échec de recherche.

**Piège central : comptes sociaux ≠ comptes consolidés.** Pappers, Societe.com et Infogreffe donnent les **comptes sociaux** — l'entité juridique française isolée. Pour une PME/ETI à entité unique (le cas le plus courant), c'est exactement ce qu'il faut. **Pour un groupe qui a des filiales** (a fortiori un grand groupe coté), chercher le nom de la société sur ces sites renvoie souvent les comptes sociaux de la **société mère ou holding française** — une coquille juridique presque vide, puisque l'activité réelle est logée dans les filiales. Ce n'est pas juste incomplet, c'est **trompeur** : ces comptes existent, ont l'air normaux, et analysent la mauvaise entité sans le signaler. Dès que l'entreprise a des filiales consolidées, la source de niveau 1 devient les **comptes consolidés** du groupe (Document d'Enregistrement Universel pour une cotée française, rapport annuel sinon), pas les comptes sociaux de la maison mère. Vérifier en premier : cette entreprise a-t-elle des filiales significatives ? Si oui, chercher explicitement « comptes consolidés » ou « rapport annuel groupe », pas seulement le nom de l'entreprise sur un agrégateur.

### 0.2 — Un rapport de recherche délégué est une piste, pas une source

Si la collecte a été déléguée (sous-agent, recherche automatisée, synthèse d'un tiers), son rapport indique **où chercher**, il ne constitue pas la donnée. Les **inputs critiques** — ceux qui alimentent trois étapes ou plus — doivent être confirmés sur la page ou le document source avant d'entrer dans un calcul :

> **CA · EBIT · EBITDA · Capitaux propres · Dette financière · Trésorerie · Immobilisations nettes**

Les autres données peuvent rester au niveau du rapport, à condition d'être étiquetées comme telles (§ 0.4).

**Piège classique, à vérifier explicitement** : au passif d'un bilan français, la ligne `TOTAL DETTES` agrège dettes financières **et** dettes d'exploitation (fournisseurs, fiscales et sociales, produits constatés d'avance). La dette financière, ce sont uniquement les lignes `Emprunts obligataires`, `Emprunts et dettes auprès des établissements de crédit` et `Emprunts et dettes financières divers`. Confondre les deux fausse le gearing, les capitaux employés, le WACC, l'EVA et la valorisation d'un seul coup.

### 0.3 — Le chiffre publié prime sur le chiffre recalculé

Si une source publie directement un indicateur (BFR, EBITDA, CAF, ROE, délais de paiement), **retenir son chiffre**. Ne recalculer que pour contrôler — et si l'écart dépasse 5 %, ne pas trancher arbitrairement : appliquer la règle d'escalade (§ 0.5).

Reconstruire un indicateur à partir de composants partiels donne un résultat faux dès qu'un composant manque. Un BFR reconstitué à partir des seuls postes clients et fournisseurs ignore les dettes fiscales et sociales, souvent massives dans les sociétés de services — et peut se tromper d'un facteur 3.

### 0.4 — Traçabilité et propagation de l'incertitude

Chaque donnée porte un statut (valeurs exactes attendues dans `donnees-financieres.json`, § 0.6) :

| Statut | Signification |
|---|---|
| `verifie-source` | Confirmé sur le document ou la page source primaire |
| `secondaire` | Vient d'un agrégateur ou d'un rapport délégué, non re-vérifié |
| `estime` | Proxy ou hypothèse — la méthode de calcul doit être explicitée sur place |
| `non-trouve` | Recherché sans succès |

**Règle de propagation : tout indicateur dérivé hérite du statut le plus faible de ses inputs.** Un ROIC calculé à partir d'une dette `secondaire` est un ROIC `secondaire`, et l'EVA qui en découle aussi — jusque dans l'Executive Summary. Le lecteur doit voir où l'analyse est fragile sans avoir à le deviner.

**« Je n'ai pas trouvé » n'est pas « ça n'existe pas ».** Ne jamais écrire qu'une donnée est indisponible publiquement sans avoir consulté la source primaire — c'est une affirmation sur le monde, pas une précaution de langage.

### 0.5 — Doctrine d'escalade vers la source primaire

Ne pas télécharger les comptes complets systématiquement (coûteux), ne jamais s'en priver non plus. **Escalader sur déclencheur :**

| Déclencheur | Action |
|---|---|
| Un contrôle de cohérence échoue | **Escalade obligatoire** — on ne documente pas l'écart, on va chercher la donnée |
| Deux sources de niveau 2 divergent | **Escalade obligatoire** |
| Un chiffre est structurellement invraisemblable (§ contrôles, test de plausibilité) | **Escalade obligatoire** |
| Un input critique manque, ou n'existe qu'en agrégat | Escalade |
| Un poste n'existe que dans le détail : D&A, charges financières, immobilisations brutes/nettes, échéancier des dettes, taux d'IS effectif | Escalade |
| Tout est cohérent, recoupé et suffisant pour les calculs | **Rester au niveau 2** — c'est légitime |

**Dans un jeu de comptes complets, l'annexe vaut souvent plus que les tableaux chiffrés.** C'est elle qui révèle les malis de fusion, les conventions de trésorerie intragroupe (cash pooling), l'intégration fiscale, les engagements hors bilan et les transactions avec parties liées — autant d'éléments qui changent l'interprétation et qu'aucun tableau de synthèse ne montre.

### 0.6 — Exécuter le contrôle automatique

**Une instruction en prose peut être suivie ou rationalisée. Un script ne rationalise jamais.** Si l'environnement dispose de l'exécution de code (Bash/Python — vrai dans Claude Code, à vérifier ailleurs), le contrôle de cohérence (section dédiée plus bas) **n'est pas fait à la main : il est calculé par [`scripts/verifier_coherence.py`](scripts/verifier_coherence.py)**, sans dépendance externe.

**Étapes :**

1. À mesure que les données sont collectées (§ 0.1 à 0.4), les consigner dans un fichier `donnees-financieres.json`, un objet par exercice — voir [`scripts/donnees-financieres.exemple.json`](scripts/donnees-financieres.exemple.json) pour le format exact et la liste des champs reconnus. Chaque champ critique est un objet `{"valeur": ..., "statut": ..., "source": ...}`, pas juste un nombre nu.
2. Exécuter :
   ```bash
   python scripts/verifier_coherence.py donnees-financieres.json
   ```
3. **Coller la sortie du script telle quelle** dans la section « Contrôles de cohérence » de l'artefact final (voir gabarit plus bas) — pas une reformulation, pas un résumé sélectif.
4. Le script retourne un code de sortie non nul si un contrôle échoue **ou** si plus de la moitié des contrôles sont inexécutables faute de données. Dans les deux cas : ne pas rédiger les Étapes 6 à 8 avant d'avoir résolu la cause (escalade, § 0.5).

**Si l'exécution de code n'est pas disponible** (par exemple certains contextes Claude.ai) : appliquer les contrôles C1 à C6 et le test de plausibilité manuellement, avec la même discipline — un contrôle qui échoue s'escalade, il ne se documente pas. Le signaler explicitement dans l'artefact (« contrôles effectués manuellement, outil de calcul indisponible ») plutôt que de laisser croire que le script a tourné.

### 0.7 — Adapter la méthode à la taille et à la structure de l'entreprise

Les Étapes 0 à 8 ont été rodées sur des PME/ETI françaises à entité juridique unique (le cas le plus fréquent). Deux profils s'écartent nettement de ce cas par défaut et demandent une vigilance spécifique — les identités comptables (§ Contrôles de cohérence) restent valables partout, ce sont les **données d'entrée** et leur **lecture** qui changent.

**Grand groupe consolidé (ex. Renault, L'Oréal) :**

- **Comptes consolidés, pas comptes sociaux** (§ 0.1) — la source change de nature, pas seulement de taille.
- **Intérêts minoritaires.** Si une filiale n'est pas détenue à 100 %, les capitaux propres consolidés se décomposent en « part du groupe » + « intérêts minoritaires », alors que le bilan consolidé inclut 100 % des actifs de la filiale. Utiliser les capitaux propres **totaux** (part du groupe + minoritaires) dans C1 — sinon le contrôle échoue pour une raison purement comptable, pas parce qu'une donnée est fausse. Si l'écart de C1 réapparaît toujours après ce redressement, alors seulement le traiter comme un vrai signal d'erreur (§ Contrôles de cohérence).
- **Activité financière captive** (ex. Mobilize Financial Services chez Renault, filiales de financement chez les grands industriels) : une partie de la dette du groupe finance le crédit accordé aux clients, pas l'entreprise elle-même — ce n'est pas du levier au sens de l'Étape 4. Chercher si l'entreprise publie une décomposition sectorielle (« Automobile » / « Services financiers » ou équivalent) et appliquer gearing et dette/EBITDA à l'activité industrielle seule ; sinon, le signaler explicitement comme une limite plutôt que de publier un ratio consolidé trompeur.
- **Goodwill et intangibles issus d'acquisitions.** Un groupe qui a beaucoup acquis (marques, entreprises) porte un goodwill souvent non amorti (test de dépréciation, pas d'amortissement linéaire sous IFRS depuis 2004). Il gonfle l'actif économique sans générer de dotation comparable à un actif industriel : un ROIC plus bas ne signale pas forcément une entreprise moins efficace opérationnellement, seulement une base d'actifs différente. Le mentionner dans l'interprétation de l'Étape 3 plutôt que de laisser le chiffre parler seul.
- **Participations financières** (ex. une prise de participation minoritaire dans une autre société cotée) : à exclure de l'actif économique, même logique que la trésorerie exclue pour Thiga et OCTO — c'est un actif financier, pas un moyen d'exploitation.

**Entité sans comptes publics accessibles (micro-entreprise, TPE avec confidentialité des comptes) :**

- Une micro-entreprise (régime auto-entrepreneur) n'a pas de bilan au sens comptable — juste une déclaration de chiffre d'affaires. Le niveau 1 de la hiérarchie des sources n'existe pas, ce n'est pas une recherche insuffisante.
- Une SARL/EURL en dessous des seuils peut avoir déposé des comptes sous option de confidentialité — légalement déposés, non publiés. Vérifier explicitement cette option avant de conclure à une absence de données (elle est mentionnée sur la fiche Infogreffe/Pappers de l'entreprise).
- Dans les deux cas, **dégrader la méthode plutôt que de forcer les 8 étapes sur du vide** : rester sur ce qui est vérifiable (CA si communiqué, avis clients/marché, positionnement qualitatif), ne produire ni WACC, ni EVA, ni valorisation chiffrée sans base réelle, et le dire explicitement dans l'Executive Summary — « diagnostic partiel, comptes non accessibles publiquement » — plutôt que de combler par des proxys en cascade jusqu'à une recommandation qui n'a plus de socle.

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
- Vérifier si le FCF est positif et récurrent. Un FCF négatif de façon récurrente signale que l'entreprise investit plus qu'elle ne génère de cash, ce qui n'est soutenable que si ce déficit est financé et que la croissance future le justifie.
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
- Comparer ROIC vs WACC : c'est le test décisif de la création de valeur.
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

## Contrôles de cohérence

Les 8 étapes s'enchaînent en cascade : l'actif économique alimente le ROIC, la structure de financement alimente le WACC, les deux alimentent l'EVA puis la valorisation. **Un input faux ne se signale jamais tout seul** — il produit des résultats plausibles jusqu'au bout. Ces contrôles sont le seul mécanisme qui le détecte.

**Quand les exécuter** : après les Étapes 1 à 5 (dès que bilan et compte de résultat sont exploités), **avant** d'écrire les Étapes 6 à 8 et la restitution — c'est là que la cascade démarre.

**Comment les exécuter** : via [`scripts/verifier_coherence.py`](scripts/verifier_coherence.py) quand l'exécution de code est disponible (§ 0.6) — c'est le mode par défaut. Les tableaux ci-dessous décrivent ce que le script calcule ; ils servent aussi de référence pour une exécution manuelle en repli.

### Contrôles d'identité comptable

| # | Contrôle | Tolérance |
|---|---|---|
| C1 | **Actif économique** (BFR total + immobilisations nettes) **= Capitaux employés** (capitaux propres + provisions + dette financière nette) | écart < 5 % |
| C2 | **Capitaux propres + total des dettes + provisions = total du bilan** | à l'euro près |
| C3 | **EBITDA − dotations aux amortissements et provisions = EBIT** | à l'euro près |
| C4 | **ROE recalculé** (résultat net / capitaux propres) **= ROE publié** par la source | écart < 0,5 pt |
| C5 | Si dette financière = 0 : **gearing = 0 et charges d'intérêts ≈ 0** — sinon l'un des deux est faux | cohérence logique |
| C6 | **Taux d'IS effectif** (impôt / résultat courant avant impôts) **dans une fourchette plausible** (≈ 15 % à 35 % en France) | sinon investiguer (intégration fiscale, CIR, déficits reportables) |

### Tests de plausibilité structurelle

Vérifier que le profil de bilan correspond au modèle d'activité. Une violation n'est pas forcément une erreur, mais **exige une explication documentée** :

| Modèle | Attendu | Alerte si |
|---|---|---|
| **Services / conseil** | Stocks ≈ 0 · immobilisations corporelles faibles · masse salariale 50-75 % du CA · **dettes fiscales et sociales significatives** (plusieurs mois de charges) | Dettes sociales quasi nulles alors que la masse salariale est importante → **la ventilation du passif est fausse** |
| **Distribution** | BFR négatif · rotation d'actif élevée · marge faible | BFR fortement positif → modèle atypique à expliquer |
| **Industrie** | Immobilisations lourdes · stocks significatifs · intensité capitalistique élevée | Immobilisations faibles → activité sous-traitée ? |

**Test de bon sens à appliquer systématiquement** : reconstituer mentalement les postes manquants et vérifier qu'ils sont possibles. Exemple : si capitaux propres + dette financière ≈ total du bilan, alors toutes les autres dettes valent zéro — impossible pour une entreprise qui paie des salaires et de la TVA. Ce raisonnement seul suffit à détecter une ventilation de passif erronée. `verifier_coherence.py` l'implémente sous la forme du contrôle `PLAUS.` (masse salariale vs dettes fiscales et sociales).

### En cas d'échec d'un contrôle

**Un contrôle qui échoue est une donnée fausse, pas une curiosité à commenter.**

1. **Ne pas documenter l'écart et poursuivre.** C'est le réflexe naturel et c'est l'erreur : expliquer pourquoi deux chiffres divergent ne les rend pas justes.
2. **Escalader vers la source primaire** (§ 0.5) pour récupérer la donnée manquante ou corrigée.
3. Si, après escalade, la donnée reste introuvable : **le dire explicitement, marquer les indicateurs dérivés comme `estime`** (§ 0.4), et propager cette réserve jusqu'à l'Executive Summary. Ne jamais présenter comme établi un résultat dont un input est incertain.

Le script matérialise cette règle : il retourne un code de sortie non nul (`FAIL` sur un contrôle, ou trop de `N.A.`) précisément dans les cas où la suite ne doit pas être écrite sans escalade préalable.

### Restitution des contrôles

Faire figurer dans l'artefact une section **« Contrôles de cohérence »** avec, quand le script a tourné, **sa sortie brute collée telle quelle** (§ 0.6) ; à défaut, un tableau listant chaque contrôle avec son résultat (✓ / ✗ / non applicable) et les chiffres du rapprochement. Deux bénéfices : le lecteur vérifie que les contrôles ont réellement tourné, et il devient impossible de les contourner silencieusement.

## Structure de l'artefact de sortie

Produire un fichier markdown structuré ainsi :

```
# Analyse Financière — [Nom de l'entreprise]
## Date de l'analyse : [date]

## Fiabilité des données
[Tableau : donnée → statut (verifie-source / secondaire / estime / non-trouve) + source]
[Signaler ici toute donnée critique non vérifiée directement]

## Executive Summary
[3-5 bullets avec les conclusions clés : santé financière, création/destruction de valeur, valorisation, recommandation]
[Chaque conclusion reposant sur une donnée `estime` ou `secondaire` doit le mentionner]

## Contrôles de cohérence
[Sortie brute de scripts/verifier_coherence.py (§ 0.6) — ou, à défaut, C1 à C6 et le test de plausibilité calculés manuellement : ✓ / ✗ / n.a., avec les chiffres du rapprochement]

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
- **Vérifier les inputs critiques à la source** (§ 0.2). Un rapport de recherche délégué oriente vers la source, il ne la remplace pas.
- **Exécuter `scripts/verifier_coherence.py`** (§ 0.6) dès que l'exécution de code est disponible, plutôt que de calculer les contrôles de tête. C'est un calcul, pas une vérification qu'on délègue à sa propre estimation.
- **Ne jamais contourner un contrôle de cohérence en l'expliquant.** Si deux chiffres qui devraient converger divergent, la donnée est fausse — il faut aller la chercher, pas rédiger une note de bas de page.
- **Propager l'incertitude** jusqu'à l'Executive Summary (§ 0.4). Un résultat calculé sur un input `estime` reste `estime`, quel que soit le soin du calcul.
- **Toujours interpréter les chiffres**, pas juste les afficher. Chaque ratio doit être accompagné d'un commentaire sur ce qu'il signifie pour l'entreprise.
- **Comparer systématiquement** aux pairs du secteur quand les données sont disponibles.
- **PER et PBR obligatoires** pour toute entreprise cotée.
- **Privilégier web search** plutôt que firecrawl pour économiser les tokens ; escalader vers les comptes déposés complets sur déclencheur (§ 0.5).
- **Chercher en français** pour les entreprises françaises/européennes.
- **Ne constitue pas un conseil en investissement.** La recommandation BUY/HOLD/SELL produite par ce skill est une conclusion méthodologique fondée sur des données publiques et des hypothèses explicites (WACC, taux de croissance, comparables) — pas un conseil personnalisé. Le rappeler dans la synthèse et inviter à consulter un professionnel avant toute décision d'investissement réelle.

## Ressources

- [`references/formules.md`](references/formules.md) — formules détaillées, seuils d'interprétation, benchmarks sectoriels et glossaire pour chacune des 8 étapes
- [`scripts/verifier_coherence.py`](scripts/verifier_coherence.py) — contrôle automatique des identités C1-C6 et du test de plausibilité (§ 0.6), sans dépendance externe
- [`scripts/donnees-financieres.exemple.json`](scripts/donnees-financieres.exemple.json) — format attendu du fichier de données, illustré avec un jeu de données réel (OCTO Technology, comptes sociaux 2024-2025)
- [`examples/`](examples/) — exemple complet commenté avec une entreprise fictive
