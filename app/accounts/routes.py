
from flask import render_template, request, redirect, flash, url_for, current_app
from extensions import db, login_manager


@account.route("/signup", methods=["GET", "POST"])
def signup():
    # Future improvement tip: check if username is unique
    if request.method == "POST":
        if Blog_User.query.filter_by(email=request.form.get("email")).first():
            # if user already exists:
            flash("This email is already registered with us. Log-in instead!")
            return redirect(url_for("account.login"))

        new_user = Blog_User(
            name=request.form.get("username"),
            email=request.form.get("email"),
            password=hash_pw(request.form.get("password")),
            type="user"
        )
        db.session.add(new_user)
        db.session.commit()
        update_stats_users_total()
        update_stats_users_active(1)

        login_user(new_user)

        return redirect(url_for('account.dashboard'))

    return render_template('account/signup.html', logged_in=current_user.is_authenticated)

@account.route('/login', methods=["GET", "POST"])
def login