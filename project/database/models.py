from .base import Base, session
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import select
from aiogram.utils.markdown import hbold


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}"

    @classmethod
    def user_exist(cls, user_id: int) -> bool:
        user = session.query(cls).filter_by(id=user_id).first()
        return user is not None

    @classmethod
    def create_user(cls, user_id: int) -> "User":
        new_user = user_id
        session.add(new_user)
        session.commit()
        return new_user

    @classmethod
    def delete_user(cls, user_id: int) -> str:
        if User.user_exist(user_id) is False:
            return "Вы не зарегистрированы!"
        session.query(cls).filter_by(id=user_id).delete()
        session.commit()
        return 'Ваш аккаунт был удален!'

    @classmethod
    def view_info(cls, user_id: int) -> str:
        user = session.query(cls).filter_by(id=user_id).first()
        info = f'Ваше имя: {hbold(user.name)}\n'
        f'Ваш возраст: {hbold(user.age)}\n'
        f'Ваш пол: {hbold(user.gender)}\n'
        f'Ваш вес: {hbold(user.weight)}\n'
        f'Ваш рост: {hbold(user.height)}\n'
        f'Ваша цель: {hbold(user.pace)}\n'
        if user:
            return info
        else:
            raise ValueError("User not found")

    @classmethod
    def update_user_name(cls, user_id: int, new_name: str) -> "User":
        user = session.query(cls).filter_by(id=user_id).first()
        if user:
            user.name = new_name
            session.commit()
            return user
        else:
            raise ValueError("User not found")

    @classmethod
    def set_name(cls, user_id: int, name):
        user = session.query(cls).filter_by(id=user_id).first()
        user.name = name
        session.commit()

    @classmethod
    def set_age(cls, user_id: int, age):
        user = session.query(cls).filter_by(id=user_id).first()
        user.age = age
        session.commit()

    @classmethod
    def set_gender(cls, user_id: int, gender):
        user = session.query(cls).filter_by(id=user_id).first()
        user.gender = gender
        session.commit()

    @classmethod
    def set_weight(cls, user_id: int, weight):
        user = session.query(cls).filter_by(id=user_id).first()
        user.weight = weight
        session.commit()

    @classmethod
    def set_height(cls, user_id: int, height):
        user = session.query(cls).filter_by(id=user_id).first()
        user.height = height
        session.commit()

    @classmethod
    def set_pace(cls, user_id: int, pace):
        user = session.query(cls).filter_by(id=user_id).first()
        user.pace = pace
        session.commit()


