from django.test import TestCase

class TestSimpleApp:
    def test_one(self):
        x = "my simple app test"
        assert 'simple app' in x
