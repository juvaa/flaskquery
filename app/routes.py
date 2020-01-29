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

    #starttime = datetime(2020, 1, 31, 10, 00, 00)
    #endtime = datetime(2020, 2, 10, 21, 59, 00)

    starttime = datetime(2020, 1, 29, 20, 16, 00)
    endtime = datetime(2020, 1, 29, 20, 17, 00)
    nowtime = datetime.utcnow()
    otitlimit = 33
    communicalimit = 33
    proselimit = 34

    entrys = Model.query.all()
    count = Model.query.count()


    otits = []
    communicas = []
    proses = []

    maxlimit = 500

    for entry in entrys:
        if entry.guild == "otit":
            otits.append({"name": entry.name})
        elif entry.guild == "communica":
            communicas.append({"name": entry.name})
        elif entry.guild == "prose":
            proses.append({"name": entry.name})


    if form.validate_on_submit() and count <= maxlimit:
        flash('Kiitos ilmoittautumisesta!')
        sub = Model(
            avec = False,
            name=form.name.data,
            mail=form.mail.data,
            guild = form.guild.data,
            alcohol = form.alcohol.data,
            wine = form.wine.data,
            beer = form.beer.data,
            specialneeds = form.specialneeds.data,
            avec_name = form.avec_name.data,
            other = form.other.data,
            datetime = nowtime
        )
        db.session.add(sub)
        if form.avec.data:
            sub = Model(
                avec = form.avec.data,
                name = form.avec_name.data,
                mail= " ",
                guild = form.guild.data,
                alcohol = form.avec_alcohol.data,
                wine = form.avec_wine.data,
                beer = form.avec_beer.data,
                specialneeds = form.avec_specialneeds.data,
                avec_name = " ",
                other = " ",
                datetime = nowtime
            )
            db.session.add(sub)
        db.session.commit()
        return redirect("{}".format(appurl))

    elif form.is_submitted() and count > maxlimit:
        flash('Ilmoittautuminen täynnä!')

    return render_template('index.html',
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           otitlimit=otitlimit,
                           otits=otits,
                           otitcount=len(otits),
                           communicalimit=communicalimit,
                           communicas=communicas,
                           communicacount=len(communicas),
                           proselimit=proselimit,
                           proses=proses,
                           prosecount=len(proses),
                           maxlimit=maxlimit,
                           form=form,
                           appurl=appurl)

@app.route('/admin', methods=['GET'])
@basic_auth.required
def admin():
    entrys = Model.query.all()
    return render_template('admin.html', title='Humu admin', appurl=appurl,
                           entrys=entrys)
