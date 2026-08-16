# Exemple 1 — T2 dans l'ancien, budget serré

> **Données fictives.** Les biens, loyers et URLs de cet exemple sont inventés pour illustrer le format de sortie. Les URLs utilisent le domaine réservé `.invalid` et ne pointent nulle part. Une exécution réelle produit des annonces existantes avec leurs liens vérifiables.

## Demande

```
Analyse locative Saint-Étienne 80000 pour un apport de 5000
```

## Paramètres résolus

| Paramètre | Valeur | Origine |
|-----------|--------|---------|
| `ville` | Saint-Étienne | demande |
| `type_bien` | T2 | défaut |
| `budget_max` | 80 000 € | demande |
| `apport` | 5 000 € | demande |
| `etat_bien` | ancien | défaut |
| `taux_frais_notaire` | 8 % | défaut ancien |
| `taux_credit` | 3,5 % | baromètre courtier, à vérifier |

## Contexte marché — Saint-Étienne (INSEE)

```
Contexte marché — Saint-Étienne (INSEE)
- Population : 171 000 hab. (quasi stable, -0,1 %/an sur 2016-2022, recensement INSEE)
- Revenu médian mensuel du ménage : 1 650 € (FiLoSoFi 2022)
- Part de locataires dans le parc de logements : 54 %
- Indice des prix immobiliers : +2,1 % sur 1 an, +6,4 % sur 5 ans (Notaires-INSEE)
- Taux d'effort locatif type : 26,9 % (loyer moyen des 4 biens ≈ 444 € ÷ revenu médian)
```

Lecture : ville démographiquement stable, avec un parc majoritairement locatif (54 %) — signal favorable à la relocation. Le taux d'effort de 26,9 % reste sous le seuil d'alerte de 33 %, ce qui laisse une marge de manœuvre raisonnable sur les loyers retenus.

## Tableau de synthèse (Étape 5.1 — lecture immédiate)

Trié par verdict puis rendement net décroissant :

| Bien | Surface | Prix | Loyer HC | Fiabilité | Rendement net | Cashflow 25 ans | Verdict |
|------|---------|------|----------|-----------|-----------------|--------------------|---------|
| T2 Châteaucreux 39 m² | 39 m² | 39 000 € | 420 € | Réelle | 8,3 % | +107 € | 🟢 |
| T2 Carnot 36 m² | 36 m² | 45 000 € | 445 € | Réelle | 7,8 % | +96 € | 🟢 |
| T2 Fauriel 42 m² | 42 m² | 52 000 € | 480 € | Estimé | 7,1 % | +74 € | 🟡 |
| T2 Bellevue 45 m² loué | 45 m² | 74 000 € | 430 € | En place | 4,0 % | −111 € | 🟡 |

## Sortie — bloc à coller (Étape 5.2 — 19 colonnes, avec en-tête)

```
Ville	Adresse / Description	Surface (m²)	Prix achat (€)	Frais notaire (€)	Coût total (€)	Emprunt nécessaire (€)	Mensualité 20 ans (€)	Mensualité 25 ans (€)	Loyer HC (€)	Fiabilité loyer	Charges copro /mois (€)	Taxe foncière /mois (€)	Assurance PNO /mois (€)	Vacance loc. /mois (€)	Rendement brut (%)	Rendement net (%)	Cashflow /mois 25 ans (€)	Lien annonce
Saint-Étienne	T2 Châteaucreux 39 m²	39	39000	3120	42120	37120	215	186	420	Annonce réelle	45	35	12	35	12.9	8.3	107	https://exemple.invalid/annonce/se-001
Saint-Étienne	T2 Fauriel 42 m²	42	52000	4160	56160	51160	297	256	480	Estimation marché	55	40	15	40	11.1	7.1	74	https://exemple.invalid/annonce/se-002
Saint-Étienne	T2 Bellevue 45 m² loué	45	74000	5920	79920	74920	435	375	430	Loyer en place	70	45	15	36	7.0	4.0	-111	https://exemple.invalid/annonce/se-003
Saint-Étienne	T2 Carnot 36 m²	36	45000	3600	48600	43600	253	218	445	Annonce réelle	50	32	12	37	11.9	7.8	96	https://exemple.invalid/annonce/se-004
```

