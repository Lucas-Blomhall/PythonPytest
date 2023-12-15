import math
import pytest
import source.shapes as shapes


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")

    def teardown_method(self, method):
        print(f"tearing down {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_one(self):
        assert True

    def test_two(self):
        assert True
