# Exemple 2 — T3 dans le neuf, frais de notaire réduits

> **Données fictives.** Voir l'avertissement de l'[exemple 1](t2-ancien-saint-etienne.md).

Cet exemple montre l'effet des trois paramètres ajoutés : `type_bien`, `etat_bien` (qui bascule les frais de notaire de 8 % à 2,5 %) et un couple budget / apport différent.

## Demande

```
Analyse locative Angers T3 neuf 200000 apport 20000
```

## Paramètres résolus

| Paramètre | Valeur | Origine |
|-----------|--------|---------|
| `ville` | Angers | demande |
| `type_bien` | T3 | demande |
| `budget_max` | 200 000 € | demande |
| `apport` | 20 000 € | demande |
| `etat_bien` | **neuf** | demande |
| `taux_frais_notaire` | **2,5 %** | déduit de `etat_bien = neuf` |
| `taux_credit` | 3,4 % | baromètre courtier, à vérifier |

## Contexte marché — Angers (INSEE)

```
Contexte marché — Angers (INSEE)
- Population : 158 000 hab. (croissance, +0,6 %/an sur 2016-2022, recensement INSEE)
- Revenu médian mensuel du ménage : 1 780 € (FiLoSoFi 2022)
- Part de locataires dans le parc de logements : 58 %
- Indice des prix immobiliers : +1,4 % sur 1 an, +11,8 % sur 5 ans (Notaires-INSEE)
- Taux d'effort locatif type : 38,2 % (loyer moyen des 3 biens ≈ 693 € ÷ revenu médian)
```

Lecture : ville en croissance démographique, parc majoritairement locatif — le contexte est structurellement favorable à la demande locative. Mais le taux d'effort de 38,2 % dépasse le seuil d'alerte de 33 % : les loyers du neuf, pour cette gamme de biens, sont déjà tendus par rapport au revenu médian local. La marge de revalorisation des loyers y est donc faible, ce qui pèse directement sur les rendements ci-dessous.

## Sortie — bloc à coller (19 colonnes)

```
Angers	T3 neuf Saint-Serge 62 m²	62	186000	4650	190650	170650	981	845	720	Estimation marché	85	55	18	60	4.6	3.2	-343	https://exemple.invalid/annonce/an-001
Angers	T3 neuf Belle-Beille 58 m²	58	172000	4300	176300	156300	898	774	690	Annonce réelle	78	50	17	58	4.8	3.3	-287	https://exemple.invalid/annonce/an-002
Angers	T3 neuf Monplaisir 60 m²	60	159000	3975	162975	142975	822	708	670	Annonce réelle	72	0	17	56	5.1	3.9	-183	https://exemple.invalid/annonce/an-003
```

Version fichier : [`sortie-t3-neuf.tsv`](sortie-t3-neuf.tsv)

## Points d'attention propres au neuf

**Frais de notaire.** Sur Saint-Serge, 2,5 % donnent 4 650 € au lieu de 14 880 € si le bien était ancien — une économie de plus de 10 000 €. Elle ne constitue pas un gain net : la TVA à 20 % est déjà incorporée dans le prix affiché.

**Taxe foncière à 0 sur Monplaisir.** La ligne reflète l'exonération temporaire de taxe foncière de 2 ans applicable aux constructions neuves dans de nombreuses communes. **Le rendement net de 3,9 % n'est donc pas soutenable au-delà de la 3ᵉ année** : avec une taxe foncière normalisée à ~50 €/mois, il retombe vers 3,5 % et le cashflow passe de −183 € à −233 €. Toujours signaler ce décalage plutôt que de laisser le chiffre le plus flatteur en l'état.

**Rendements structurellement bas.** 3,2 % à 3,9 % de rendement net contre 4,0 % à 8,3 % dans l'exemple ancien : c'est l'écart habituel entre neuf et ancien, le prix au m² du neuf intégrant la marge du promoteur. Les trois lignes sont en cashflow négatif.

**Ces chiffres n'intègrent aucun dispositif fiscal.** Le skill ne modélise ni amortissement LMNP, ni dispositif de défiscalisation, ni récupération de TVA en résidence services — autant de mécanismes qui peuvent changer l'arbitrage neuf / ancien et qui relèvent d'un conseil professionnel.

## Restitution attendue

```
Paramètres de calcul :
- Type de bien : T3
- Budget max : 200 000 €
- Apport : 20 000 € (fixe)
- État : neuf → frais de notaire 2,5 %
- Taux crédit : 3,4 % (baromètre courtier)
- Vacance locative : 1 mois/an
```

**Verdicts**

| Bien | Rendement net | Cashflow 25 ans | Fiabilité loyer | Verdict | Justification |
|------|----------------|-------------------|-------------------|---------|----------------|
| Monplaisir | 3,9 % | −183 € | Annonce réelle | 🔴 À écarter | Cashflow sous le seuil de −150 €/mois, malgré le loyer fiable et la taxe foncière exonérée |
| Belle-Beille | 3,3 % | −287 € | Annonce réelle | 🔴 À écarter | Cashflow largement négatif malgré un loyer fiable |
| Saint-Serge | 3,2 % | −343 € | Estimation marché | 🔴 À écarter | Cashflow le plus négatif des trois, et loyer non confirmé par une annonce réelle |

**Recommandation de synthèse**

**Aucun des trois biens n'atteint le verdict Prioritaire.** Les trois cumulent un cashflow inférieur à −150 €/mois, dans une ville où le contexte INSEE est pourtant favorable sur le papier (croissance démographique de +0,6 %/an, parc à 58 % locatif) — mais où le taux d'effort locatif de 38,2 % signale que les loyers du neuf sont déjà tendus par rapport au revenu médian local : il ne faut pas compter sur une revalorisation rapide des loyers pour combler l'écart. Si un bien devait être visité malgré tout, Monplaisir serait le moins défavorable des trois (loyer fiable, taxe foncière exonérée), mais son rendement net retombe vers 3,5 % et son cashflow vers −233 € dès la fin de l'exonération. Sur ce marché et à ce niveau d'apport, l'ancien de l'[exemple 1](t2-ancien-saint-etienne.md) offre un profil nettement plus favorable — la piste à explorer est d'augmenter l'apport, d'élargir la recherche à l'ancien, ou de vérifier si un dispositif fiscal du neuf change l'arbitrage (hors périmètre de ce skill, voir [`references/calculs.md`](../references/calculs.md#6-rendement-net-de-charges-avant-impôt)).
