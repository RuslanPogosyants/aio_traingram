import unittest
from unittest.mock import patch

from project.database.models import User

class TestUserMethods(unittest.TestCase):

    @patch('session.query')
    def test_user_exist(self, mock_query):
        test_user = User()
        mock_query.return_value.filter_by.return_value.first.return_value = test_user
        self.assertTrue(User.user_exist(1))

    @patch('session.add')
    @patch('session.commit')
    def test_create_user(self, mock_add, mock_commit):
        User.create_user(1)
        mock_add.assert_called_once()
        mock_commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
