
# Générateur
Il s'agit d'une fonctionnalité essentielle de Python que l'on retrouve aussi dans d'autres langages (itérateurs en C++ par exemple).
L'idée du générateur, c'est de pouvoir justement générer des éléments au fur et à mesure de leur utilisation.

Imaginez par exemple, une usine qui fabrique des cartons.
Pour faire un carton, nous avons besoin du carton à proprement parlé (cardboard) et de ruban adhésif (tape).
On utilise ces 2 ressources pour assembler une boite (box).
En python, cela se traduit par 3 fonctions: `build_carboard`, `build_tape` et `assemble_box`

Nous allons vouloir assembler autant de cartons possibles jusqu'à ce que l'une des ressources soit épuisée (sans connaitre les quantités à l'avance).

Une première méthode consiste à fabriquer tous le scotch et les cartons possibles:
```python

def build_cardboard():
  # Build all the cardboard we can
  # ...
  # And return them
  return ['carton1', 'carton2', 'carton3']

def build_tape():
  # Build all the tape we can
  # ...
  # And return them
  return ['tape1', 'tape2', 'tape3', 'tape4']

def assemble_box(cardboard, tape):
  return [(cardboard, tape)]


cardboards = build_cardboard()
tapes = build_tape()

max_assembled_cardboard = max(len(cardboards), len(tapes))

for idx in range(max_assembled_cardboard):
    assemble_box(cardboards[idx], tapes[idx])
```

Le problème avec cette méthode, c'est que nous utilisons des ressources pour rien.
Si il y a plus de carton que de ruban adhésif, au final, on aura créé trop de cartons.
D'un point de vue programmation, nous avons utilisé du temps CPU pour fabriquer des cartons et de la mémoire pour rien.
Dans cette exemple, la quantité de carton et de ruban est faible donc ce n'est pas très lourd mais imaginez le scénario suivant:

On génère tous les cartons possibles et on en génère au final 100.000.
On fait pareil avec le scotch et on en génère 1.000.
On a donc généré 99.000 cartons pour rien.
Si chaque carton pèse 10 ko en mémoire et qu'il faut 1 ms de temps CPU pour en fabriquer un,
on aura donc au total passé 1 ms * 99.000 = 99s et 10ko * 99.000 = 966 Mo.

99s et 966 Mo pour rien! C'est vraiment pas top!

De plus, même si la quantité de carton et de ruban est équilibré (à peu près autant de carton que de ruban), 
il y a bien un moment où l'on va utilisé toute cette mémoire pour stocker tous les cartons et rubans que l'on a généré.

En utilisant un générateur, nous allons pouvoir justement pallier à tout ces problèmes.
Nous allons généré les cartons et les rubans adhésifs au fur et à mesure jusqu'à ce que l'une des ressources 
soit épuisée:

```python

def build_cardboard():
  # Generator of cardboard
  yield 'carton1'
  yield 'carton2'
  yield 'carton3'


def build_tape():
  # Generator of tape
  yield 'tape1'
  yield 'tape2'
  yield 'tape3'
  yield 'tape4'


def assemble_box(cardboard, tape):
  return [(cardboard, tape)]


cardboard_gen = build_cardboard()
tape_gen = build_tape()

while True:
    try:
        cardboard = next(cardboard_gen)
        tape = next(tape_gen)
    except StopIteration:
        break
    assemble_box(cardboard, tape)
```

Passons en revue ce code:

Premièrement, nous avons transformé nos 2 fonctions `build_cardboard` et `build_tape` en générateur.
Pour se faire, on utilise le mot-clé `yield` qui indique que nous l'on renvoie l'élément indiqué. On génère l'élément 
et on le met à disposition de la fonction appelante.

Lorsque l'on appelle ces fonctions, on ne crée pas nos cartons ou nos rubans mais un objet `generator`.
Ici, on crée ces `generator` avec ces deux lignes:

```python
cardboard_gen = build_cardboard()
tape_gen = build_tape()
```

On peut utiliser la fonction built-in `next` pour demander à générer le prochain élément.
Cela a pour effet 'd'avancer' l'exécution des fonctions `build_cardboard` et `build_tape` jusqu'au prochain `yield`.

Lorsqu'il n'y a plus rien à générer, l'utilisation de next va lever l'exception `StopIteration`.

Pour résumer ce qu'il se passe dans la boucle `while`:
1) On génère un carton
2) On génère un ruban
3) Si l'une des ressources vient à manquer, on arrête notre boucle
4) Sinon on assemble notre boite et on retourne au 1)

