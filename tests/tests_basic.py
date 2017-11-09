import unittest

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
                
if __name__ == '__main__':
    #test_exercise()
    unittest.main()
