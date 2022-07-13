from flask import render_template, request, redirect, url_for
from login.blueprint import login_bp
from loginDAO.getdata import check_log_in

@login_bp.route("/success")
def success():
    return render_template("success.html")

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if check_log_in(username, password) == True:
            return redirect("/success")
        else:
            return redirect("/login")

    return render_template("login.html")
