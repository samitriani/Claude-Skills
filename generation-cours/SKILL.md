---
name: generation-cours
description: Construit un cours écrit complet et sourcé (8-10k mots, 8 modules) sur n'importe quel sujet, à partir de recherches en sources académiques, institutionnelles et industrielles. Déclencher dès que l'utilisateur veut apprendre, comprendre en profondeur ou monter en compétences sur un sujet — même sans le mot "cours". Déclencheurs typiques — "fais-moi un cours sur X", "j'ai besoin de monter en compétences sur X", "explique-moi X en profondeur", "je veux comprendre X sérieusement", "forme-moi sur X", "prépare-moi un support pour apprendre X", "je dois maîtriser X pour...". Utiliser aussi quand la demande porte sur un domaine technique, réglementaire ou méthodologique que l'utilisateur dit ne pas connaître. Ne PAS utiliser pour une simple question factuelle, une définition, ou une explication courte tenant en quelques paragraphes.
license: MIT
---

# Cours Approfondi

Produire un cours qu'on lit pour vraiment apprendre, pas un résumé Wikipédia allongé.

La différence tient à trois choses, et tout le reste de ce skill en découle :
1. **La structure est dérivée de syllabi existants**, pas inventée. Des gens ont passé des années à trouver dans quel ordre enseigner ce sujet — utiliser leur travail.
2. **Les controverses sont incluses.** Un cours qui présente un domaine comme consensuel alors qu'il ne l'est pas est un cours faux.
3. **Rien n'est comblé par de la génération plausible.** Une zone mal documentée est signalée comme telle.

Le pipeline a 5 phases. La phase 3 comporte un point d'arrêt obligatoire.

---

## Phase 1 — Cadrage

Un sujet seul est ambigu : « LLM » peut vouloir dire 3h de culture générale ou 30h d'ingénierie.

Inférer d'abord depuis le contexte disponible (métier de l'utilisateur, conversation, sujet lui-même). Ne poser une question que si un choix structurant reste indéterminé — typiquement l'angle (stratégique / technique / opérationnel) quand le sujet peut basculer d'un côté ou de l'autre. Une seule question, avec des options, jamais un questionnaire.

Fixer aussi :
- **Langue du cours** = langue de la demande.
- **Volume** = 8 modules, 8-10k mots par défaut. Ajuster si l'utilisateur le demande.

Ne pas annoncer le cadrage comme une étape. Enchaîner.

---

## Phase 2 — Recherche en 4 couches

C'est le vrai levier de qualité. Compter **15 à 25 recherches**. Moins, et le cours devient une paraphrase de mémoire.

Les 4 couches ne sont pas interchangeables : chacune apporte quelque chose que les autres n'ont pas.

### Couche 1 — Canon (5-8 recherches) — donne la STRUCTURE

Objectif : trouver comment le domaine est enseigné, et le vocabulaire exact que les experts emploient.

Requêtes qui marchent :
- `[sujet] syllabus` / `[sujet] lecture notes` / `[sujet] course outline`
- `[sujet] MIT OpenCourseWare` / `Stanford [sujet] course`
- `[sujet] textbook table of contents` — la table des matières d'un manuel de référence est un plan de cours déjà validé
- `[sujet] seminal paper` / `[sujet] original paper` — pour comprendre d'où vient le domaine
- `[sujet] survey arxiv` / `[sujet] systematic review` — un bon survey résume 100 papiers

### Couche 2 — État de l'art (3-5 recherches) — donne l'ACTUALITÉ

