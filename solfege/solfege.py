from numpy import roll

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
    