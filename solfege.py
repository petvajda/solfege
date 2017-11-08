import random
import unittest
from numpy import roll
#############
### NOTES ###
#############
NOTES_NORMAL = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
NOTES_SHARP  = list(map(lambda x: x+'#', NOTES_NORMAL))
NOTES_FLAT   = list(map(lambda x: x+'b', NOTES_NORMAL))
ALL_NOTES    = NOTES_NORMAL + NOTES_SHARP + NOTES_FLAT

######################
### PENTATON MODES ###
######################
PENTATON = [1, 2, 3, 5, 6]

####################
### SCALES MODES ###
####################
MODES = [1, 2, 3, 4, 5, 6, 7]

######################
### NAMES OF MODES ###
######################
NAMES_MODES = {}
NAMES_MODES["I"]   = "Ionian"
NAMES_MODES["II"]  = "Dorian"
NAMES_MODES["III"] = "Phrygian"
NAMES_MODES["IV"]  = "Lydian"
NAMES_MODES["V"]   = "Mixolydian"
NAMES_MODES["VI"]  = "Aeolian"
NAMES_MODES["VII"] = "Locrian"

def check_order(list):
    for i in range(len(list)-1):
        if abs(list[i] - list[i+1]) <= 2:
            return True
    return False

def rand_mode(modes):
    while check_order(modes):    
        a = random.randrange(len(modes)-1)
        modes[a], modes[a+1] = modes[a+1], modes[a]
        # print('{0} {1} {2}'.format(a, a+1, modes))
    return modes

def exercise(modes):
    print(ALL_NOTES[random.randrange(len(ALL_NOTES))], end=' ')
    print(rand_mode(modes))

class Note:    
    __reference_sharps  = [ "C", "C#", "D", "D#", "E", "F", "F#",
                            "G", "G#", "A", "A#", "B"]
    __reference_flats   = [ "Cb", "C", "Db", "D", "Eb", "E", "F",
                            "Gb", "G", "Ab", "A", "Bb", "B"]
    
    def __init__(self, note):
        note = note.capitalize()
        self.flat = self.sharp = False
        if note in self.__reference_sharps:
            self.note  = note
            self.sharp = True
        elif note in self.__reference_flats:
            self.note  = note
            self.flat = True
        else:
            raise Exception("Not a valid base Note: %s" % note)
    
    def __str__(self):
        return self.note
            
    def __add__(self, a):
        i = self.__reference_sharps.index(self.note)
        return Note(self.__reference_sharps[(i + a) % len(self.__reference_sharps)])

    def __sub__(self, a):
        i = self.__reference_sharps.index(self.note)
        return Note(self.__reference_sharps[i - a])            

class Scale:
    __distances = [2, 2, 1, 2, 2, 2, 1]

    def __init__(self, base, mode):
        self.base     = Note(base)
        self.type     = type
        self.notes    = [self.base, ]
        i = 1
        for d in roll(self.__distances, -1*mode+1):
            self.notes.append(self.notes[i-1] + d)
            i = i + 1    

    def __str__(self):
        return " ".join(str(n) for n in self.notes)

class TestNotes(unittest.TestCase):
    
    def test_add_notes(self):
        self.assertEqual(str(Note("C") + 1), "C#")
        self.assertEqual(str(Note("C") + 2), "D")
        self.assertEqual(str(Note("C") + 4), "E")
        self.assertEqual(str(Note("C") + 7), "G")
        self.assertEqual(str(Note("C") + 11), "B")
        self.assertEqual(str(Note("C") + 12), "C")
        
    def test_sub_notes(self):
        self.assertEqual(str(Note("D") - 1), "C#")
        self.assertEqual(str(Note("D") - 2), "C")
        self.assertEqual(str(Note("B") - 2), "A")
        self.assertEqual(str(Note("G") - 2), "F")
    
    def test_bounderies(self):
        self.assertEqual(str(Note("C") - 1), "B")
        self.assertEqual(str(Note("C") - 2), "A#")
        self.assertEqual(str(Note("C") - 3), "A")
        self.assertEqual(str(Note("D") - 3), "B")
        self.assertEqual(str(Note("E") - 9), "G")

class TestScales(unittest.TestCase):
        
    def test_Ionian_scales(self):
        self.assertEqual(str(Scale("C", 1)), "C D E F G A B C")
        self.assertEqual(str(Scale("G", 1)), "G A B C D E F# G")
        self.assertEqual(str(Scale("D", 1)), "D E F# G A B C# D")
        self.assertEqual(str(Scale("A", 1)), "A B C# D E F# G# A")
        self.assertEqual(str(Scale("E", 1)), "E F# G# A B C# D# E")
        self.assertEqual(str(Scale("B", 1)), "B C# D# E F# G# A# B")
        
    def test_Dorian_scales(self):
        self.assertEqual(str(Scale("D", 2)), "D E F G A B C D")
        self.assertEqual(str(Scale("A", 2)), "A B C D E F# G A")
        
    def test_Phrygian_scales(self):
        self.assertEqual(str(Scale("E",  3)), "E F G A B C D E")
        self.assertEqual(str(Scale("F#", 3)), "F# G A B C# D E F#")
        
    def test_Lydian_scales(self):
        self.assertEqual(str(Scale("F", 4)), "F G A B C D E F")
        self.assertEqual(str(Scale("C", 4)), "C D E F# G A B C")

    def test_Mixolydian_scales(self):
        self.assertEqual(str(Scale("G", 5)), "G A B C D E F G")
        self.assertEqual(str(Scale("D", 5)), "D E F# G A B C D")

    def test_Aeolian_scales(self):
        self.assertEqual(str(Scale("A", 6)), "A B C D E F G A")
        self.assertEqual(str(Scale("E", 6)), "E F# G A B C D E")

    def test_Locrian_scales(self):
        self.assertEqual(str(Scale("B",  7)), "B C D E F G A B")
        self.assertEqual(str(Scale("C#", 7)), "C# D E F# G A B C#")
        
def test_exercise():
    exercise(PENTATON)
    exercise(MODES)
    
if __name__ == '__main__':
    #test_exercise()
    unittest.main()
