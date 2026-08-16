# Référence des calculs

Détail des formules utilisées par le skill `analyse-locative`, de leurs hypothèses et de leurs limites.
**Périmètre : France.** Les taux, taxes et conventions décrits ici sont propres au droit français.

---

## 1. Frais de notaire

Les « frais de notaire » ne sont pas des honoraires : la rémunération du notaire (les *émoluments*) représente moins d'un cinquième du total. Le reste est constitué de taxes reversées à l'État et aux collectivités.

### Composition

| Poste | Ancien | Neuf (VEFA / 1ʳᵉ vente, soumis à TVA) |
|-------|--------|----------------------------------------|
| Droits de mutation (DMTO) | ~5,80 % à 6,31 % du prix, selon le département | — |
| Taxe de publicité foncière | — | 0,715 % |
| Émoluments du notaire | barème dégressif, ~0,8 % à 1 % sur les montants courants | idem |
| Débours (pièces, cadastre, géomètre) | quelques centaines d'euros | idem |
| Contribution de sécurité immobilière | 0,10 % | 0,10 % |
| **Total pratique** | **7 % à 8,5 %** — défaut du skill : **8 %** | **2 % à 3 %** — défaut du skill : **2,5 %** |

### Formule

```
Frais de notaire = Prix d'achat × taux_frais_notaire
```

### Points de vigilance

