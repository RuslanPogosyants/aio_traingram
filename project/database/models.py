from .base import Base, session, engine
from sqlalchemy import Column, Integer, String, BigInteger
from aiogram.utils.markdown import hbold


class User(Base):
    __tablename__ = "user_account"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(30), default=None)
    gender = Column(String(30), default=None)
    age = Column(Integer, default=None)
    height = Column(Integer, default=None)
    weight = Column(Integer, default=None)
    pace = Column(String(30), default=None)
    split = Column(String(30), default=None)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}"

    @classmethod
    def user_exist(cls, user_id: int) -> bool:
        user = session.query(cls).filter_by(id=user_id).first()
        return user is not None

    @classmethod
    def create_user(cls, user_id: int) -> None:
        new_user = cls(id=user_id)
        session.add(new_user)
        session.commit()

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
        info = f'ПРОФИЛЬ:\nВаше имя: {hbold(user.name)}\nВаш возраст: {hbold(user.age)}\nВаш пол: {hbold(user.gender)}\nВаш вес: {hbold(user.weight)}\nВаш рост: {hbold(user.height)}\nВаша цель: {hbold(user.pace)}\nВаш тренировочный план: {hbold(user.split)}'
        if user:
            return info
        else:
            return 'Вы не зарегистрированы!'

    @classmethod
    def update_user_name(cls, user_id: int, new_name: str) -> None:
        user = session.query(cls).filter_by(id=user_id).first()
        user.name = new_name
        session.commit()

    @classmethod
    def set_name(cls, user_id: int, name) -> None:
        user = session.query(cls).filter_by(id=user_id).first()
        user.name = name
        session.commit()

    @classmethod
    def set_age(cls, user_id: int, age) -> None:
        user = session.query(cls).filter_by(id=user_id).first()
        user.age = age
        session.commit()

    @classmethod
    def set_gender(cls, user_id: int, gender) -> None:
        user = session.query(cls).filter_by(id=user_id).first()
        user.gender = gender
        session.commit()

    @classmethod
    def set_weight(cls, user_id: int, weight) -> None:
        user = session.query(cls).filter_by(id=user_id).first()
        user.weight = weight
        session.commit()

    @classmethod
    def set_height(cls, user_id: int, height) -> None:
        user = session.query(cls).filter_by(id=user_id).first()
        user.height = height
        session.commit()

    @classmethod
    def set_pace(cls, user_id: int, pace) -> None:
        user = session.query(cls).filter_by(id=user_id).first()
        user.pace = pace
        session.commit()

    @classmethod
    def set_split(cls, user_id: int, split_name) -> None:
        user = session.query(cls).filter_by(id=user_id).first()
        user.split = split_name
        session.commit()

    @classmethod
    def get_name(cls, user_id) -> str:
        user = session.query(cls).filter_by(id=user_id).first()
        return user.name if user else None

    @classmethod
    def get_gender(cls, user_id) -> str:
        user = session.query(cls).filter_by(id=user_id).first()
        return user.gender if user else None

    @classmethod
    def get_age(cls, user_id) -> int:
        user = session.query(cls).filter_by(id=user_id).first()
        return user.age if user else None

    @classmethod
    def get_height(cls, user_id) -> int:
        user = session.query(cls).filter_by(id=user_id).first()
        return user.height if user else None

    @classmethod
    def get_weight(cls, user_id) -> int:
        user = session.query(cls).filter_by(id=user_id).first()
        return user.weight if user else None

    @classmethod
    def get_pace(cls, user_id) -> str:
        user = session.query(cls).filter_by(id=user_id).first()
        return user.pace if user else None

    @classmethod
    def get_split(cls, user_id) -> str:
        user = session.query(cls).filter_by(id=user_id).first()
        return user.split if user else None


Base.metadata.create_all(engine)
