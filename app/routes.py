from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime
import os

appurl = os.environ.get("URL")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2020, 1, 28, 21, 20, 00)
    endtime = datetime(2020, 1, 28, 21, 25, 00)
    nowtime = datetime.utcnow()
    #otitlimit = 33
    #communicalimit = 33
    #proselimit = 34

    otitlimit = 3
    communicalimit = 3
    proselimit = 3

    entrys = Model.query.all()
    count = Model.query.count()


    otits = []
    communicas = []
    proses = []

    #maxlimit = 100
    maxlimit = 9

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
