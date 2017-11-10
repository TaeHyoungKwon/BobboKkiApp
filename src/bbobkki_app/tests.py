# -*- coding: utf-8 -*-

"""
docstring
"""

from django.test import TestCase
from .models import GuessNumbers

class GuessNumbersTestCase(TestCase):
    """
    docstring for class
    """

    def test_generate(self):
        """
        method docstring
        """
        g = GuessNumbers(name="apple", text="pineapple")
        g.generate()
        print(g.update_date)
        print(g.lottos)
        self.assertTrue(len(g.lottos) > 20)