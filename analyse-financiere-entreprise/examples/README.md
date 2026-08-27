# Exemples

| Fichier | Cas illustré |
|---------|--------------|
| [`exemple-aurea-industries.md`](exemple-aurea-industries.md) | Diagnostic complet en 8 étapes, entreprise fictive « Auréa Industries » — cas nuancé (HOLD, valorisation quasi alignée sur le cours) plutôt qu'un BUY ou SELL évident |

## Avertissement

Toutes les données de cet exemple sont **fictives** : compte de résultat, bilan, cours de bourse et recommandation sont inventés pour que les calculs s'enchaînent de façon cohérente d'une étape à l'autre. Ils servent uniquement à illustrer le format de sortie attendu (voir « Structure de l'artefact de sortie » dans [`SKILL.md`](../SKILL.md)) et la logique des formules.

Dans une exécution réelle, chaque chiffre est recherché et sourcé (rapport annuel officiel, Boursorama, Zonebourse, Morningstar…) — jamais inventé.

## Vérifier la cohérence d'un exemple

Les ratios d'un diagnostic se recoupent entre eux (le ROIC de l'Étape 3 doit redonner l'EVA de l'Étape 7, le WACC de l'Étape 6 doit être cohérent avec le DCF de l'Étape 8…). Avant de publier un nouvel exemple, refaire les calculs à la main ou via un tableur pour vérifier qu'aucun chiffre n'est incohérent avec un autre.
