# Exemple — Cadrage, plan et un module rédigé

> **Ce que cet exemple montre.** Écrire un cours complet de 8-10k mots dans un exemple de dépôt serait ingérable et rapidement daté. Ce fichier montre à la place les livrables des Phases 1 à 3 (courts, faciles à vérifier) et **un seul module entièrement rédigé** (Phase 4), pour que la trame et le niveau de densité attendu soient concrets. Les faits cités (normes NIST, algorithmes, dates) sont réels et vérifiables au moment de la rédaction — mais n'ont pas fait l'objet des 15-25 recherches que le skill exige réellement ; c'est un gabarit de forme, pas un cours validé.

## Demande

```
Fais-moi un cours sur la cryptographie post-quantique
```

## Phase 1 — Cadrage

Le sujet bascule nettement selon l'angle : compréhension des fondements mathématiques (pourquoi RSA et les courbes elliptiques deviennent vulnérables), ou pilotage d'une migration organisationnelle (inventaire des systèmes, priorisation, calendrier). Un seul choix structurant, une seule question :

> « Tu veux un cours plutôt **technique** (les mécanismes cryptographiques, ce qui casse et pourquoi) ou plutôt **stratégique** (comment une organisation planifie sa migration) ? Je peux aussi couvrir les deux si le temps de lecture ne te fait pas peur. »

**Réponse retenue pour cet exemple : technique**, avec un module de clôture qui touche à la dimension migration sans en faire l'angle principal.

Langue : français (langue de la demande). Volume : 8 modules, 8-10k mots.

## Phase 2 — Recherche en 4 couches (résumé)

