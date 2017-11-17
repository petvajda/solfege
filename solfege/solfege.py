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
    __base_notes            = ["C", "D", "E", "F", "G", "A", "B"]
    __sharp_keys            = ["G",  "D",  "A",  "E",  "B", "F#", "C#",
                               "G#", "D#", "A#", "E#", "B#"]
    __flat_keys             = ["F",  "Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"]

    def __init__(self, base, mode=1):
        self.roman = NAMES_MODES[mode-1][0]
        self.name  = NAMES_MODES[mode-1][1]
        self.sharp = self.flat = False
        base = base.capitalize()
        if mode > 1:
            base = self.__base_notes[self.__base_notes.index(base[:1])-mode+1]
            if base=="B": base=base+"b" # FIXIT
        if base == "C":
            self.notes = self.__base_notes
        else:
            if base in self.__sharp_keys:
                self.sharp = True
                num_of_mod = self.__sharp_keys.index(base)
                modfied_notes = self.__sharp_keys[5:6+num_of_mod]
            elif base in self.__flat_keys:
                self.flat = True
                num_of_mod=self.__flat_keys.index(base)
                modfied_notes = self.__flat_keys[1:2+num_of_mod]
            else:
                raise Exception("Not supported base Note for a Scale: %s" % base)

            self.base      = Note(base)
            self.notes     = roll(self.__base_notes, len(self.__base_notes) -
                                 self.__base_notes.index(base[:1])).tolist()
            for n in modfied_notes:
                self.notes[self.notes.index(n[:1])] = n
            
        if mode > 1:
            self.notes = roll(self.notes, -1*mode+1).tolist()

    def __str__(self):
        return " ".join(str(n) for n in self.notes)
    
    def vextab(self, i=2):
        vt_pre = """tabstave clef=treble notation=true tablature=false time=4/4
notes """
        notes_str =  "-".join(str(n) for n in self.notes[:i]) + "/4"
        notes_str += "-".join(str(n) for n in self.notes[i:]) + "/5"
        return vt_pre + notes_str