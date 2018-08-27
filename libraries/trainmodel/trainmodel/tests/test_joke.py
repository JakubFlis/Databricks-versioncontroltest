from unittest import TestCase

import trainmodel

class TestJoke(TestCase):
    def test_is_string(self):
        s = trainmodel.train_model()
        self.assertTrue(isinstance(s, basestring))
