from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from base import


from functools import wraps

# Декоратор для обработки ошибок и отката транзакции
def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
    return wrapper

# Функция для создания нового объекта пользователя с использованием декоратора
@handle_errors
def create_user(name: str) -> User:
    new_user = User(name=name)
    session.add(new_user)
    return new_user

# Функция для изменения атрибута имени пользователя с использованием декоратора
@handle_errors
def update_user_name(user_id: int, new_name: str) -> User:
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.name = new_name
        return user
    else:
        raise ValueError("User not found")
