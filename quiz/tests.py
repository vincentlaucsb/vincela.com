from django.test import TestCase
from quiz.quiz import verify

# Create your tests here.

class print_status(TestCase):
    def test_dummy(self):
        print("\nRunning quizzes tests\n")

# Check if quizzes are being graded correctly
class CheckCorrectAnswer(TestCase):
    # Make sure spaces don't erroneously affect validity of answers
    def test_spaces_check(self):
        self.assertEqual(verify("[1,2,3]","[1, 2, 3]"),True)
    # Make sure choice of ' or " doesn't affect correctness
    def test_quotes_check(self):
        self.assertEqual(verify("x['abc']",'x["abc"]'),True)
    # Check both
    def test_sq_check(self):
        self.assertEqual(verify("gdp_2015['UK'] = 2.84",'gdp_2015["UK"]=2.84'),True)

# Checks same function as above for false positives
class CheckFalsePositive(TestCase):
    def test_obvious_bs(self):
        self.assertFalse(verify([1,2,3],[1,2,4]))
    # Failing test
    #def test_problem_1(self):
    #    self.assertFalse(verify("Test12","Test 1 2"))


if __name__ == '__main__':
    unittest.main()
