import unittest
from unittest.mock import Mock
from flask import Flask, render_template, request, session, redirect
from main import hello_world, login_check
from Tweet_Extract import Tweet_manager


##where unit test reside
class MockDatabase:

    def execute_query(self, query, params=None):
        # Implement a mock method to return fake data for testing
        if query == "SELECT t.fecha, t.text, u.nickname, t.hora, t.id FROM tweet AS t JOIN user AS u ON t.author = u.userid ORDER BY fecha ASC, hora ASC;":
            # Return a list of tuples simulating the database result
            return [('2022-01-01', 'Tweet 1', 'User 1', '12:00', 1), ('2022-01-02', 'Tweet 2', 'User 2', '13:00', 2)]
        elif query == "SELECT c.fecha, c.text, u.nickname, c.hora FROM comment AS c JOIN user AS u ON c.userid = u.userid WHERE c.id_tweet = %s ORDER BY fecha DESC, hora DESC;":
            # Return a list of tuples simulating the comment database result
            return [('2022-01-01', 'Comment 1', 'User 3', '14:00'), ('2022-01-02', 'Comment 2', 'User 4', '15:00')]
        else:
            return None

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.secret_key = 'test_secret_key'
        self.client = self.app.test_client()
        self.tweet_manager = Tweet_manager
        self.mock_db = Mock()
        self.tweet_manager.db = self.mock_db

    def test_hello_world(self):
        with self.app.test_request_context('/'):
            response = hello_world()
            self.assertEqual(response, render_template('Home.html'))

    def test_login_check_success(self):
        with self.app.test_request_context('/login', method='POST',
                                           data={'username': 'admin', 'password': 'password'}):
            response = login_check()
            self.assertEqual(response.status_code, 302)
            self.assertEqual(session['user'], {'username': 'admin', 'password': 'password'})
            self.assertEqual(response.location, 'http://localhost/board')

    def test_login_check_failure(self):
        with self.app.test_request_context('/login', method='POST',
                                           data={'username': 'invalid', 'password': 'wrong'}):
            response = login_check()
            self.assertEqual(response, b'error')

    def test_get_tweets(self):
        # Set up mock data for the execute_query method
        mock_data = [
            ('2023-06-01', 'Tweet 1', 'user1', '10:00', 1),
            ('2023-06-02', 'Tweet 2', 'user2', '12:00', 2)
        ]
        self.mock_db.execute_query.return_value = mock_data

        # Set up mock data for the second query within the loop
        mock_comment_data = [
            ('2023-06-01', 'Comment 1', 'user3', '11:00'),
            ('2023-06-01', 'Comment 2', 'user4', '11:30')
        ]
        self.mock_db.execute_query.side_effect = [
            mock_comment_data,  # First call to execute_query for comment data
            None  # Second call to execute_query for tweet without comments
        ]

        # Call the method being tested
        result = self.tweet_manager.get_Tweets()

        # Assert that the mock database method was called with the correct query
        self.mock_db.execute_query.assert_called_with("""
            SELECT t.fecha, t.text, u.nickname, t.hora,t.id
            FROM tweet AS t
            JOIN user AS u ON t.author = u.userid
            ORDER BY fecha ASC, hora ASC;
        """)

        # Assert the expected behavior of the method
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].author, 'user1')
        self.assertEqual(result[0].text, 'Tweet 1')
        self.assertEqual(result[0].timestamp, '2023-06-01')
        self.assertEqual(result[0].hour, '10:00')
        self.assertEqual(result[0].comments, [
            ('2023-06-01', 'Comment 1', 'user3', '11:00'),
            ('2023-06-01', 'Comment 2', 'user4', '11:30')
        ])
        self.assertEqual(result[1].author, 'user2')
        self.assertEqual(result[1].text, 'Tweet 2')
        self.assertEqual(result[1].timestamp, '2023-06-02')
        self.assertEqual(result[1].hour, '12:00')
        self.assertEqual(result[1].comments, [])
if __name__ == '__main__':
    unittest.main()
