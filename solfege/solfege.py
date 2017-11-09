import random
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
        
def test_exercise():
    exercise(PENTATON)
    exercise(MODES)
    
if __name__ == '__main__':
    test_exercise()
