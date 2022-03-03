# Coder dans les règles de l'art
> [Dernière mise à jour par @minapecheux-artline - 03/03/2022]

## Environnement, dépendances

- En général, un projet Python a vite besoin de dépendances externes : les bibliothèques *built-in* deviennent trop limitées et on doit utiliser des packages plus puissants.

  Ces packages peuvent être listés et récupérés sur le Python Package Index, ou [PyPI](https://pypi.org/), une sorte "d'annuaire" de bibliothèques Python.

  Pour [installer une dépendance dans son projet](https://docs.python.org/fr/3/installing/index.html), on utilise `pip`, un utilitaire en ligne de commande qui est capable d'aller chercher dans cet annuaire un package, à partir de son nom.

  Par exemple, pour installer le package [`numpy`](https://pypi.org/project/numpy/), très utilisé en *data science*, on peut lancer la commande :

  ```
  pip install numpy
  ```

  Cette commande ira chercher la dernière version disponible du package nommé "numpy" sur le PyPI. On peut aussi spécifier une version particulière du package si on veut fixer la dépendance :

  ```
  pip install numpy==1.22.2
  ```

- Pour bien contrôler son environnement de développement, souvent, il est pratique d'[utiliser des **environnements virtuels**](https://docs.python.org/3/tutorial/venv.html.), ou *virtual environments*, qui "isolent" les projets et permettent de séparer les dépendances de chacun, voire même la version de Python à utiliser (Python 2, Python 3.6, etc.). En gros, on définit notre configuration au niveau du projet plutôt que d'avoir une seule configuration globale où on mélange tout !

  Les trois utilitaires les plus connus pour créer des environnements virtuels sont [`venv`](https://docs.python.org/3/library/venv.html#module-venv) (inclus de base avec Python), [`virtualenv`](https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html) et [`pipenv`](https://pypi.org/project/pipenv/).
  
- Et puis, il est important de connaître les dépendances de son projet ! En Python, on stocke généralement la liste des bibliothèques nécessaires à notre projet dans un fichier `requirements.txt`, qui contient la liste des libs avec éventuellement leur version exacte :

  ```
  numpy==1.9.2
  requests==2.7.0
  ```
  
  Ce fichier peut être utilisé par l'outil `pip` pour installer directement toutes les bibliothèques chez votre collègue ou votre client :

  ```
  pip install -r requirements.txt
  ```

  Pour connaître la liste des dépendances actuellement installées, on peut faire un `pip freeze`.

## Liens utiles

- [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) : des règles de "bonne conduite" pour écrire du Python joli, lisible, conventionnel...
  
  Ça tient en 20 lignes (parfois c'est évident, mais c'est bien de le rappeler... et surtout, c'est hiérarchisé !) :

  ```
  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts.
  Special cases aren't special enough to break the rules.
  Although practicality beats purity.
  Errors should never pass silently.
  Unless explicitly silenced.
  In the face of ambiguity, refuse the temptation to guess.
  There should be one-- and preferably only one --obvious way to do it.
  Although that way may not be obvious at first unless you're Dutch.
  Now is better than never.
  Although never is often better than *right* now.
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those!
  ```

- [Pep8](https://www.python.org/dev/peps/pep-0008/) : dans le même ordre idée, ce guide liste les conventions pour écrire du Python "dans les règles de l'art" (il a été rédigé par Guido van Rossum, le créateur du Python, et ces conventions sont typiquement suivies par les modules _built-in_ du Python).

  Comme écrit dans le document : ce ne sont pas des principes à appliquer absolument et aveuglément - il faut toujours privilégier la lisibilité ! Donc, à considérer pour écrire du code "conventionnel", mais aussi parfois à contourner si ça risque d'être nuisible dans votre cas particulier... :)

- [CheatSheet pour écrire du code Python 2/3 compatible](https://python-future.org/compatible_idioms.html) : même si, aujourd'hui, l'utilisation du Python 2 est déconseillée (depuis 2020), beaucoup de code pré-existant (= _legacy code_) et même beaucoup d'intégrations Python dans des DCCs (Maya, Blender, Houdini) s'en servent encore.
  
  Ecrire du code compatible avec les deux versions (Python 2 et Python 3) n'est pas toujours simple, cette doc vous aide à repérer les principales différences et vous donne des petites astuces pour que vos programmes soient plus "universels" ! 

- [Are we Python 3 ready?](https://vfxpy.com/) : pour approfondir, un état des lieux des supports Python dans les DCCs les plus courants
