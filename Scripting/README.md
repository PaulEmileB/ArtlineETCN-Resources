# Coder dans les règles de l'art
> [Dernière mise à jour par @minapecheux-artline - 16/02/2022]

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
