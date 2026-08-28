# Exemples

Deux diagnostics complets en 8 étapes, sur des entreprises réelles, pour illustrer le format de sortie attendu (voir « Structure de l'artefact de sortie » dans [`SKILL.md`](../SKILL.md)) sur deux profils différents.

Ces fichiers sont aussi embarqués dans [`analyse-financiere-entreprise.zip`](../analyse-financiere-entreprise.zip), le package uploadé dans Claude.ai — toute modification ici doit être suivie d'une régénération du zip (automatique via le hook `pre-commit`, voir [Régénérer le zip](../README.md#régénérer-le-zip)).

| Fichier | Cas illustré |
|---------|--------------|
| [`Analyse-Financiere-OCTO-Technology.md`](Analyse-Financiere-OCTO-Technology.md) | Société non cotée (filiale à 100 % d'Accenture) — pas de PER/PBR/DCF actionnarial, méthodologie adaptée en conséquence, valorisation limitée aux multiples |
| [`Analyse-Financiere-Sopra-Steria.md`](Analyse-Financiere-Sopra-Steria.md) | Grand groupe coté (Euronext Paris) — comptes consolidés, WACC via MEDAF, PER/PBR, recommandation argumentée |

## Avertissement

Contrairement aux exemples avec données fictives d'autres skills de ce dépôt, ces deux analyses portent sur des **entreprises réelles**, à partir de données publiques (comptes déposés, communiqués officiels, cotations de marché). Elles restent des illustrations du format de sortie — elles ne constituent pas un conseil en investissement (voir « Ce que l'analyse n'est pas » dans le [`README.md`](../README.md) du skill).
