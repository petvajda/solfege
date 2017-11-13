from numpy import roll

NAMES_MODES      = {}
NAMES_MODES[0]   = ["I",   "Ionian"]
NAMES_MODES[1]   = ["II",  "Dorian"]
NAMES_MODES[2]   = ["III", "Phrygian"]
NAMES_MODES[3]   = ["IV",  "Lydian"]
NAMES_MODES[4]   = ["V",   "Mixolydian"]
NAMES_MODES[5]   = ["VI",  "Aeolian"]
NAMES_MODES[6]   = ["VII", "Locrian"]

class Note:    
    __chromatic_sharps  = [ "C", "C#", "D", "D#", "E", "F", "F#",
                            "G", "G#", "A", "A#", "B"]
    __chromatic_flats   = [ "C",  "Db", "D",  "Eb", "E",  "F",
                            "Gb", "G",  "Ab", "A",  "Bb", "B"]
                                
    def __init__(self, note, use_sharp=True):
        self.use_sharp = use_sharp
        note = note.capitalize()
        if note in self.__chromatic_sharps or self.__chromatic_flats:
            self.note  = note
        else:
            raise Exception("Not supported base Note: %s" % note)

        self.__chromatic = self.__chromatic_sharps if use_sharp else self.__chromatic_flats
        
    def __str__(self):
        return self.note
            
    def __add__(self, a):
        i = self.__chromatic.index(self.note)
        return Note(self.__chromatic[(i + a) % len(self.__chromatic)], self.use_sharp)

    def __sub__(self, a):
        i = self.__chromatic.index(self.note)
        return Note(self.__chromatic[(i - a) % len(self.__chromatic)], self.use_sharp)

class Scale:
    __ionian_distances   = [2, 2, 1, 2, 2, 2, 1]
    __sharp_keys         = ["C",  "G",  "D",  "A",  "E",  "B", "F#", "C#",
                            "G#", "D#", "A#", "E#", "B#"]
    __flat_keys          = ["F",  "Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"]
    __mode_to_half_steps = [2, 4, 5, 7, 9, 11, 12]

    def __init__(self, base, mode):
        major_base=base.capitalize()
        self.sharp = self.flat = False
        if mode == 2:
            major_base = str(Note(major_base, False) - self.__mode_to_half_steps[mode-2])

        if major_base in self.__sharp_keys:
            self.sharp = True
        elif major_base in self.__flat_keys:
            self.flat = True
        else:
            raise Exception("Not supported base Note for a Scale: %s" % base)
        
        self.base     = Note(base, self.sharp)
        self.type     = type
        self.notes    = [self.base, ]
        i = 1
        for d in roll(self.__ionian_distances, -1*mode+1):
            self.notes.append(self.notes[i-1] + d)
            i = i + 1
        
        self.name_roman = NAMES_MODES[mode-1][0]
        self.name       = NAMES_MODES[mode-1][1]

    def __str__(self):
        return " ".join(str(n) for n in self.notes)
    