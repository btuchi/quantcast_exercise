import unittest
from cookie_log_parser import CookieLogParser

class TestCookieLogParser(unittest.TestCase):

    # single most active cookie on the day
    def test_find_most_active_cookies_single_result(self):
        parser = CookieLogParser('test_log.csv')
        self.assertEqual(parser.find_most_active_cookies('2018-12-09'), ['AtY0laUfhglK3lC7'])

    # multiple most active cookies on the day
    def test_find_most_active_cookies_multiple_results(self):
        parser = CookieLogParser('test_log.csv')
        expected_cookies = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']  # Replace with actual expected cookies
        self.assertEqual(sorted(parser.find_most_active_cookies('2018-12-08')), sorted(expected_cookies))

    # no active cookie on the day
    def test_no_activity_day(self):
        parser = CookieLogParser('test_log.csv')
        self.assertEqual(parser.find_most_active_cookies('2018-12-01'), [])

    # no cookie record
    def test_empty_log_file(self):
        parser = CookieLogParser('empty_log.csv')
        self.assertEqual(parser.find_most_active_cookies('2018-12-09'), [])

if __name__ == '__main__':
    unittest.main()
