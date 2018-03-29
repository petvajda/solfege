# solfege
Solfege Library in Python. Supporting Note and Scale creation. Just pass a base Note and the library can tell all the notes in a major scale and modes (I-VII).

[More Info on Scale and Modes](https://en.wikipedia.org/wiki/Mode_(music))


Example C Major Scale and D Dorian:

```python
from solfege import Scale

cmaj=Scale("C")
str(cmaj)
'C D E F G A B'
cmaj.name
'Ionian'
emaj=Scale("E")
str(emaj)
'E F# G# A B C# D#'

cdor=Scale("C", 2)
str(cdor)
'C D Eb F G A Bb'
cdor.roman
'II'
```

Also basic interval support (more will come later):
```python
from solfege import Note

Note("C#").w_up()
'D#'
```

Some useful scripts for example generating random key and modes to play on your instrument:

```python3 solfege/gen_exercise.py
D [2, 5, 1, 6, 3]
C# [6, 3, 7, 2, 5, 1, 4]
```