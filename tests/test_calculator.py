from unittest import TestCase, main
from calculator.settings import CALCULATOR_TITLE  # type: ignore

class TestHello(TestCase):

	def setUp(self) -> None:
		pass

	def tearDown(self) -> None:
		pass

	def test_is_instance(self):
		"Test function calculator"
		EXPECTED = 'GUI Calculator'

		self.assertEqual(EXPECTED, CALCULATOR_TITLE)

if __name__ == '__main__':
    main()