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

    starttime = datetime(2019, 12, 2, 13, 37, 00)
    endtime = datetime(2019, 12, 8, 23, 59, 59)
    nowtime = datetime.now()


    entries_temp = Model.query.all()

    otits = []
    olos = []

    for entry in entries_temp:
        if entry.guild == "otit":
            if entry.gdpr:
                otits.append(entry.name)
            else:
                otits.append("Remminorsu")
        if entry.guild == "olo":
            if entry.gdpr:
                olos.append(entry.name)
            else:
                olos.append("Anonyymi")



    if form.validate_on_submit():
        flash('Form has been submitted!')
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
                           otits=otits,
                           olos=olos,
                           form=form)