- **Majoration départementale des DMTO** : depuis 2025, les départements peuvent relever leur taux d'un demi-point. Une large partie du territoire est concernée, ce qui pousse l'ancien vers le haut de la fourchette. Vérifier le taux du département cible quand le montant en jeu le justifie.
- **Primo-accédants** : certains départements exonèrent de la majoration. Sans objet pour un investissement locatif classique, mais à connaître.
- **Neuf** : la TVA à 20 % est déjà incluse dans le prix affiché. C'est ce qui explique des frais de notaire réduits — et non un avantage net, puisque la TVA a été payée en amont.
- Les **frais d'agence** ne sont pas modélisés. Si l'annonce affiche un prix FAI (frais d'agence inclus), les DMTO se calculent en principe sur le prix hors frais d'agence quand ceux-ci sont à la charge de l'acquéreur et mentionnés séparément. Le skill applique le taux au prix affiché : c'est une approximation légèrement conservatrice.

---

## 2. Coût total et emprunt

```
Coût total       = Prix d'achat + Frais de notaire
Emprunt          = Coût total − Apport
```

Si l'apport n'est pas fourni, le skill retient **10 % du coût total**, ce qui correspond à un dossier bancaire standard. Un apport de 0 € (financement dit « à 110 % ») est un cas légitime mais fait mécaniquement chuter le cashflow.

Ce qui **n'est pas** intégré au coût total :

- frais de dossier bancaire (généralement 500 à 1 500 €)
- frais de garantie : caution type Crédit Logement ou hypothèque, ~1 % à 1,5 % du montant emprunté
- travaux de remise en état ou de mise aux normes
- ameublement (déterminant si l'objectif est la location meublée / LMNP)

Sur un petit bien, ces postes représentent facilement 3 000 à 8 000 €. **Les ajouter mentalement avant toute décision.**

---

## 3. Mensualité de crédit (PMT)

Mensualité constante d'un prêt amortissable à taux fixe :

```
              i × (1 + i)^n
PMT = C × ───────────────────
             (1 + i)^n − 1

C = capital emprunté
i = taux nominal annuel ÷ 12
n = nombre de mensualités (20 ans = 240, 25 ans = 300)
```

### Facteurs par tranche de 1 000 € empruntés

Multiplier par `Emprunt ÷ 1000` pour obtenir la mensualité.

| Taux nominal | 20 ans (240 mois) | 25 ans (300 mois) |
|--------------|-------------------|-------------------|
| 3,00 % | 5,55 € | 4,74 € |
| 3,40 % | 5,75 € | 4,95 € |
| 3,50 % | 5,80 € | 5,01 € |
| 4,00 % | 6,06 € | 5,28 € |
| 4,50 % | 6,33 € | 5,56 € |

*Exemple : 37 120 € à 3,5 % sur 25 ans → 37,120 × 5,01 ≈ 186 €/mois.*

### Ce que la mensualité n'inclut pas

**L'assurance emprunteur (ADI) est exclue.** Elle coûte typiquement 0,10 % à 0,40 % du capital emprunté par an selon l'âge et l'état de santé, soit **10 à 35 €/mois pour 100 000 € empruntés**. Le cashflow calculé par le skill est donc **optimiste de ce montant**. C'est le principal écart entre les chiffres du tableau et une simulation bancaire réelle.

Le taux nominal utilisé n'est pas non plus le TAEG, qui intègre assurance, frais de dossier et garantie.

---

## 4. Charges d'exploitation mensuelles

| Poste | Ordre de grandeur | Remarques |
|-------|-------------------|-----------|
| Charges de copropriété non récupérables | 40 – 70 €/mois | Seule la part non récupérable pèse sur le propriétaire. Ascenseur et chauffage collectif font grimper le total. |
| Taxe foncière | 25 – 55 €/mois | Très variable d'une commune à l'autre — écart de 1 à 3 sur des villes voisines. À rechercher localement. |
| Assurance PNO | 12 – 18 €/mois | Propriétaire non occupant ; obligatoire en copropriété. |
| Vacance locative | Loyer ÷ 12 | Provision d'un mois par an. |

### Vacance locative

```
Vacance mensuelle = Loyer HC ÷ 12
```

Un mois par an est une hypothèse **moyenne** : prudente sur un marché tendu, optimiste sur un marché détendu ou pour un bien atypique. Sur une ville où la demande locative est faible, retenir 1,5 à 2 mois par an (`Loyer × 1,5 ÷ 12` ou `Loyer ÷ 6`).

### Postes volontairement exclus

- frais de gestion locative en agence : 6 % à 9 % des loyers encaissés
- assurance loyers impayés (GLI) : 2 % à 4 % des loyers
- travaux d'entretien courant et provision pour gros travaux : une règle usuelle est 5 % du loyer annuel
- CFE en location meublée
- imposition des revenus fonciers

---

## 5. Rendement brut

```
Rendement brut (%) = (Loyer HC × 12) ÷ Prix d'achat × 100
```

Indicateur de comparaison rapide entre biens. Il ignore toutes les charges et tous les frais d'acquisition : **il surévalue systématiquement la performance réelle**, souvent de 3 à 5 points.

---

## 6. Rendement net (de charges, avant impôt)

```
                    (Loyer − Charges copro − Taxe foncière − PNO − Vacance) × 12
Rendement net (%) = ────────────────────────────────────────────────────────────── × 100
                                        Coût total
```

### Deux conventions à connaître

**Les dénominateurs diffèrent.** Le rendement brut est calculé sur le **prix d'achat seul**, le rendement net sur le **coût total** (frais de notaire inclus). C'est la convention la plus répandue dans l'immobilier locatif français, mais elle a deux conséquences :

1. L'écart brut / net mélange deux effets — les charges *et* les frais d'acquisition. Il ne mesure pas le seul poids des charges.
2. Un rendement brut du skill n'est pas comparable à un rendement brut calculé sur coût total par un autre outil. **Toujours vérifier le dénominateur avant de comparer deux sources.**

**« Net » signifie ici net de charges, pas net d'impôt.** Le rendement net-net, qui intègre la fiscalité, est nettement inférieur. Selon le régime :

| Régime | Effet approximatif |
|--------|--------------------|
| Micro-foncier | Abattement de 30 % sur les loyers, puis TMI + 17,2 % de prélèvements sociaux |
| Réel foncier | Déduction des charges réelles et des **intérêts d'emprunt** — souvent plus favorable au démarrage |
| LMNP au réel | Amortissement du bien : la base imposable peut être proche de zéro pendant plusieurs années |

Le skill ne modélise aucun régime fiscal : le choix dépend de la situation personnelle de l'investisseur et relève d'un conseil professionnel.

---

## 7. Cashflow mensuel

```
Cashflow = Loyer HC − Charges copro − Taxe foncière − PNO − Vacance − Mensualité
```

C'est l'indicateur le plus concret : ce que l'opération coûte ou rapporte chaque mois, une fois le crédit payé.

- **Cashflow positif** : l'opération s'autofinance.
- **Cashflow négatif** : un effort d'épargne mensuel est nécessaire. Ce n'est pas disqualifiant en soi — c'est un arbitrage entre effort de trésorerie et constitution de patrimoine — mais il doit être assumé en connaissance de cause.

Le skill calcule le cashflow sur la durée la plus longue (25 ans), la plus favorable. Sur 20 ans, la mensualité est supérieure d'environ 16 % et le cashflow se dégrade d'autant.

Rappel : ajouter l'assurance emprunteur (§3) et, le cas échéant, les frais de gestion (§4) pour obtenir un cashflow réaliste.

---

## 8. Contexte marché local (INSEE)

Quatre indicateurs situent une ville avant d'en juger les biens. Ils sont collectés **une fois par ville**, pas par bien.

| Indicateur | Ce qu'il mesure | Lecture pour un investisseur |
|------------|------------------|-------------------------------|
| Évolution démographique | Variation annuelle moyenne de la population (recensement) | Croissance → demande locative portée par le flux de population ; déclin → risque de vacance structurelle qui ne se résorbe pas avec un loyer plus bas |
| Revenu médian mensuel du ménage | Revenu disponible médian (FiLoSoFi) | Sert de base au taux d'effort locatif ci-dessous |
| Part de locataires dans le parc de logements | Recensement, thème Logement | Un parc à forte dominante locative signale une demande structurelle, indépendamment des annonces du moment |
| Indice des prix immobiliers | Évolution 1 an / 5 ans (Notaires-INSEE) | Situe le prix des biens sélectionnés : sous la tendance (bonne affaire ou anomalie à vérifier) ou au-dessus |

### Taux d'effort locatif

```
Taux d'effort (%) = Loyer HC mensuel ÷ Revenu médian mensuel du ménage × 100
```

Ce n'est pas le taux d'effort du locataire réel du bien (données individuelles non disponibles), mais un indicateur de **soutenabilité locale** : le loyer visé est-il compatible avec le pouvoir d'achat médian de la commune ?

| Taux d'effort | Lecture |
|----------------|---------|
| < 25 % | Marge de revalorisation du loyer probable |
| 25 % – 33 % | Loyer aligné sur le marché local, marge de manœuvre limitée |
| > 33 % | Seuil usuel d'alerte — loyer difficilement soutenable pour le ménage médian ; à nuancer si le parc locatif cible une population à revenus différents (étudiants, jeunes actifs) |

### Pourquoi ce n'est pas une colonne du TSV

Les quatre indicateurs et le taux d'effort agrégé sont des données **de ville**, identiques sur toutes les lignes d'une même recherche. Les intégrer comme colonnes supplémentaires du tableau créerait une redondance sur chaque ligne et casserait la compatibilité avec les modèles d'import déjà utilisés. Ils sont affichés une fois, dans un bloc "Contexte marché" séparé, et réutilisés dans l'analyse et les verdicts (voir SKILL.md, Étape 6).

---

## 9. Verdicts et recommandation

Le skill classe chaque bien selon des règles fixes, pour que la recommandation finale soit reproductible plutôt que basée sur une impression :

| Verdict | Condition |
|---------|-----------|
| 🟢 Prioritaire | Cashflow 25 ans ≥ 0 € **ET** fiabilité loyer ∈ {`Loyer en place`, `Annonce réelle`} **ET** pas de DPE F/G non budgété |
| 🟡 À creuser | Cashflow 25 ans entre −150 € et 0 € **OU** fiabilité = `Estimation marché` avec rendement net ≥ 5 % **OU** DPE F sans budget travaux mentionné |
| 🔴 À écarter | Cashflow 25 ans < −150 €/mois **OU** DPE G sans budget travaux ni échéance de mise en conformité **OU** prix anormalement bas sans explication |

Le seuil de −150 €/mois n'est pas arbitraire au sens strict, mais reste un repère : il correspond à peu près à un mois de loyer d'écart sur l'année pour un T2 de province. Il peut être resserré ou élargi si l'utilisateur indique explicitement sa capacité d'épargne mensuelle disponible pour l'opération — auquel cas utiliser ce montant plutôt que le repère par défaut, et le signaler.

La recommandation de synthèse croise ces verdicts avec le contexte INSEE (§8) : un bien 🟢 dans une ville en déclin démographique mérite une réserve ; un bien 🟡 dans une ville en forte tension locative (taux d'effort bas, forte part de locataires, croissance démographique) mérite d'être mentionné comme à surveiller plutôt qu'à écarter d'emblée.

---

## 10. Exemple chiffré pas à pas

**Hypothèses** : T2 ancien de 39 m² à Saint-Étienne, prix 39 000 €, apport 5 000 €, taux 3,5 %, notaire 8 %.

| Étape | Calcul | Résultat |
|-------|--------|----------|
| Frais de notaire | 39 000 × 8 % | 3 120 € |
| Coût total | 39 000 + 3 120 | 42 120 € |
| Emprunt | 42 120 − 5 000 | 37 120 € |
| Mensualité 20 ans | 37,120 × 5,80 | 215 € |
| Mensualité 25 ans | 37,120 × 5,01 | 186 € |
| Loyer HC retenu | annonce de location comparable | 420 € |
| Vacance | 420 ÷ 12 | 35 € |
| Charges retenues | copro 45 + TF 35 + PNO 12 | 92 € |
| Rendement brut | (420 × 12) ÷ 39 000 × 100 | **12,9 %** |
| Revenu net mensuel | 420 − 45 − 35 − 12 − 35 | 293 € |
| Rendement net | (293 × 12) ÷ 42 120 × 100 | **8,3 %** |
| Cashflow 25 ans | 293 − 186 | **+107 €** |
| Taux d'effort local | 420 ÷ 1 650 (revenu médian ménage Saint-Étienne, exemple) × 100 | **25,5 %** |
| Verdict | Cashflow ≥ 0, loyer en `Annonce réelle`, pas de DPE bloquant | **🟢 Prioritaire** |

**Lecture réaliste** : en retranchant une assurance emprunteur d'environ 12 €/mois et une provision travaux de 5 % du loyer (21 €/mois), le cashflow retombe autour de **+74 €**. En passant par une agence de gestion (7 % des loyers, ~29 €), il descend vers **+45 €**. L'opération reste autofinancée, mais la marge réelle est deux fois plus faible que le chiffre brut du tableau. Le taux d'effort de 25,5 % indique par ailleurs que le loyer retenu est cohérent avec le pouvoir d'achat local, sans marge de revalorisation évidente à court terme.

---

## 11. Sources à privilégier

| Donnée | Sources |
|--------|---------|
| Biens à vendre | LeBonCoin, SeLoger, PAP, Bien'ici, Logic-Immo, agences locales |
| Loyers de marché | Annonces de location en cours, observatoires locaux des loyers (OLL), SeLoger, LocService, MeilleursAgents |
| Prix au m² | MeilleursAgents, base DVF (transactions réelles publiées par la DGFiP) |
| Taux de crédit | Baromètres des courtiers (Meilleurtaux, Empruntis, Cafpi) — vérifier la date de publication |
| Taxe foncière | Site de la commune, forums locaux, annonces mentionnant le montant |
| DMTO départementaux | Service-public.fr, site du conseil départemental |
| Encadrement des loyers | Site de la préfecture ou de l'agglomération concernée |
| Démographie, revenu médian, part de locataires | INSEE — Dossier complet de la commune (insee.fr), recensement de la population, FiLoSoFi |
| Indice des prix immobiliers | Indices Notaires-INSEE |

La base **DVF** (Demandes de Valeurs Foncières) est la source la plus fiable pour les prix : ce sont des transactions réellement conclues, pas des prix affichés. Le **Dossier complet INSEE** d'une commune regroupe démographie, revenus et logement dans une seule fiche — c'est le point d'entrée le plus rapide pour l'Étape 2 du SKILL.md.

---

## 12. Limites générales

Ce skill produit une **première sélection chiffrée**, pas une étude d'investissement. Avant tout engagement :

- visiter le bien et faire chiffrer les travaux
- lire les procès-verbaux d'assemblée générale de copropriété des trois dernières années
- vérifier le montant réel des charges et de la taxe foncière auprès du vendeur ou du syndic
- consulter le DPE et son impact sur le droit de louer (voir SKILL.md)
- faire simuler le financement réel, assurance comprise, par une banque ou un courtier
- valider le régime fiscal avec un professionnel

Le contexte INSEE (§8) est une donnée **de commune**, pas de quartier : dans une grande ville, la moyenne communale peut masquer de fortes disparités entre arrondissements ou quartiers. À affiner avec des données à l'échelle IRIS quand elles sont disponibles et que l'enjeu le justifie.

Les indicateurs, verdicts et recommandations produits sont **indicatifs**. Ils ne constituent ni un conseil en investissement, ni une recommandation d'achat.
