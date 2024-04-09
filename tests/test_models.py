import unittest
from unittest.mock import patch

from project.database.models import User

class TestUserMethods(unittest.TestCase):

    @patch('project.database.models.session.query')
    def test_user_exist(self, mock_query):
        test_user = User()
        mock_query.return_value.filter_by.return_value.first.return_value = test_user
        self.assertTrue(User.user_exist(1))

    @patch('project.database.models.session.add')
    @patch('project.database.models.session.commit')
    def test_create_user(self, mock_add, mock_commit):
        User.create_user(1)
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

    @patch('project.database.models.session.query')
    def test_delete_user(self, mock_query):
        # Предположим, что пользователь с id=1 существует
        mock_query.return_value.filter_by.return_value.first.return_value = User(id=1)

        result = User.delete_user(1)
        self.assertEqual(result, 'Ваш аккаунт был удален!')

    @patch('project.database.models.session.query')
    def test_delete_user_not_registered(self, mock_query):
        # Предположим, что пользователь с id=2 не существует
        mock_query.return_value.filter_by.return_value.first.return_value = None

        result = User.delete_user(2)
        self.assertEqual(result, 'Вы не зарегистрированы!')

    @patch('project.database.models.session.query')
    def test_view_info(self, mock_query):
        user_data = {
            'id': 1,
            'name': 'Alice',
            'age': 25,
            'gender': 'Female',
            'weight': 60,
            'height': 165,
            'pace': 'Moderate',
            'split': 'Cardio'
        }
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        expected_info = f'ПРОФИЛЬ:\nВаше имя: <b>{user_data["name"]}</b>\nВаш возраст: <b>{user_data["age"]}</b>\nВаш пол: <b>{user_data["gender"]}</b>\nВаш вес: <b>{user_data["weight"]}</b>\nВаш рост: <b>{user_data["height"]}</b>\nВаша цель: <b>{user_data["pace"]}</b>\nВаш тренировочный план: <b>{user_data["split"]}</b>'
        self.assertEqual(User.view_info(1), expected_info)

    @patch('project.database.models.session.query')
    def test_update_user_name(self, mock_query):
        user_data = {
            'id': 1,
            'name': 'Alice',
            'age': 25,
            'gender': 'Female',
            'weight': 60,
            'height': 165,
            'pace': 'Moderate',
            'split': 'Cardio'
        }
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        new_name = 'Bob'
        User.update_user_name(1, new_name)
        updated_user = mock_query.return_value.filter_by.return_value.first.return_value
        self.assertEqual(updated_user.name, new_name)

    @patch('project.database.models.session.query')
    def test_set_name(self, mock_query):
        user_data = {
            'id': 1,
            'name': 'Alice',
            'age': 25,
            'gender': 'Female',
            'weight': 60,
            'height': 165,
            'pace': 'Moderate',
            'split': 'Cardio'
        }
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        new_name = 'Charlie'
        User.set_name(1, new_name)
        updated_user = mock_query.return_value.filter_by.return_value.first.return_value
        self.assertEqual(updated_user.name, new_name)

    @patch('project.database.models.session.query')
    def test_set_age(self, mock_query):
        user_data = {
            'id': 1,
            'name': 'Alice',
            'age': 25,
            'gender': 'Female',
            'weight': 60,
            'height': 165,
            'pace': 'Moderate',
            'split': 'Cardio'
        }
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        new_age = 30
        User.set_age(1, new_age)
        updated_user = mock_query.return_value.filter_by.return_value.first.return_value
        self.assertEqual(updated_user.age, new_age)

    @patch('project.database.models.session.query')
    def test_set_gender(self, mock_query):
        user_data = {
            'id': 1,
            'name': 'Alice',
            'gender': 'Female'
        }
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        new_gender = 'Male'
        User.set_gender(1, new_gender)
        updated_user = mock_query.return_value.filter_by.return_value.first.return_value
        self.assertEqual(updated_user.gender, new_gender)

    @patch('project.database.models.session.query')
    def test_set_weight(self, mock_query):
        user_data = {
            'id': 1,
            'name': 'Alice',
            'weight': 60
        }
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        new_weight = 70
        User.set_weight(1, new_weight)
        updated_user = mock_query.return_value.filter_by.return_value.first.return_value
        self.assertEqual(updated_user.weight, new_weight)


    @patch('project.database.models.session.query')
    def test_set_height(self, mock_query):
        user_data = {
            'id': 1,
            'name': 'Alice',
            'height': 165
        }
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)
        new_height = 170
        User.set_height(1, new_height)
        updated_user = mock_query.return_value.filter_by.return_value.first.return_value
        self.assertEqual(updated_user.height, new_height)

    @patch('project.database.models.session.query')
    def test_set_pace(self, mock_query):
        user_id = 1
        pace = 'High Intensity'
        user_data = {'id': user_id, 'name': 'Alice', 'pace': 'Moderate'}
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        User.set_pace(user_id, pace)
        updated_user = mock_query.return_value.filter_by.return_value.first.return_value
        self.assertEqual(updated_user.pace, pace)

    @patch('project.database.models.session.query')
    def test_set_split(self, mock_query):
        user_id = 1
        split_name = 'Strength Training'
        user_data = {'id': user_id, 'name': 'Alice', 'split': 'Cardio'}
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        User.set_split(user_id, split_name)
        updated_user = mock_query.return_value.filter_by.return_value.first.return_value
        self.assertEqual(updated_user.split, split_name)

    @patch('project.database.models.session.query')
    def test_get_age(self, mock_query):
        user_id = 1
        expected_age = 30
        user_data = {'id': user_id, 'name': 'Alice', 'age': expected_age}
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        self.assertEqual(User.get_age(user_id), expected_age)

    @patch('project.database.models.session.query')
    def test_get_weight(self, mock_query):
        user_id = 1
        expected_weight = 70
        user_data = {'id': user_id, 'name': 'Alice', 'weight': expected_weight}
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        self.assertEqual(User.get_weight(user_id), expected_weight)

    @patch('project.database.models.session.query')
    def test_get_height(self, mock_query):
        user_id = 1
        expected_weight = 165
        user_data = {'id': user_id, 'name': 'Alice', 'weight': expected_weight}
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        self.assertEqual(User.get_weight(user_id), expected_weight)

    @patch('project.database.models.session.query')
    def test_get_pace(self, mock_query):
        user_id = 1
        expected_pace = 'Moderate'
        user_data = {'id': user_id, 'name': 'Alice', 'pace': expected_pace}
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        self.assertEqual(User.get_pace(user_id), expected_pace)

    @patch('project.database.models.session.query')
    def test_get_split(self, mock_query):
        user_id = 1
        expected_split = 'Cardio'
        user_data = {'id': user_id, 'name': 'Alice', 'split': expected_split}
        mock_query.return_value.filter_by.return_value.first.return_value = User(**user_data)

        self.assertEqual(User.get_split(user_id), expected_split)


if __name__ == '__main__':
    unittest.main()
