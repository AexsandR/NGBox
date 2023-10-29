import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"
    token = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    code = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("rooms.id"))
    name = sqlalchemy.Column(sqlalchemy.Integer)