Requêtes :
- `[sujet] 2026` (utiliser l'année en cours, pas une année passée)
- `[sujet] recent advances` / `[sujet] latest research`
- `[sujet] what changed` / `[sujet] new approach`

Attention aux dates. Un domaine qui bouge vite rend obsolète un cours basé sur des sources de 2 ans.

### Couche 3 — Terrain (4-6 recherches) — donne la CRÉDIBILITÉ OPÉRATIONNELLE

C'est ce qui distingue un cours utile d'un cours théorique. Objectif : comment ça se passe réellement quand on l'applique.

Requêtes :
- `[sujet] case study` / `[sujet] in production` / `[sujet] lessons learned`
- `[sujet] engineering blog` — les blogs techniques des entreprises qui font vraiment la chose
- `[sujet] standard` / `[sujet] ISO` / `[sujet] NIST` / `[sujet] regulation` — s'il y a un cadre normatif ou réglementaire, il structure la pratique et son absence dans le cours serait une faute
- `[sujet] benchmark` / `[sujet] cost` — les chiffres réels

### Couche 4 — Controverses (3-4 recherches) — donne l'HONNÊTETÉ

Sans cette couche, le cours est de la brochure commerciale.

Requêtes :
- `[sujet] criticism` / `[sujet] limitations` / `[sujet] does not work`
- `[sujet] failure` / `[sujet] postmortem` / `[sujet] why projects fail`
- `[sujet] debate` / `[sujet] controversy` / `[sujet] overhyped`
- `[sujet] alternative to` — les approches concurrentes et pourquoi certains les préfèrent

### Hiérarchie des sources

| Tier | Quoi | Usage |
|---|---|---|
| **A** | Papiers avec comité de lecture, manuels de référence, cours universitaires, normes officielles, textes réglementaires | Fondations, définitions, formalisme |
| **B** | Rapports institutionnels (OCDE, NIST, Commission européenne, agences nationales), documentation officielle d'éditeurs, cabinets avec méthodologie publiée | État des pratiques, chiffres de marché |
| **C** | Blogs d'ingénierie d'organisations identifiées, retours d'expérience détaillés et signés, conférences techniques | Réalité opérationnelle, exemples |

À exclure : contenu SEO, listicles, blogs sans auteur identifiable, agrégateurs, résumés produits par IA, pages de vente déguisées en articles.

Si un sujet ne remonte que du Tier C, c'est une information en soi : le domaine est immature ou peu étudié. Le dire dans le cours.

---

## Phase 3 — Plan, validé avant écriture

**Point d'arrêt obligatoire.** Ne jamais écrire le cours sans validation du plan. Écrire 9000 mots dans la mauvaise direction est le pire échec possible de ce skill.

### Construire le plan par dépendances conceptuelles

Pas par ordre alphabétique de sous-thèmes, pas par ordre chronologique d'apparition dans les recherches. La question à chaque module est : **qu'est-ce qu'il faut avoir compris avant de pouvoir comprendre ça ?**

Aucune structure imposée. Le nombre de modules, leur ordre et leur découpage se déduisent du sujet lui-même et de ce que la recherche a fait apparaître — pas d'un gabarit générique. Les controverses et les limites doivent être traitées quelque part dans le plan (pas forcément en fin, pas forcément dans un module dédié), et l'ancrage terrain (couche 3) doit irriguer plusieurs modules plutôt que d'être relégué à un seul.

### Présenter le plan

En chat, compact : titre de chaque module + une ligne sur son contenu + volume estimé. Ajouter :
- Ce que la recherche a fait apparaître d'inattendu et qui a influencé le plan
- Les zones où les sources sont faibles ou contradictoires
- 1 ou 2 arbitrages assumés (« j'ai mis X en module 6 plutôt qu'en 2 parce que… »)

Signaler aussi, module par module, si un schéma est prévu (voir Phase 4 — Schémas) et lequel type.

Puis attendre. Ajuster autant que nécessaire.

---

## Phase 4 — Rédaction

### Mécanique d'écriture

Le cours va dans un seul fichier `.md`. L'emplacement dépend de l'environnement d'exécution :
- s'il existe un dossier de sortie conventionnel pour les livrables destinés à l'utilisateur (par exemple `/mnt/user-data/outputs/` sur certains déploiements Claude), l'utiliser ;
- sinon, écrire dans le répertoire de travail courant, avec un nom de fichier clair dérivé du sujet (ex. `cours-transformers.md`).

**Écrire module par module, pas en un seul jet** : créer le fichier avec l'en-tête et le module 1, puis ajouter chaque module suivant par des éditions successives (append), avec l'outil d'écriture/édition de fichier disponible dans l'environnement. Un cours de 9000 mots produit d'une traite se dégrade en fin de parcours et risque la troncature. Module par module, chacun reçoit la même attention.

### Contenu de chaque module

Pas de trame fixe. La forme (analogie ou non, formalisme ou non, ordre des sous-parties) se décide au cas par cas selon ce que le sujet exige. Ce qui reste requis, quelle que soit la forme :
- Une définition claire de ce qu'on saura faire ou distinguer à la fin du module.
- Au moins un exemple concret tiré des sources — acteur nommé, chiffre, cas réel.
- Les erreurs ou confusions fréquentes sur ce point, quand la recherche (couche 4) en a fait remonter.
- Les controverses ou limites propres au module, quand elles existent — pas reléguées systématiquement à la fin du cours.

### Schémas

Un seul livrable : le `.md`. Les schémas sont des blocs Mermaid intégrés directement dans le texte du module, jamais un fichier séparé ni une image externe.

Un schéma se justifie quand le concept est **intrinsèquement visuel** — une structure, un flux, une hiérarchie, une comparaison, une séquence temporelle sont plus clairs en diagramme qu'en prose. Ce n'est pas systématique : la plupart des modules n'ont besoin d'aucun schéma. Un schéma qui n'ajoute rien à ce que la prose dit déjà est un remplissage visuel — même défaut que le remplissage textuel.

Types Mermaid à mobiliser selon le besoin : `flowchart` pour un processus ou une décision, `graph` pour une architecture ou des relations, `timeline` pour une chronologie, `quadrantChart` pour une comparaison à deux axes, `sequenceDiagram` pour une interaction entre acteurs. Choisir le type qui correspond à la nature du concept, pas le premier venu.

Chaque schéma est placé au point du texte où il éclaire le propos — jamais regroupé en annexe — et introduit par une phrase qui dit ce qu'il montre, pas juste "voir le schéma ci-dessous".

### Règles de contenu

**Aucun chiffre sans source.** Format inline : `62 % des projets échouent [McKinsey, 2025]`. Un chiffre non sourcé est un chiffre inventé.

**Marquer le statut épistémique** quand ce n'est pas établi :
- rien à marquer si consensus
- `[débattu]` si les experts ne sont pas d'accord — et expliquer les deux positions
- `[émergent]` si trop récent pour être validé

**Ne pas combler les trous.** Si un module manque de matière solide, deux options : le fusionner avec un autre, ou écrire explicitement « cette zone est peu documentée — voici ce qui existe et ce qui manque ». Jamais d'étirement par du contenu plausible.

**Nommer les choses.** « Certaines entreprises » → « Netflix, dans son postmortem de 2024 ». Le concret est ce qui rend un cours mémorisable.

---

## Phase 5 — Ancrage et livraison

Trois sections finales, après les modules :

**Glossaire** — chaque terme technique du cours, défini en une phrase. Le lecteur y revient.

**Vérification de compréhension** — 8 à 12 questions ouvertes, une ou deux par module, qui demandent d'expliquer ou d'arbitrer, pas de restituer. Réponses attendues en 2-3 lignes juste après chaque question, repliées ou en fin de section.

**Pour aller plus loin** — bibliographie hiérarchisée par tier, avec pour chaque entrée une ligne sur ce qu'elle apporte et à qui elle sert. Une liste de liens sans annotation est inutile.

### Livraison

Remettre le fichier `.md` à l'utilisateur via le mécanisme disponible dans l'environnement (envoi de fichier, artefact, ou indication du chemin créé), puis en chat : 3-4 lignes maximum — ce que le cours couvre, et le point le plus contre-intuitif que la recherche a fait remonter. Pas de résumé du cours : il est dans le fichier.

---

## Anti-patterns

Ce qui fait échouer ce skill, par ordre de fréquence :

- **Sous-rechercher.** 5 recherches puis rédaction depuis la mémoire. Le résultat est fluide et creux. Si moins de 15 recherches ont été faites, le cours n'est pas prêt.
- **Sauter la validation du plan.**
- **Omettre la couche controverses.** Produit un cours qui ressemble à du marketing.
- **Écrire les 8 modules en un seul jet.** Les 3 derniers sont toujours plus faibles.
- **Chiffres non sourcés.**
- **Faux équilibre.** Présenter une position marginale comme équivalente à un consensus solide est aussi malhonnête que masquer un désaccord réel. Dire le poids relatif des positions.
- **Remplissage.** Mieux vaut 6 modules denses que 8 dont 2 sont vides.

## Ressources

- [`examples/`](examples/) — un cours complet illustrant le format attendu : plan par dépendances conceptuelles, modules sans trame fixe mais avec les quatre exigences de fond, glossaire, vérification de compréhension, bibliographie hiérarchisée
