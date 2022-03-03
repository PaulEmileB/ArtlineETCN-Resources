# Versionner et partager son code
> [Dernière mise à jour par @minapecheux-artline - 03/03/2022]

## Trucs et astuces

- [Commandes utiles](./commandes-utiles.md) : une petite **_cheatsheet_ de commandes Git** courantes, pratiques ou même un peu plus exotiques...
- Parfois, on veut que Git "ignore" certains fichiers et qu'ils ne soient jamais ajoutés à l'historique des commits (ex : des fichiers avec des mots de passe, des dépendances ou bibliothèques externes...). Pour ça, on utilise un fichier **.gitignore**.
  
  Ce fichier doit être appelé exactement comme ça et placé à la racine du dépôt, et il contient une liste de tous les [**wildcards**](https://en.wikipedia.org/wiki/Wildcard_character) à ignorer. Par exemple :

  ```
  __pycache__/
  venv/
  *.pyc
  ```

  Vous pouvez trouver des modèles de `.gitignore` classiques pour votre langage/type de projet sur [le Github officiel gitignore](https://github.com/github/gitignore/) :)

## Conventions, bonnes pratiques

- [Git Conventional Commits](./git-convential-commits.md) : un ensemble de **bonnes pratiques** pour la rédaction de vos **messages de commits**

- [Workflows Git](./workflows-git.md) : des règles pour mieux **s'organiser et utiliser Git efficacement** en production

## Liens utiles

- [Website de Git](https://git-scm.com/), avec notamment la [liste de toutes les commandes disponibles](https://git-scm.com/docs)

- Liste des [clients GUI Git](https://git-scm.com/downloads/guis) pour utiliser Git avec une interface visuelle plutôt que la ligne de commande

- [Learn Git Branching](https://learngitbranching.js.org/?locale=fr_FR) : un petit parcours ludique pour apprendre à utiliser Git dans un bac à sable, avec des petits exercices croissants en difficulté
