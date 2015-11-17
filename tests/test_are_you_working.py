from unittest import TestCase

import python_project_example

class TestWorking(TestCase):

    def test_is_string(self):
        answer = python_project_example.are_you_working()
        self.assertTrue(isinstance(answer, basestring))
