# Workflows Git
> [Dernière mise à jour par @minapecheux-artline - 11/02/2022]

Un worfklow Git, c'est une organisation de travail et un ensemble de règles qui aide à utiliser Git de manière efficace et productive.

## Pourquoi utiliser un workflow Git ?

En soi, Git n'impose pas de structure. L'outil laisse chaque équipe assez libre de travailler à sa façon. Il existe donc différents "flows Git" et il n'y en pas "un meilleur que les autres"... mais certains systèmes sont néanmoins plus répandus et ont fait leurs preuves.

L'important, c'est de trouver le workflow qui convient à votre équipe et votre projet ! Comme expliqué dans [cet article](https://www.atlassian.com/fr/git/tutorials/comparing-workflows), un workflow doit aider, et pas contraindre ; donc, il doit :

- être adapté à la taille de l'équipe et aux objectifs
- permettre de corriger les erreurs / fautes facilement
- réduire la charge pour les devs (en donnant des standards, en automatisant ce qui peut l'être...)

## Principaux workflows Git

Actuellement, il y a deux workflows Git connus : le **"GitHub flow"** (historique) et le **développement basé sur le tronc** (plus apprécié de nos jours).

### Github Flow

Le **"GitHub flow"**, c'est un workflow simple de développement qui repose sur l'utilisation de **branches** de développement, et où seules certaines personnes ont le droit de venir re-merger le code dans les branches "principales".

L'avantage, c'est que ça maintient une bonne qualité de code et que ça réduit le nombre de bugs.

> Pour plus d'infos (lien en anglais) : https://docs.github.com/en/get-started/quickstart/github-flow.

L'idée, c'est de définir une **branche principale** comme référence (généralement `master` ou `main`) qui contient le code officiel, en production. Puis, si on doit :

- rajouter une nouvelle fonctionnalité (_feature_)
- résoudre un bug (_fix_)
- réorganiser un système sans en changer les fonctionnalités (_refactor_)
- mettre à jour la doc (_docs_)
- ...

alors on va **créer une nouvelle branche de développement** à partir de la branche principale dans son état actuel, et travailler en parallèle de la branche principale sur notre branche tout le long du développement.

Une fois le travail (feature, fix, refactor, docs...) terminé, on fait une "**pull request**" (= PR) de notre branche vers la branche principale. Un autre dev (souvent plus expérimenté) est alors en charge de vérifier que les changements sont valides et efficaces (c'est le "**reviewer**", qui fait une "review du code") et il accepte ou refuse la pull request.

**Si la PR est acceptée**, les commits sur la branche de développement sont réintégrés (= re-**mergés**) dans la branche principale, et font maintenant partie du code en production.

**Sinon**, le dev en charge du développement doit **corriger les erreurs** et continue à travailler sur sa branche de développement jusqu'à ce que sa PR soit acceptée.

Dans ce système, si une branche de développement est acceptée et intégrée dans la branche principale, toutes les autres branches de développement actuellement "en vie" doivent réintégrer ces changements également, à l'aide d'un [**rebase**](https://git-scm.com/docs/git-rebase). Cela peut créer des **conflits**, et c'est pour ça que ce workflow est parfois problématique...

### Développement basé sur le tronc

Le **développement basé sur le tronc**, au contraire, préconise des branches secondaires plus courtes qui sont régulièrement re-mergées dans les branches principales.

> Pour plus d'infos : https://www.atlassian.com/fr/continuous-delivery/continuous-integration/trunk-based-development.

Dans ce workflow, on a aussi une branche principale (le "tronc") `master` ou `main`, mais cette fois on ne s'embarque pas de dans longues branches de développement - on livre le code par petits lots, mieux scopés, et on cherche à tirer parti des outils modernes d'**intégration continue**.

En gros, on a moins de conflits que le GitHub flow, car les branches secondaires ont moins le temps de "dériver". Mais plus de personnes ont accès à la branche principale, on a aussi plus de risques d'avoir des bugs.

Ce risque est normalement contrôlé/réduit grâce à l'utilisation de processus de validations automatiques, de tests unitaires, etc. ; mais, de toute façon, comme on travaille à une échelle plus granulaire, le développement basé sur le tronc permet normalement plus facilement de corriger les erreurs et de revenir en arrière si nécessaire.

_Note : on peut aussi utiliser des "feature flags" pour temporairement désactiver une partie de la codebase - le nouveau code est donc intégré au code en production, mais il ne sera jamais réellement utilisé tant que le "flag" n'est pas activé..._

## Conseils & remarques

Comme pour les [Git Conventional Commits](./git-convential-commits.md), il peut être intéressant de mettre en place une nomenclature précise pour les branches.

Typiquement, quand on crée sa branche de développement, on peut s'inspirer des "git conventional commits" et préfixer son nom selon le type de tâche à effectuer :

- `feat/` pour une nouvelle fonctionnalité
- `fix/` pour une correction
- `refactor/` pour une réorganisation
- `test/` pour explorer une piste de travail
- ...

Par exemple, pour un petit projet de jeu vidéo : `feat/inventaire-heros`, `fix/ui-game-over`...
