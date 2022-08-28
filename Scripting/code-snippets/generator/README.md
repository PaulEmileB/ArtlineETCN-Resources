# Code-snippets
Ce dossier contient quelques exemples de code Python commenté pour illustrer différentes fonctionnalités du langage.


## Générateur
Il s'agit d'une fonctionnalité essentielle de Python que l'on retrouve aussi dans d'autres langages (itérateurs en C++ par exemple).
L'idée du générateur, c'est de pouvoir justement générer des éléments au fur et à mesure de leur utilisation.

Imaginez par exemple, une usine qui fabrique des cartons.
Pour faire un carton, nous avons besoin du carton à proprement parlé (cardboard) et de ruban adhésif (tape).
On utilise ces 2 ressources pour assembler une boite (box).
En python, cela se traduire par 3 fonctions: `build_carboard`, `build_tape` et `assemble_box`

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
soient épuisés:

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

J'espère qu'avec cet exemple, vous arriverez à mieux comprendre l'intérêt des générateurs.

Vous retrouverez quelques exmeples de générateurs dans les code snippets fournits.
