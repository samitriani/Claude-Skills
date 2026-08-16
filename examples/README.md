# Exemples

Sessions complètes montrant l'entrée, les paramètres résolus, le contexte marché INSEE, le bloc TSV produit, les verdicts par bien et la recommandation de synthèse.

| Fichier | Cas illustré |
|---------|--------------|
| [`t2-ancien-saint-etienne.md`](t2-ancien-saint-etienne.md) | T2 ancien, petit budget, apport fixe — les trois niveaux de fiabilité du loyer, deux verdicts 🟢, deux verdicts 🟡 |
| [`t3-neuf-angers.md`](t3-neuf-angers.md) | T3 neuf — frais de notaire à 2,5 %, exonération de taxe foncière, taux d'effort local tendu, **aucun bien ne passe 🟢** |

## Fichiers TSV

| Fichier | Usage |
|---------|-------|
| [`en-tetes.tsv`](en-tetes.tsv) | Ligne d'en-tête des 19 colonnes, à coller une fois en haut du tableau |
| [`sortie-t2-ancien.tsv`](sortie-t2-ancien.tsv) | Sortie brute de l'exemple 1 |
| [`sortie-t3-neuf.tsv`](sortie-t3-neuf.tsv) | Sortie brute de l'exemple 2 |

## Avertissement

Toutes les données de ces exemples sont **fictives**. Les URLs utilisent le domaine réservé `.invalid` (RFC 2606) et ne pointent vers aucune annonce. Les prix, loyers et charges sont plausibles mais inventés — ils servent uniquement à illustrer le format de sortie et la cohérence des calculs.

## Vérifier le format d'une sortie

Chaque ligne doit contenir exactement 19 champs séparés par des tabulations :

```bash
awk -F'\t' '{print NR": "NF" champs"}' sortie-t2-ancien.tsv
```
