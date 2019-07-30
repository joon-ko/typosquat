import unittest

from typosquat import domain

class TestDomain(unittest.TestCase):
	def test_google_domain_is_taken(self):
		domain_name = 'google.com'
		expected = (False, None)
		actual = domain.get_domain_information(domain_name)
		self.assertEqual(expected, actual)

	def test_invalid_domain_is_available(self):
		domain_name = 'wmsufieoe3942c.com'
		expected = True
		actual = domain.get_domain_information(domain_name)[0]
		self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
