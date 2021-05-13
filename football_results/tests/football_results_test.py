import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):

    def setUp(self):
        self.final_scores = [
            {"home_score": 0, "away_score": 1},
            {"home_score": 1, "away_score": 0},
            {"home_score": 1, "away_score": 1}   
        ]
    
    def test_greater_away_score_returns__away_win(self):
        self.assertEqual("Away win", get_result(self.final_scores[0]))

    def test_greater_home_score_returns__home_win(self):
        self.assertEqual("Home win", get_result(self.final_scores[1]))

    def test_equal_scores_returns__draw(self):
        self.assertEqual("Draw", get_result(self.final_scores[2]))

    def test_get_results__returns_list_of_results(self):
        self.assertEqual(3, len(get_results(self.final_scores)))
    



    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
