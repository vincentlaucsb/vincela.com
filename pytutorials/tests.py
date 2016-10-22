from django.test import TestCase
from pytutorials.views import tutorial_menu

class print_status(TestCase):
    def test_dummy(self):
        print("\nRunning tutorials tests\n")

# Note to future self:
# * Use dot notation when referring to subdirectories in pytutorials for tutorial_menu() function
        
# Check if tutorial_menu() works properly
class tutorial_menu_error_handling(TestCase):
    # Make sure a useful error message occurs when contents.py can't be imported
    def test_missing_contents_py(self):
        with self.assertRaises(FileNotFoundError):
            self.assertRaises(ImportError,tutorial_menu("test_files.missing_contents"))
    
    # Check that mislabelled files in contents.py raises a FileNotFoundError
    def test_mislabelled_contents(self):
        with self.assertRaises(FileNotFoundError):
            tutorial_menu("test_files.mislabelled_contents")
    
    # Make sure errors in contents.py are handled properly
    def test_contents_error(self):
        with self.assertRaises(AttributeError):
            tutorial_menu("test_files.contents_error")

# Ensure intended functionality works
class tutorial_menu_basic(TestCase):
    def setUp(self):
        self.menu = tutorial_menu('test_files.basic')
        
    # Make sure items are listed in the correct order
    def test_order(self):
        # Cycle through keys
        i = 0
        for key in self.menu:
            if i == 0: self.assertEqual(key,'Test 1')
            if i == 1: self.assertEqual(key,'Test 2')
            
            # This step also makes sure missing title handling works properly
            if i == 2: self.assertEqual(key,'test3.html')
            i += 1
    
    # Make sure correct template is being specified
    # Also a test of get_title()
    def test_template(self):
        self.assertEqual(self.menu['Test 1']['template'],'test_files/basic/test1.html')

    # Make sure description is being read off correctly
    # Also a test of get_description()
    def test_description(self):
        self.assertEqual(self.menu['Test 1']['description'],'A basic description')
    
    # Makes sure missing descriptions result in an empty string
    def test_no_description(self):
        self.assertEqual(self.menu['test3.html']['description'],'')
    
if __name__ == '__main__':
    unittest.main()