*(Dans une exécution réelle, cette section n'apparaît pas dans le livrable — elle est reconstituée ici pour montrer ce que chaque couche doit remonter.)*

- **Canon** : le processus de standardisation du NIST (2016-2024), les papiers fondateurs sur les réseaux euclidiens (lattice-based cryptography) et CRYSTALS-Kyber/Dilithium, les cours de cryptographie post-quantique du MIT et de l'ETH Zurich.
- **État de l'art** : les FIPS 203/204/205 publiés en août 2024 (ML-KEM, ML-DSA, SLH-DSA), les annonces matérielles récentes sur l'informatique quantique (dont la puce Willow de Google, décembre 2024) et ce qu'elles changent réellement au calendrier de menace.
- **Terrain** : les billets d'ingénierie de Cloudflare et Google sur leur déploiement de TLS post-quantique hybride en production, les retours d'expérience sur la taille des clés et l'impact sur les handshakes TLS.
- **Controverses** : les débats sur l'urgence réelle de la migration, les critiques de schémas post-quantiques antérieurs cassés après sélection (SIKE, cassé en 2022 après avoir atteint le tour final du concours NIST — un rappel que « post-quantique » ne veut pas dire « prouvé sûr »), le débat sur la nécessité du mode hybride (classique + post-quantique) à long terme.

**Ce que la recherche a fait apparaître d'inattendu** : la menace n'est pas seulement future. Le scénario « harvest now, decrypt later » — intercepter aujourd'hui du trafic chiffré pour le déchiffrer plus tard — rend la migration urgente pour toute donnée à durée de vie longue, indépendamment de la date d'arrivée d'un ordinateur quantique cryptographiquement pertinent.

**Zone faible** : les estimations de calendrier pour un ordinateur quantique capable de casser RSA-2048 varient énormément selon la source (de la fin de la décennie à plusieurs décennies) — traité comme `[débattu]` dans le cours plutôt que tranché arbitrairement.

## Phase 3 — Plan (validé avant écriture)

| # | Module | Contenu | Volume |
|---|--------|---------|--------|
| 1 | Pourquoi ce sujet existe | La menace quantique sur la cryptographie asymétrique, l'algorithme de Shor, « harvest now, decrypt later » | ~1100 mots |
| 2 | Vocabulaire et cadre conceptuel | Cryptographie symétrique vs asymétrique, problèmes durs classiques vs quantiques, familles post-quantiques (réseaux, codes, hachage, isogénies) | ~1000 mots |
| 3 | Fondations — la cryptographie à base de réseaux euclidiens | Le problème LWE, pourquoi il résiste au calcul quantique connu | ~1300 mots |
| 4 | Fondations — signatures et alternatives | Dilithium, SPHINCS+, les compromis taille/vitesse/sécurité entre familles | ~1200 mots |
| 5 | Standardisation | Le processus NIST 2016-2024, FIPS 203/204/205, ce qui a été cassé en chemin (SIKE) | ~1100 mots |
| 6 | Application — migrer un système réel | Mode hybride, TLS post-quantique chez Cloudflare et Google, impact sur la taille des certificats et les handshakes | ~1200 mots |
| 7 | Limites, échecs, controverses | Le débat sur l'urgence réelle, les schémas cassés après sélection, la dette technique du hybride | ~1000 mots |
| 8 | Écosystème et suite | Acteurs (NIST, ETSI, agences nationales), outils de migration, où va la recherche (isogénies après la casse de SIKE) | ~1000 mots |

**Arbitrage assumé** : le module 5 (standardisation) est placé après les fondations mathématiques (3-4) plutôt qu'avant, parce que comprendre *pourquoi* le NIST a choisi ces algorithmes précis suppose de déjà connaître les familles en compétition.

## Phase 4 — Un module rédigé (extrait)

## Module 1 — Pourquoi ce sujet existe

> **À la fin de ce module :** tu sauras expliquer pourquoi la cryptographie asymétrique actuelle est menacée par l'informatique quantique, et pourquoi cette menace concerne des données chiffrées aujourd'hui, pas seulement dans le futur.

### L'intuition

RSA et les courbes elliptiques (les deux familles qui protègent la quasi-totalité du trafic web chiffré aujourd'hui) reposent sur des problèmes mathématiques faciles à poser mais très longs à résoudre pour un ordinateur classique — factoriser un grand nombre, ou inverser une opération sur une courbe elliptique. « Très long » veut dire : même en mobilisant toute la puissance de calcul actuelle de la planète, ça prendrait plus de temps que l'âge de l'univers pour des clés de taille standard. C'est cette asymétrie — facile à vérifier, presque impossible à casser — qui fait la sécurité du chiffrement moderne.

Le problème, c'est qu'« impossible à casser » dépendait d'une hypothèse implicite : que personne ne dispose d'un type de calculateur radicalement différent. En 1994, Peter Shor a montré qu'un ordinateur quantique suffisamment grand et stable pourrait factoriser ces grands nombres en un temps raisonnable — pas instantané, mais des heures ou des jours plutôt que des ères géologiques. La sécurité de RSA et des courbes elliptiques ne s'effondre pas parce que le problème est devenu facile dans l'absolu ; elle s'effondre parce qu'un nouveau type de machine change la définition de « facile ».

### Le fond

L'algorithme de Shor s'attaque à deux problèmes structurellement liés : la factorisation d'entiers (base de RSA) et le logarithme discret (base de Diffie-Hellman et des courbes elliptiques). Les deux se résolvent en temps polynomial sur un ordinateur quantique suffisamment grand, contre un temps sous-exponentiel — donc praticable — pour les meilleurs algorithmes classiques connus. C'est cette différence de classe de complexité, pas une simple amélioration de vitesse, qui rend la menace qualitativement différente d'un progrès en puissance de calcul classique.

La cryptographie symétrique (AES, qui chiffre les données une fois la clé échangée) est beaucoup moins affectée. Le seul algorithme quantique pertinent, celui de Grover, offre une accélération quadratique sur la recherche exhaustive de clé — ce qui revient à diviser par deux la sécurité effective en bits. AES-256 reste donc considéré comme sûr face à un ordinateur quantique, alors qu'AES-128 verrait sa marge de sécurité sérieusement entamée. C'est pour cette raison que le débat post-quantique porte presque exclusivement sur la cryptographie asymétrique (l'échange de clé et les signatures), pas sur le chiffrement symétrique lui-même.

Reste la question du calendrier, et c'est là que les estimations divergent fortement `[débattu]`. Construire un ordinateur quantique cryptographiquement pertinent (« CRQC », capable de casser RSA-2048 en pratique) suppose des millions de qubits physiques fiables — les machines actuelles en comptent quelques centaines à quelques milliers, avec des taux d'erreur qui restent le principal obstacle. L'annonce par Google de sa puce Willow (décembre 2024), qui a démontré une correction d'erreur quantique passant sous le seuil critique pour la première fois à cette échelle, est un jalon scientifique réel — mais un jalon de correction d'erreur, pas une preuve qu'un CRQC arrive dans les prochaines années. Les estimations sérieuses de la communauté cryptographique vont, selon les sources, de la fin des années 2020 à plusieurs décennies — une fourchette large qui reflète une incertitude authentique, pas un simple désaccord d'opinion.

Ce qui transforme cette incertitude de calendrier en urgence immédiate, c'est le scénario **« harvest now, decrypt later »** : un adversaire capable d'intercepter et stocker du trafic chiffré aujourd'hui n'a pas besoin d'un ordinateur quantique maintenant — il lui suffit d'attendre qu'un CRQC existe pour déchiffrer rétroactivement ce qu'il a enregistré. Pour des données dont la confidentialité doit durer des décennies (secrets d'État, données de santé, propriété intellectuelle stratégique), la question n'est donc pas « quand le quantique arrivera-t-il » mais « ces données seront-elles encore sensibles à cette date » — et la réponse, souvent, est oui.

### En pratique

Le National Institute of Standards and Technology (NIST) américain a lancé en 2016 un concours public pour sélectionner de nouveaux standards cryptographiques résistants au quantique, ouvert à toute la communauté de recherche mondiale. Après plusieurs tours d'élimination et d'analyse cryptanalytique publique, quatre algorithmes ont été retenus en 2022, et trois ont été finalisés comme standards fédéraux américains en août 2024 : FIPS 203 (ML-KEM, dérivé de CRYSTALS-Kyber, pour l'échange de clé), FIPS 204 (ML-DSA, dérivé de CRYSTALS-Dilithium, pour les signatures) et FIPS 205 (SLH-DSA, dérivé de SPHINCS+, une signature basée sur le hachage plutôt que sur les réseaux euclidiens, en réserve de diversité mathématique) [NIST, 2024].

Cloudflare et Google ont commencé à déployer un échange de clé post-quantique en production dans leurs implémentations de TLS dès 2023, avant même la finalisation des standards — en mode **hybride** : la clé finale combine un échange classique (X25519) et un échange post-quantique (Kyber), de sorte que casser l'un des deux ne suffit pas à casser la connexion. Ce choix reflète une prudence méthodologique directement héritée de l'histoire du concours NIST (voir Module 5) : personne ne veut fonder la sécurité de demain sur un algorithme post-quantique qui n'a pas encore été suffisamment testé par la communauté.

### Pièges

- **Confondre « menace future » et « problème futur ».** À cause du scénario harvest-now-decrypt-later, ne rien faire aujourd'hui expose déjà les données à durée de vie longue, même si aucun ordinateur quantique capable de les déchiffrer n'existe encore.
- **Penser que le chiffrement symétrique (AES) doit changer radicalement.** Il suffit, au pire, de doubler la taille de clé (passer à AES-256) — c'est une adaptation mineure comparée à la refonte complète des mécanismes asymétriques.
- **Traiter la migration comme un simple remplacement d'algorithme.** En pratique, le standard actuel est le mode hybride (classique + post-quantique combinés), pas un remplacement pur — précisément parce que la confiance dans les nouveaux algorithmes est encore en construction.
- **Sous-estimer l'incertitude du calendrier.** Présenter une date précise d'arrivée du risque quantique comme un fait établi trahit une méconnaissance du sujet — c'est un point activement débattu dans la communauté, pas une donnée technique stabilisée.

### À retenir

- L'algorithme de Shor casse RSA et les courbes elliptiques en temps polynomial sur un ordinateur quantique suffisamment grand — une différence de classe de complexité, pas juste de vitesse.
- La cryptographie symétrique (AES) est beaucoup moins menacée : l'algorithme de Grover n'offre qu'une accélération quadratique, compensée en doublant la taille de clé.
- Le calendrier d'arrivée d'un ordinateur quantique cryptographiquement pertinent reste activement débattu, de la fin des années 2020 à plusieurs décennies selon les sources.
- Le scénario « harvest now, decrypt later » rend la migration urgente dès aujourd'hui pour toute donnée à confidentialité longue durée, indépendamment de ce calendrier.
- Le NIST a finalisé trois standards post-quantiques en août 2024 (FIPS 203, 204, 205) après un concours public ouvert depuis 2016 ; le déploiement en production se fait en mode hybride, pas en remplacement pur.

---

*(Les modules 2 à 8 suivraient la même trame — ils ne sont pas reproduits ici, cet exemple ayant pour seul objectif de montrer le format.)*
