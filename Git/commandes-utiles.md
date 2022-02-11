# Commandes utiles
> [Dernière mise à jour par @minapecheux-artline - 11/02/2022]

## Commandes de base

- initialiser un nouveau dépôt Git (à lancer dans le répertoire où on souhaite créer le dépôt) :
  
  ```
  git init
  ```

- cloner un dépôt Git (pour initialiser un dépôt à partir d'une source déjà existante) :
  
  ```
  git clone <adresse-du-depot>
  ```

  Par exemple, pour un projet Github "MyProject" d'un user "MyUser" :

  ```
  git clone git@github.com:MyUser/MyProject.git
  ```

- lister l'historique du dépôt (= l'ensemble des commits jusqu'à maintenant)
  
  ```
  git log
  ```

  *Note : n'hésitez pas à lancer `git log --help` pour voir toutes les options disponibles - il y en a beaucoup ! :)*

- lister la liste des changements non committés :
  
  ```
  git status
  ```

- voir tous les changements non committés, fichier par fichier :
  
  ```
  git diff
  ```

- ajouter des fichiers modifiés et faire un commit (suivant les bonnes pratiques des [Git Conventional Commits](./git-convential-commits.md)) :

  ```
  git add fichier1.txt fichier2.py
  git commit -m "chore(exemples): ajout de 2 fichiers d'exemple"
  ```

- annuler des changements locaux sur des fichiers non committés :

  ```
  git checkout fichier1.txt fichier2.py ...
  ```

- **A UTILISER AVEC PRÉCAUTION !** - annuler tous les changements locaux et revenir au dernier état "partagé" du dépôt :

  ```
  git reset --hard HEAD
  ```

  *Note : cette commande est équivalente à supprimer votre copie locale du dépôt Git et le re-cloner depuis la source distante.*

- **A UTILISER AVEC PRÉCAUTION !** - annuler tous les changements locaux et revenir à un commit particulier :

  ```
  git reset --hard <hash-du-commit>
  ```

## Local/Remote

Généralement, le dépôt distant (ou "remote") est appelé `origin`. Donc, dans les commandes ci-dessous, on peut a priori remplacer `<remote>` par `origin`.

- lister le(s) dépôt(s) distant(s) lié(s) au dépôt local courant :
  
  ```
  git remote -v
  ```

- lier un dépôt distant au dépôt local :
  
  ```
  git remote add <remote> <adresse>
  ```

  Par exemple, pour un projet Github "MyProject" d'un user "MyUser" :

  ```
  git remote add origin git@github.com:MyUser/MyProject.git
  ```

- récupérer tous les derniers changements du dépôt distant (nouvelles branches, branches supprimées, etc.) :
  
  ```
  git fetch <remote>
  ```

- récupérer en local tous les derniers changements d'une branche distante (= derniers commits sur la branche) :
  
  ```
  git pull <remote> ma-branche
  ```

- envoyer les derniers changements locaux d'une branche sur sa version distante :
  
  ```
  git push <remote> ma-branche
  ```

  Si la branche n'existe pas encore, Git vous proposera de la créer avec :

  ```
  git push --set-upstream <remote> ma-branche
  ```

## Branches

### Création de branches

- lister toutes les branches disponibles :
  
  ```
  git branch
  ```

- créer une branche, puis basculer dessus (en 2 étapes) :
  
  ```
  git branch ma-branche && git checkout ma-branche
  ```

- créer une branche et basculer dessus directement (en 1 étape) :
  
  ```
  git checkout -b ma-branche
  ```

### Suppression de branches

- supprimer une branche locale :
  
  ```
  git branch -d ma-branche
  ```

- supprimer une branche distante :
  
  ```
  git branch -dr ma-branche
  ```

### Synchronisation de branches local/remote

- récupérer l'état distant en local de la branche courante (cas simple)
  
  ```
  git pull
  ```

- récupérer l'état distant en local de la branche courante (avec [rebase](https://git-scm.com/docs/git-rebase))
  
  ```
  git pull --rebase
  ```

- récupérer l'état distant d'une autre branche en local (avec [rebase](https://git-scm.com/docs/git-rebase))
  
  ```
  git pull --rebase origin autre-branche
  ```

## Bonus : petits scénarios avancés

- suivant les bons principes des [workflows Git](./workflows-git.md) : récupérer les dernières modifications de la branche `master` et en tirer sa branche de feature, fix, etc. :
  
  ```sh
  git checkout master
  git pull --rebase # mise à jour par rapport à l'état distant
  git checkout -b feat/ma-feature # création de votre branche
  git status # vérifier que vous êtes sur votre branche
  git push --set-upstream origin feat/ma-feature # création de la version distante de votre branche
  ```

- 
