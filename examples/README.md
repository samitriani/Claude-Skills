# Exemples

Sessions complètes montrant l'entrée, les paramètres résolus, le contexte marché INSEE, le tableau de synthèse lisible, le bloc TSV avec en-tête, le fichier Excel (disponible ou non selon l'environnement), les verdicts détaillés et la recommandation de synthèse.

Ces fichiers sont aussi embarqués dans [`analyse-locative.zip`](../analyse-locative.zip), le package uploadé dans Claude.ai — toute modification ici doit être suivie d'une régénération du zip (automatique via le hook `pre-commit`, voir [Régénérer le zip](../README.md#régénérer-le-zip)).

| Fichier | Cas illustré |
|---------|--------------|
| [`t2-ancien-saint-etienne.md`](t2-ancien-saint-etienne.md) | T2 ancien, petit budget, apport fixe — trois niveaux de fiabilité du loyer, deux verdicts 🟢, deux verdicts 🟡, fichier Excel **disponible** |
| [`t3-neuf-angers.md`](t3-neuf-angers.md) | T3 neuf — frais de notaire à 2,5 %, taux d'effort local tendu, **aucun bien ne passe 🟢**, fichier Excel **non disponible** (repli sur les livrables texte, sans le signaler comme un manque) |

## Fichiers TSV

Depuis l'introduction du tableau de synthèse (Étape 5.1 du skill), le bloc TSV inclut une **ligne d'en-tête** — ce n'était pas le cas dans les toutes premières versions du skill.

| Fichier | Usage |
|---------|-------|
| [`en-tetes.tsv`](en-tetes.tsv) | Ligne d'en-tête seule, pour qui veut la coller séparément (ex. préparer un onglet avant de recevoir les données) |
| [`sortie-t2-ancien.tsv`](sortie-t2-ancien.tsv) | Sortie brute de l'exemple 1, en-tête incluse |
| [`sortie-t3-neuf.tsv`](sortie-t3-neuf.tsv) | Sortie brute de l'exemple 2, en-tête incluse |

## Avertissement

Toutes les données de ces exemples sont **fictives**. Les URLs utilisent le domaine réservé `.invalid` (RFC 2606) et ne pointent vers aucune annonce. Les prix, loyers et charges sont plausibles mais inventés — ils servent uniquement à illustrer le format de sortie et la cohérence des calculs.

## Vérifier le format d'une sortie

Chaque ligne doit contenir exactement 19 champs séparés par des tabulations :

```bash
awk -F'\t' '{print NR": "NF" champs"}' sortie-t2-ancien.tsv
```