Version fichier : [`sortie-t2-ancien.tsv`](sortie-t2-ancien.tsv)

## Fichier Excel (Étape 5.3 — si l'outil est disponible)

Dans cette session, l'outil de génération de fichiers est disponible : `analyse-locative-saint-etienne-2026-08-16.xlsx` est généré et joint à la réponse en complément, avec deux feuilles — « Biens » (19 colonnes + Verdict en couleur, en-tête figé) et « Contexte marché » (bloc INSEE ci-dessus). Ce fichier ne remplace pas les deux livrables précédents.

## Restitution attendue

```
Paramètres de calcul :
- Type de bien : T2
- Budget max : 80 000 €
- Apport : 5 000 € (fixe)
- État : ancien → frais de notaire 8 %
- Taux crédit : 3,5 % (baromètre courtier)
- Vacance locative : 1 mois/an
```

**Fiabilité des loyers**

| Bien | Fiabilité | Base |
|------|-----------|------|
| Châteaucreux | `Annonce réelle` | T2 38 m² loué 415 €, même rue |
| Fauriel | `Estimation marché` | 11,4 €/m² × 42 m² — **à confirmer** |
| Bellevue | `Loyer en place` | bail en cours mentionné dans l'annonce |
| Carnot | `Annonce réelle` | T2 37 m² loué 450 €, quartier voisin |

**Verdicts**

| Bien | Rendement net | Cashflow 25 ans | Fiabilité loyer | Verdict | Justification |
|------|----------------|-------------------|-------------------|---------|----------------|
| Châteaucreux | 8,3 % | +107 € | Annonce réelle | 🟢 Prioritaire | Cashflow positif, loyer adossé à un comparable réel, aucun DPE bloquant mentionné |
| Carnot | 7,8 % | +96 € | Annonce réelle | 🟢 Prioritaire | Mêmes conditions que Châteaucreux, surface plus petite donc plus liquide à la relocation |
| Fauriel | 7,1 % | +74 € | Estimation marché | 🟡 À creuser | Cashflow positif mais loyer non confirmé par une annonce réelle — rendement net ≥ 5 %, donc pas écarté, mais à vérifier avant visite |
| Bellevue | 4,0 % | −111 € | Loyer en place | 🟡 À creuser | Cashflow négatif mais dans la fourchette −150 à 0 € ; le loyer en place est fiable mais bas pour la surface |

**Recommandation de synthèse**

Châteaucreux et Carnot sont les deux biens à visiter en priorité : ils cumulent un cashflow positif, un loyer adossé à une annonce de location réelle et pas de signal réglementaire bloquant — dans une ville dont le contexte INSEE (parc à 54 % locatif, taux d'effort à 26,9 %, démographie stable) ne remet pas en cause ces chiffres. Fauriel mérite d'être approfondi avant d'être écarté ou retenu : son rendement de 7,1 % ne tient qu'à une estimation de loyer au m², à confirmer par une annonce de location comparable avant toute visite. Bellevue n'est pas à écarter définitivement mais à traiter à part : le cashflow négatif de −111 €/mois vient d'un loyer en place visiblement sous le marché (430 € pour 45 m², contre ~445 € pour 36 m² à Carnot) — une renégociation ou une relocation au départ du locataire actuel changerait le calcul, mais ce n'est pas actionnable immédiatement.

**Réserves**

- Le loyer de Fauriel doit être confirmé par des annonces de location réelles avant toute visite.
- Les taxes foncières sont des ordres de grandeur : demander l'avis d'imposition au vendeur.
- Aucun DPE n'est mentionné dans deux des annonces. Un classement F ou G change complètement l'analyse (voir la section réglementaire du SKILL.md).
- Les cashflows n'intègrent pas l'assurance emprunteur (~10 à 12 €/mois ici) ni les frais de gestion.
