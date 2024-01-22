import unittest

from trainingstimer_core import grumfundler

class GrumfundlerTest(unittest.TestCase):

    def test_grumfndler_str(self):
        #All development tests that test a single unit of code are unit tests.
        #Usually that includes mocking dependencies.
        gf = grumfundler.Grumfundler("Hello World!")
        self.assertEqual(str(gf), "Grumfundler: Hello World!")
