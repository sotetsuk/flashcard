import unittest

from flashcard.sources import fetch_google_spreadsheet, _parse_google_spreadsheet, _generate_downloadable_url


class TestParseGoogleSpreadsheet(unittest.TestCase):

    def test_get_id_and_gid(self):
        # without gid
        url = "https://docs.google.com/spreadsheets/d/2X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g/edit?usp=sharing"
        parsed_id, parsed_gid = _parse_google_spreadsheet(url)
        expected_id, expected_gid = "2X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g", None

        self.assertEqual(expected_id, parsed_id)
        self.assertIs(expected_gid, parsed_gid)

        # with gid
        url = "https://docs.google.com/spreadsheets/d/2bHXt4ZY0S54RU6EeT7eHGh_KAI7ncdn96KSh-Hx0xGo/edit#gid=742930534"
        parsed_id, parsed_gid = _parse_google_spreadsheet(url)
        expected_id, expected_gid = "2bHXt4ZY0S54RU6EeT7eHGh_KAI7ncdn96KSh-Hx0xGo", "742930534"

        self.assertEqual(expected_id, parsed_id)
        self.assertEqual(expected_gid, parsed_gid)

        # with blank gid
        url = "https://docs.google.com/spreadsheets/d/2bHXt4ZY0S54RU6EeT7eHGh_KAI7ncdn96KSh-Hx0xGo/edit#gid="
        parsed_id, parsed_gid = _parse_google_spreadsheet(url)
        expected_id, expected_gid = "2bHXt4ZY0S54RU6EeT7eHGh_KAI7ncdn96KSh-Hx0xGo", ""

        self.assertEqual(expected_id, parsed_id)
        self.assertEqual(expected_gid, parsed_gid)


class TestGenerateDownloadableUrl(unittest.TestCase):

    def test_url(self):
        # tsv
        _id, gid = "2X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g", None
        parsed = _generate_downloadable_url(_id, gid)
        expected = "https://docs.google.com/spreadsheets/d/2X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g/export?gid=0&format=tsv"

        self.assertEqual(expected, parsed)

        # csv
        parsed = _generate_downloadable_url(_id, gid, "csv")
        expected = "https://docs.google.com/spreadsheets/d/2X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g/export?gid=0&format=csv"

        self.assertEqual(expected, parsed)

        # with gid
        gid = "742930534"
        parsed = _generate_downloadable_url(_id, gid)
        expected = "https://docs.google.com/spreadsheets/d/2X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g/export?gid=742930534&format=tsv"

        self.assertEqual(expected, parsed)

        # with blank gid
        gid = ""
        parsed = _generate_downloadable_url(_id, gid)
        expected = "https://docs.google.com/spreadsheets/d/2X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g/export?gid=0&format=tsv"

        self.assertEqual(expected, parsed)


class TestFetchGoogleSpreadsheet(unittest.TestCase):

    def test_(self):
        url = "https://docs.google.com/spreadsheets/d/1X1uW_ZxgwZWh9elAI1jJCYkiCbmDL-xH2zkCMEZEV4g/edit#gid=0"
        flashcard = fetch_google_spreadsheet(url)
        expected = [['最初のカード', 'Initial card'],
                    ['二番目のカード', '2nd card'],
                    ['三番目のカード', '3rd card']]

        self.assertListEqual(expected, flashcard)

if __name__ == '__main__':
    unittest.main()
