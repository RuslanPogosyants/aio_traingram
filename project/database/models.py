from .bd import Base
from .bd import session
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import select, delete


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"

    @staticmethod
    def create_user(user_id: int):
        user = User(id=user_id, name=None)
        session.add(user)
        session.commit()

    @staticmethod
    def user_exist(user_id: int) -> bool:
        stmt = select(User).where(User.id == user_id)
        result = session.execute(stmt)
        return result.scalar() is not None

    @staticmethod
    def delete_user(user_id: int) -> None:
        stmt = delete(User).where(User.id == user_id)
        result = session.execute(stmt)
        return result.scalar() is not None
