from flask import Flask, redirect, render_template, url_for, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "ThisISMyFIRSTSessionCODEinREDTONE"
app.permanent_session_lifetime = timedelta(seconds=60)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You have already logged in", "info")
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
        # return f"<h1>Hello {user}, you are loged in.</h1>"
    else:
        flash("You are not logged in", "info")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out", "info")
    session.pop("user", None)
    # flash("You have been logged out!", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
