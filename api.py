import flask
from flask import request
from data import db_session
from data.__all_models import *
from token_generation import genaration_token
from flask import jsonify

blueprint = flask.Blueprint("api",
                            __name__,
                            template_folder='templates')


@blueprint.route("/api/zbolj23bn156m69mu6f3xzlmvmwm3m/get_code", methods=["POST"])
def send_code():
    """
    data = {
        "type_game": string
    }
    """
    db_sess = db_session.create_session()
    codes_data = db_sess.query(Room).all()
    codes = set()
    for code_data in codes_data:
        codes.add(code_data.code)
    while True:
        code = genaration_token(4).upper()
        if code not in codes:
            db_sess = db_session.create_session()
            room = Room()
            room.code = code
            room.type_game = request.json["type_game"]
            db_sess.add(room)
            db_sess.commit()
            return jsonify({"code_room": code})


# @blueprint.route("/api/zbolj23bn156m69mu6f3xzlmvmwm3m/send_question", methods=["POST"])
# def get_question():
#     """
#     data = {
#         "question": string,
#         "answer": string[],
#         "option_true": int index
#     }
#     """
#
#     print(request.json)
#     return jsonify({"status": "ok"})


@blueprint.route("/api/zbolj23bn156m69mu6f3xzlmvmwm3m/update_player", methods=["GET"])
def update_player():
    """
    data = {
        "code_room": string
    }
    """
    db_sess = db_session.create_session()
    room = db_sess.query(Room).filter(Room.code == request.json["code_room"]).first()
    users_data = db_sess.query(User).filter(User.code == room.id).all()
    users = set()
    for users_data in users_data:
        users.add(users_data.name)

    return jsonify({"playrs": list(users)})


# @blueprint.route("/api/zbolj23bn156m69mu6f3xzlmvmwm3m/point_playr", methods=["GET"])
# def point_player():
#     """
#     {
#     "code_room": sring
#     }
#     """
#     db_sess = db_session.create_session()
#     room = db_sess.query(Room).filter(Room.code == request.json["code_room"]).first()
#     users_data = db_sess.query(User).filter(User.code == room.id).all()
#     points = []
#     users = []
#     for user in users_data:
#         users.append(user.name)
#         points.append(db_sess.query(Game).filter(Game.token == user.token).first().point)
#
#     return jsonify({
#         "user": users,
#         "points": points
#     })


@blueprint.route("/api/zbolj23bn156m69mu6f3xzlmvmwm3m/exit", methods=["DELETE"])
def exit():
    """
    {
    "code_room": sring
    }
    """
    db_sess = db_session.create_session()
    room = db_sess.query(Room).filter(Room.code == request.json["code_room"]).first()
    users_data = db_sess.query(User).filter(User.code == room.id).all()
    for user in users_data:
        # db_sess.delete(db_sess.query(Game).filter(Game.token == user.token).first())
        db_sess.delete(user)
    db_sess.delete(room)
    db_sess.commit()

    return jsonify({"status": "ok"})
