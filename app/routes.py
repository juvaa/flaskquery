import os
from flask import render_template, flash, redirect, url_for, Markup
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime
from flask_basicauth import BasicAuth


app.config['BASIC_AUTH_USERNAME'] = os.environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("ADMIN_PASSWORD") or 'supersalasanajeejee' # TODO: this could be somewhere else

basic_auth = BasicAuth(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    nowtime = datetime.now()

    entrys = Model.query.all()

    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisestasi!')
        sub = Model(
            nick = form.nick.data,
            email = form.email.data,
            phone = form.phone.data,
            con_irc = form.con_irc.data,
            con_tel = form.con_tel.data,
            con_email = form.con_email.data,
            organize = form.organize.data,
            game = form.game.data,
            time = form.time.data,
            other = form.other.data,

            datetime = nowtime,

        )
        if form.con_irc:
            flash('IRC kanava: #otit.vauhtijuoksu')

        if form.con_tel:
            flash(Markup('Telegrammissa: <a href="https://t.me/joinchat/ENh2gRcXarScnITp3cukJw">vauhtijuoksu</a>'))

        if form.organize.data:
            flash("Suunnitteluhommia:")
            if form.con_irc:
                flash('IRC kanava: #otit.vauhtijuoksu.suunnittelu')
            if form.con_tel:
                flash(Markup('Telegrammissa: <a href="https://t.me/joinchat/ENh2gRREItqKUKOYdF0BeA">Vauhtijuoksu - suunnittelu</a>'))

        db.session.add(sub)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('index.html', title='Vauhtijuoksu',
                                         entrys=entrys,
                                         form=form)

@app.route('/admin', methods=['GET', 'POST'])
@basic_auth.required
def admin():
    entrys = Model.query.all()


    return render_template('admin.html', title='SpeedrunAdmin',
                                         entrys=entrys)

