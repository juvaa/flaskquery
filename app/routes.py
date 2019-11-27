from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime
from flask_basicauth import BasicAuth
import os

app.config['BASIC_AUTH_USERNAME'] = os.environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("ADMIN_PASSWORD") or 'helevetinhyvasalasana' # TODO: this could be somewhere else
appurl = os.environ.get("URL")
basic_auth = BasicAuth(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2019, 10, 30, 13, 37, 00)
    endtime = datetime(2019, 11, 4, 11, 59, 59)
    nowtime = datetime.now()


    entries_temp = Model.query.all()

    entries = []

    for entry in entries_temp:
        if entry.gdpr:
            entries.append({"name": entry.name, "guild": entry.operator})
        else:
            entries.append({"name": "Anonyymi", "guild": entry.operator})





    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        sub = Model(
            name=form.name.data,
            mail = form.mail.data,
            guild = form.guild.data,
            alcohol = form.alcohol.data,
            wine = form.wine.data,
            beer = form.beer.data,
            specialneeds = form.specialneeds.data,
            gdpr = form.gdpr.data,
            datetime = nowtime
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)



    return render_template('index.html',
                           appurl=appurl,
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           entries=entries,
                           form=form)
