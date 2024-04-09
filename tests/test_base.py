import unittest
from project.database.base import get_session, close_session
from unittest.mock import patch
from sqlalchemy.orm import Session


class TestDatabaseFunctions(unittest.TestCase):

    @patch('project.database.base.create_engine')
    def test_get_session(self, mock_create_engine):
        session = get_session()
        self.assertIsInstance(session, Session)

    @patch('project.database.base.session')
    def test_close_session(self, mock_session):
        close_session()
        mock_session.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
