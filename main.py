from flask import Flask, render_template, request, redirect
from token_generation import genaration_token
from data import db_session
from data import users
import api
from data import rooms

app = Flask(__name__)
app.config["SECRET_KEY"] = "scp-foundation_secret_key"
rooms_questions = {}


@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "GET":
        return render_template("index0.html")
    if request.method == "POST":
        db_sess = db_session.create_session()
        code_in_bd = False
        room_data = None
        for room in db_sess.query(rooms.Room).all():
            if room.code == request.form["code"].upper():
                code_in_bd = True
                room_data = room
                users_in_room = db_sess.query(users.User).filter(users.User.code == room_data.id).all()
                break
        if code_in_bd and len(users_in_room) <= 7 and room_data.status_room == "ожидание играков":
            find_users = db_sess.query(users.User).filter(users.User.code == room_data.id).all()
            for user in find_users:
                if request.form["nickname"] == user.name:
                    break
            else:
                token = genaration_token(30)
                user = users.User()
                user.token = token
                user.code = room_data.id
                user.name = request.form["nickname"].upper()
                db_sess.add(user)
                db_sess.commit()
                return redirect(f"/room/{token}")
            return redirect("/")
        else:
            return redirect('/')
        return render_template("index0.html")


@app.route("/room/<string:token>")
def room_logic(token):
    db_sess = db_session.create_session()
    user = db_sess.query(users.User).filter(users.User.token == token).first()
    print(user)
    if user:
        return render_template("wait.html")
    return redirect("/404")


if __name__ == '__main__':
    db_session.global_init("db/datanase.bd")
    app.register_blueprint(api.blueprint)
    app.run("127.0.0.1", 1232)
