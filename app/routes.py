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

    teekkaritime = datetime(2019, 10, 30, 13, 37, 00)
    endtime = datetime(2019, 11, 4, 11, 59, 59)
    nowtime = datetime.now()


    entries_temp = Model.query.all()

    entries = []

    for entry in entries_temp:
        if entry.gdpr:
            entries.append({"name": entry.name, "avec": False, "operator": entry.operator})
        else:
            entries.append({"name": "Remminorsu", "avec": False, "operator": entry.operator})

        if entry.avec:
            if entry.avec_gdpr:
                entries.append({"name": entry.avec_name, "avec": True})
            else:
                entries.append({"name": "Norsuavec", "avec": True})






    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        sub = Model(
            name=form.name.data,
            mail = form.mail.data,
            operator = form.operator.data,
            alcohol = form.alcohol.data,
            wine = form.wine.data,
            beer = form.beer.data,
            specialneeds = form.specialneeds.data,
            gdpr = form.gdpr.data,
            avec = form.avec.data,
            avec_name = form.avec_name.data,
            avec_alcohol = form.avec_alcohol.data,
            avec_wine = form.avec_wine.data,
            avec_beer = form.avec_beer.data,
            avec_specialneeds = form.avec_specialneeds.data,
            avec_gdpr = form.avec_gdpr.data,
            datetime = nowtime
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)



    return render_template('index.html',
                           appurl=appurl,
                           teekkaritime=teekkaritime,
                           endtime=endtime,
                           nowtime=nowtime,
                           entries=entries,
                           form=form)
