import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../solfege')))
from solfege import Note

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
                
if __name__ == '__main__':
    unittest.main()
