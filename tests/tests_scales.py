import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../solfege')))
from solfege import Scale

class TestScales(unittest.TestCase):
        
    def test_Ionian_scales_sharps(self):
        self.assertEqual(str(Scale("C")), "C D E F G A B")
        self.assertEqual(str(Scale("G")), "G A B C D E F#")
        self.assertEqual(str(Scale("D")), "D E F# G A B C#")
        self.assertEqual(str(Scale("A")), "A B C# D E F# G#")
        self.assertEqual(str(Scale("E")), "E F# G# A B C# D#")
        self.assertEqual(str(Scale("B")), "B C# D# E F# G# A#")

    def test_Ionian_scales_flats(self):
        self.assertEqual(str(Scale("F")),  "F G A Bb C D E")
        self.assertEqual(str(Scale("Bb")), "Bb C D Eb F G A")
        self.assertEqual(str(Scale("Eb")), "Eb F G Ab Bb C D")
        self.assertEqual(str(Scale("Ab")), "Ab Bb C Db Eb F G")
                
    def test_Dorian_scales_sharps(self):
        self.assertEqual(str(Scale("D", 2)),  "D E F G A B C")
        self.assertEqual(str(Scale("A", 2)),  "A B C D E F# G")
#        self.assertEqual(str(Scale("C#", 2)), "B C# D E F# G# A B")

    def test_Dorian_scales_flats(self):
        self.assertEqual(str(Scale("G", 2)), "G A Bb C D E F")
        self.assertEqual(str(Scale("C", 2)), "C D Eb F G A Bb")
        
    def test_Phrygian_scales_sharps(self):
        self.assertEqual(str(Scale("E",  3)), "E F G A B C D")
        self.assertEqual(str(Scale("F#", 3)), "F# G A B C# D E")

    def test_Phrygian_scales_flats(self):
        self.assertEqual(str(Scale("A", 3)), "A Bb C D E F G")
        self.assertEqual(str(Scale("D", 3)), "D Eb F G A Bb C")
        
    def test_Lydian_scales(self):
        self.assertEqual(str(Scale("F", 4)), "F G A B C D E")
        self.assertEqual(str(Scale("C", 4)), "C D E F# G A B")

    def test_Mixolydian_scales(self):
        self.assertEqual(str(Scale("G", 5)), "G A B C D E F")
        self.assertEqual(str(Scale("D", 5)), "D E F# G A B C")

    def test_Aeolian_scales(self):
        self.assertEqual(str(Scale("A", 6)), "A B C D E F G")
        self.assertEqual(str(Scale("E", 6)), "E F# G A B C D")

    def test_Locrian_scales(self):
        self.assertEqual(str(Scale("B",  7)), "B C D E F G A")
        self.assertEqual(str(Scale("C#", 7)), "C# D E F# G A B")

    def test_flat_keys_flag(self):
        self.assertTrue(Scale("F").flat)
        self.assertFalse(Scale("F").sharp)

    def test_sharp_keys_flag(self):
        self.assertTrue(Scale("E").sharp)
        self.assertFalse(Scale("E").flat)
    
    def test_scale_names(self):
        self.assertEqual(Scale("C").name, "Ionian")
        self.assertEqual(Scale("G",  2).name, "Dorian")
        self.assertEqual(Scale("Bb", 3).name, "Phrygian")
        self.assertEqual(Scale("B",  7).name, "Locrian")        

    def test_scale_names_roman(self):
        self.assertEqual(Scale("C").roman,  "I")
        self.assertEqual(Scale("G", 2).roman,  "II")
        self.assertEqual(Scale("Bb", 3).roman, "III")
        self.assertEqual(Scale("B", 7).roman,  "VII")

if __name__ == '__main__':
    unittest.main()
