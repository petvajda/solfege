# solfege
Solfege Library in Python. Supporting Note and Scale creation. Based on base Note can tell all the notes in a major and scale and modes (I-VII).

[More Info on Scale and Modes](https://en.wikipedia.org/wiki/Mode_(music))

Example C Major Scale and D Dorian:
```python
from solfege import Scale

cmaj=Scale("C", 1)
str(cmaj)
'C D E F G A B C'
cmaj.name
'Ionian'

ddorain=Scale("D", 2)
str(ddorain)
'D E F G A B C D'
ddorain.roman
'II'
```
