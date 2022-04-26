import unittest
import requests


TARGET_API = "https://breakingbadapi.com/api/"
HTTP_OK = 200
TOTAL_CHARACTERS = 62

class TestMyAPI(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_fetch_all_characters(self):
        response = requests.get(f'{TARGET_API}characters')
        self.assertEqual( HTTP_OK, response.status_code)
        self.assertEqual(len(response.json()), TOTAL_CHARACTERS, f'Failed: expecting {TOTAL_CHARACTERS} characters!')

    def test_fetch_all_character_one(self):
        response = requests.get(f'{TARGET_API}characters/1')
        self.assertEqual(HTTP_OK, response.status_code)
        data = response.json()
        self.assertEqual(len(data),1)
        self.assertEqual(data[0]['char_id'],1)
        self.assertEqual(data[0]['name'], "Walter White")
        print(response.json())

    def test_fetch_all_auotes_from_a_series(self):
        response = requests.get(f'{TARGET_API}quotes?series=Better+Call+Saul')
        self.assertEqual(HTTP_OK, response.status_code)
        # print(response.json())
        self.assertEqual(
            len(response.json()),
            18,
            'Failed: expecting 18 quotes from Better Call Saul series!'
        )

    def tearDown(self) -> None:
        pass


if __name__=='__main__':
    unittest.main()