L'avantage de cette méthode, c'est qu'on ne fabrique qu'un seul carton et qu'un seul ruban à la fois.
Ainsi, le maximum de mémoire qu'on utilise à n'importe quel moment de notre programme c'est le poid d'un ruban + un carton.
De plus, on arrêtera de générer des ressources dès que l'une d'entre elles est épuisée.
Génial!

Vous retrouverez quelques exemples de générateurs dans le fichier generator.py.


# Context manager
Les context manager nous permette d'exécuter n'importe quel code python dans un scope maitrisé (contexte).
Vous avez surement déjà utilisé des context managers sans vous en rendre compte.

```python
with open("/path/to/my/file") as f:
    f.read()
```

Ce vous dit quelque chose? Et bien il s'agit de l'utilisation d'un context manager!
On reconnait l'utilisation d'un context manager grâce au mot-clé `with`.
On pourrait parfaitement remplacer ce code par le code suivant:

```python
f = open("/path/to/my/file")
f.read()
f.close()
```

Mais ce dernier pose quelques problèmes.
En effet, si quelque chose se passe mal durant l'exécution de la ligne `f.read()`, 
notre programme va crasher et le fichier restera ouvert (pour l'os).
C'est pas génial.

Pour pallier à ça, on pourrait tenter de gérer les exceptions qui pourrait être levées:

```python
f = open("/path/to/my/file")
try:
    f.read()
except Exception as e:
    # Oups
    f.close()
    raise e  # On ne rend JAMAIS une exception silencieuse si on ne la gère pas
else:
    f.close()
```

Cela fait beaucoup de ligne pour quelque chose qu'on va faire très souvent (ouvrir un fichier).
Et bien figurez vous que le code ci-dessus fait exactement ce que fait le ` with open()`: il "entoure" le code utile (ici `f.read()`) pour catcher d'enventuelles exceptions et assurer la fermeture du fichier.

Ok tout ça c'est super mais à part pour ouvrir des fichiers ça sert à quoi?
Dans une grande majorité de cas, cela permet de gérer des erreurs qui peuvent se produire.
En pratique, on retrouve très souvent des context managers pour:

- rollback des transactions sur des bases de données
- restaurer des états initiaux
- publier des fichiers
- gérer de pool
- etc...

On va regarder ensemble un cas concret pour vous montrer comment créer nos propres context managers: la gestion des undo dans Maya.

La totalité des logiciels fournissent une commande d'annulation (undo). 
Pour se faire le logiciel garde en mémoire l'intégralité des commandes qui ont été exécutées et les organisent en pile. 
Imaginons qu'on soit dans Maya fraichement ouvert et que l'on crée une sphère puis qu'on la déplace pour finalement la supprimer.
On aura ainsi dans notre stack d'undo, les commandes suivantes:

```
deleteObject <-
moveObject
createSphere
```

Lorsque l'on appuie sur Ctrl+Z pour annuler notre dernière action, on va remonter dans la pile:

```
deleteObject
moveObject <-
createSphere
```

Ça c'est pour le principe.

Si on code un script qui fait la même chose (créer, déplacer et supprimer une sphère),
vous verrez que de base dans Maya, toutes ces commandes se retrouvent dans la pile d'undo.

Ici ça va parce que ce n'est que 3 commandes, on peut toujours revenir en arrière facilement.
Mais imaginez que maintenant mon script exécute des centaines de commandes! 
Il va falloir être patient pour annuler les effets de ce script...

En fait, dans le cas de notre script, on voudrait que toutes nos commandes comptent pour une seule et qu'un Ctrl+Z annule l'ensemble.

```
myScript <-
    deleteObject
    moveObject
    createSphere
```

Heureusement, les développeurs de Maya y ont pensé et vous fournisse une commande Python (issue du MEL) pour ça: `cmds.undoInfo`

Si vous regardez la doc, vous verrez qu'on peut attendre notre objectif avec cette suite de commande:

```python
from maya import cmds

cmds.undoInfo(openChunk=True, chunkName="myUndoChunk")
# Doing all my commands
cmds.undoInfo(closeChunk=True)
```

Génial! Mais... et oui, il y a un mais.
Si vous lisez attentivement la doc, vous verrez ceci concernant l'ouverture et la fermeture d'un chunk: `Use with CAUTION!! Improper use of this command can leave the undo queue in a bad state. `

En fait, le principale problème, c'est que si il se passe quelque chose de mal durant l'exécution de vos commandes et bien vous allez laisser un chunk ouvert.
C'est vraiment pas bon et cela va générer des erreurs voir carrément faire crasher Maya.
En fait, on voudrait protéger l'exécution de nos commandes entre l'ouverture et la fermeture de notre chunk d'undo.
Comment est-ce qu'on va faire ça? Avec un context manager pardi!

Ce qu'on veut au final c'est créer quelque chose comme ça:

```python
with undo_chunk(name="myUndoChunk"):
    # Doing all my nasty commands
```

Alors c'est parti!

Il existe 2 manières de faire des context managers en Python: en utilisant le package `contextlib` ou en créant une classe avec des attributs spéciaux.

Avec le package `contextlib`, voici à quoi ressemble l'implémentation:


```python
from contextlib import contextmanager
from maya import cmds

@contextmanager
def undo_chunk(name):
    cmds.undoInfo(openChunk=True, chunkName=name)
    try:
        yield  # On renvoit à l'appelant pour qu'il puisse exécuter son code (dans le with)
    except Exception as e:
        # Oups, ça c'est pas bien passé, on ferme le chunk
        cmds.undoInfo(closeChunk=True)
        raise e 
    else:
        # Si tout c'est bien passé, on ferme quand même le chunk
        cmds.undoInfo(closeChunk=True)
```

Voici la méthode avec une classe et les fonctions spéciales `__enter__` et `__exit__`:

```python

from maya import cmds


class UndoChunk(object):
    
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        # Exécuter lorsque l'on rentre dans un with
        cmds.undoInfo(openChunk=True, chunkName=self.name)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Exécuter lorsque l'on sort du with avec, en arguments, 
        # les éventuelles exceptions levées dans le with (si vous voulez les gérer)
        cmds.undoInfo(closeChunk=True)  # On ferme dans tous les cas
        
        # Python lévera par défaut toute exception générer dans le with 
        # sauf si vous retourner True depuis cette fonction __exit__
```

Allez, un dernier exemple Maya pour la route.
Quelque chose de très agaçant avec Maya, c'est qu'il sélectionnes très souvent des éléments lorsqu'on exécute des commandes.
Pour pallier ça, on peut utiliser un context manager qui pourra restaurer notre précédente sélection:

Version contextlib:

```python
from contextlib import contextmanager
from maya import cmds

@contextmanager
def restore_selection():
    old_selection = cmds.ls(selection=True)  # On sauvegarde la sélection
    yield  # On laisse l'appelant faire ce qu'il veut
    cmds.select(old_selection)  # On restaure la sélection précédente

    
# Cas d'utilisation
with restore_selection():
    # Fait plein de chose qui change la sélection

# Ma sélection est restaurée!
```

Version classe:
```python

from maya import cmds


class RestoreSelection(object):
    
    def __init__(self):
        self.old_selection = []
    
    def __enter__(self):
        self.old_selection = cmds.ls(selection=True)  # On sauvegarde la sélection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        cmds.select(self.old_selection)  # On restaure la sélection précédente

        
# Cas d'utilisation
with RestoreSelection() as rs:
    # Fait plein de chose qui change la sélection

# Ma sélection est restaurée!

# Notez ici, que la version classe permet plus de chose, on peut par exemple faire:
rs.old_selection
# pour récupérer au sein du context la sélection au démarrage alors que ce n'est pas 
# possible via le package contextlib.
```

Ça y est! Vous savez tout ce qu'il y a savoir sur les context manager en python.
Je vous recommande de fabriquer vos context manager via des classes plutôt que via le package contextlib.
C'est plus flexible et plus facile à maintenir.
