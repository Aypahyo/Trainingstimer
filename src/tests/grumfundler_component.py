import unittest

from trainingstimer_core import grumfundler

class GrumfundlerTest(unittest.TestCase):

    def test_grumfndler_str(self):
        #All development tests that are not driven by illities or business value and are not unit tests are component tests.
        #Usually that includes the integration of several units and may or may not be running against mocked dependencies.
        gf = grumfundler.Grumfundler("Hello World!")
        self.assertEqual(str(gf), "Grumfundler: Hello World!")
