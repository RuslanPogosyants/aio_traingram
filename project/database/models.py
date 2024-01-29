from .base import Base, session
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import select


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}"

    @classmethod
    def user_exists(cls, user_id: int) -> bool:
        user = session.query(cls).filter_by(id=user_id).first()
        return user is not None

    @classmethod
    def create_user(cls, name: str) -> "User":
        new_user = cls(name=name)
        session.add(new_user)
        session.commit()
        return new_user

    @classmethod
    def update_user_name(cls, user_id: int, new_name: str) -> "User":
        user = session.query(cls).filter_by(id=user_id).first()
        if user:
            user.name = new_name
            session.commit()
            return user
        else:
            raise ValueError("User not found")
