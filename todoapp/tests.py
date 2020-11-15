from django.test import TestCase
from .models import TodoModel

# Create your tests here.

class TodoModelTestCase(TestCase):
	def setUp(self):
		TodoModel.objects.create(
					title="I will eat beef",
					memo="I want to eat beef",
					priority="high",
					duedate="2020-11-23")

class MathTestCase(TestCase):
	def test_bad_maths(self):
		self.assertEqual(1+1, 3)