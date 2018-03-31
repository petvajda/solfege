import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../solfege')))
from solfege import Note

class TestNotes(unittest.TestCase):
    
    def test_add_notes_sharp(self):
        self.assertEqual(str(Note("C") + 1), "C#")
        self.assertEqual(str(Note("C") + 2), "D")
        self.assertEqual(str(Note("C") + 3), "D#")
        self.assertEqual(str(Note("C") + 4), "E")
        self.assertEqual(str(Note("C") + 5), "F")
        self.assertEqual(str(Note("C") + 6), "F#")
        self.assertEqual(str(Note("C") + 7), "G")
        self.assertEqual(str(Note("C") + 11), "B")
        self.assertEqual(str(Note("C") + 12), "C")

    def test_add_notes_flat(self):
        self.assertEqual(str(Note("C", False) + 1), "Db")
        self.assertEqual(str(Note("C"       ) + 2), "D")
        self.assertEqual(str(Note("C", False) + 3), "Eb")
        self.assertEqual(str(Note("C",      ) + 4), "E")
        self.assertEqual(str(Note("C",      ) + 5), "F")
        self.assertEqual(str(Note("C", False) + 6), "Gb")
        self.assertEqual(str(Note("C",      ) + 7), "G")
        self.assertEqual(str(Note("C",      ) + 11), "B")
        self.assertEqual(str(Note("C",      ) + 12), "C")
        
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

    def test_whole_up(self):
        self.assertEqual(str(Note("C"        ).w_up()), "D")
        self.assertEqual(str(Note("C#"       ).w_up()), "D#")
        self.assertEqual(str(Note("D"        ).w_up()), "E")
        self.assertEqual(str(Note("D#"       ).w_up()), "F")
        self.assertEqual(str(Note("E"        ).w_up()), "F#")
        self.assertEqual(str(Note("B"        ).w_up()), "C#")
        self.assertEqual(str(Note("Cb", False).w_up()), "Db")
        self.assertEqual(str(Note("Eb", False).w_up()), "F")
        self.assertEqual(str(Note("Bb", False).w_up()), "C")
        self.assertEqual(str(Note("B"        ).w_up()), "C#")

    def test_whole_down(self):
        self.assertEqual(str(Note("C",       ).w_down()), "A#")
        self.assertEqual(str(Note("D"        ).w_down()), "C")
        self.assertEqual(str(Note("Db", False).w_down()), "Cb")
        self.assertEqual(str(Note("F",  False).w_down()), "Eb")

    def test_half_up(self):        
        self.assertEqual(str(Note("C"        ).h_up()), "C#")
        self.assertEqual(str(Note("C#"       ).h_up()), "D")
        self.assertEqual(str(Note("D#"       ).h_up()), "E")
        self.assertEqual(str(Note("G"        ).h_up()), "G#") 
        self.assertEqual(str(Note("Cb", False).h_up()), "C")
        self.assertEqual(str(Note("Db", False).h_up()), "D")
        self.assertEqual(str(Note("Eb", False).h_up()), "E")
                
    def test_half_down(self):        
        self.assertEqual(str(Note("C#"       ).h_down()), "C")
        self.assertEqual(str(Note("D#"       ).h_down()), "D")
        self.assertEqual(str(Note("D"        ).h_down()), "C#")
        self.assertEqual(str(Note("E"        ).h_down()), "D#")
        self.assertEqual(str(Note("Eb", False).h_down()), "D")

if __name__ == '__main__':
    unittest.main()
