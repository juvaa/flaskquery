from flask import render_template, flash, redirect
from app import app, db
from app.forms import Form
from app.models import Register, Invite_register
from datetime import datetime
from flask_basicauth import BasicAuth
from os import environ


APPURL = environ.get("URL")
app.config['BASIC_AUTH_USERNAME'] = environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = environ.get("ADMIN_PASSWORD") or 'helevetinhyvasalasana' # TODO: this could be somewhere else

basic_auth = BasicAuth(app)

limit = 17


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html',
                           appurl=APPURL,
                           title='Vuosijuhlat',
                           )


@app.route('/ohjelma', methods=['GET'])
def schedule():
    return render_template('schedule.html',
                           appurl=APPURL,
                           title='Vuosijuhlien ohjelma',
                           )


@app.route('/ilmo', methods=['GET', 'POST'])
def register():
    form = Form()

    starttime = datetime(2020, 3, 11, 12, 00, 00)
    endtime = datetime(2020, 6, 24, 23, 59, 59)
    nowtime = datetime.now()


    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        #if Model.query.filter_by(guild=form.guild.data).count() >= limit:
        #    flash('Olet varasijalla!')

        sub = Register(

            name=form.name.data,
            mail=form.mail.data,
            s_year=form.s_year.data,
            specialfoods=form.specialfoods.data,
            sillis=form.sillis.data,
            greeting=form.greeter.data,
            avek=form.avek_name.data,
            avek_specialfoods=form.avek_specialfoods.data,
            history=form.history.data,
            table=form.table.data,
            name_consent=form.name_consent.data,
            datetime=nowtime
        )

        db.session.add(sub)
        db.session.commit()
        return redirect(APPURL + '/ilmo')


    entries = Register.query.all()

    names = []

    for entry in entries:
        if entry.avek:
            if entry.name_consent:
                names.append(entry.name)
                names.append(entry.avek)
            else:
                names.append('anonyymi')
                names.append('anonyymi')
        else:
            if entry.name_consent:
                names.append(entry.name)
            else:
                names.append('anonyymi')

    count = len(names)

    return render_template('register.html',
                           title='Ilmoittautuminen',
                           appurl=APPURL,
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           limit=limit,
                           names=names,
                           count=count,
                           form=form
                           )


@app.route('/kutsu-ilmo', methods=['GET', 'POST'])
def invite_register():
    form = Form()

    starttime = datetime(2020, 3, 11, 12, 00, 00)
    endtime = datetime(2020, 6, 24, 23, 59, 59)
    nowtime = datetime.now()


    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        #if Model.query.filter_by(guild=form.guild.data).count() >= limit:
        #    flash('Olet varasijalla!')

        sub = Invite_register(

            name=form.name.data,
            mail=form.mail.data,
            specialfoods=form.specialfoods.data,
            sillis=form.sillis.data,
            greeting=form.greeter.data,
            avek=form.avek_name.data,
            avek_specialfoods=form.avek_specialfoods.data,
            history=form.history.data,
            table=form.table.data,
            name_consent=form.name_consent.data,
            datetime=nowtime
        )

        db.session.add(sub)
        db.session.commit()
        return redirect(APPURL + '/kutsu-ilmo')
    return render_template('invite_register.html',
                           title='Ilmoittautuminen',
                           appurl=APPURL,
                           starttime=starttime,
                           endtime=endtime,
                           nowtime=nowtime,
                           limit=limit,
                           form=form
                           )


@app.route('/admin', methods=['GET'])
@basic_auth.required
def admin():
    kiltalaiset = Register.query.all()
    kutsutut = Invite_register.query.all()
    return render_template('admin.html',
                           title='VUJU ADMIN',
                           appurl=APPURL,
                           kiltalaiset=kiltalaiset,
                           kutsutut=kutsutut,
                           limit=limit
                           )