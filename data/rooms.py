from .db_session import SqlAlchemyBase

import sqlalchemy


class Room(SqlAlchemyBase):
    __tablename__ = "rooms"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    code = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    status_room = sqlalchemy.Column(sqlalchemy.String)
    type_game = sqlalchemy.Column(sqlalchemy.String, nullable=True)
