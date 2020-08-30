from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime
from flask_basicauth import BasicAuth
from os import environ


appurl = environ.get("URL")
app.config['BASIC_AUTH_USERNAME'] = environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = environ.get("ADMIN_PASSWORD") or 'helevetinhyvasalasana' # TODO: this could be somewhere else

basic_auth = BasicAuth(app)

f_limit = 85
p_limit = 8
h_limit = 10

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2020, 8, 29, 21, 38, 00)
    endtime = datetime(2020, 8, 30, 22, 00, 00)
    nowtime = datetime.now()


    f_count = Model.query.filter_by(guild="fuksi").count()
    p_count = Model.query.filter_by(guild="pro").count()
    h_count = Model.query.filter_by(guild="hallitus").count()
    f_entries = Model.query.filter_by(guild="fuksi")
    p_entries = Model.query.filter_by(guild="pro")
    h_entries = Model.query.filter_by(guild="hallitus")

    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        if form.guild.data == "fuksi":
            if Model.query.filter_by(guild="fuksi").count() >= f_limit:
                flash('Olet varasijalla!')
        elif form.guild.data == "pro":
            if Model.query.filter_by(guild="pro").count() >= p_limit:
                flash('Olet varasijalla!')
        elif form.guild.data == "hallitus":
            if Model.query.filter_by(guild="hallitus").count() >= h_limit:
                flash('Olet varasijalla!')

        sub = Model(
            name=form.name.data,
            mail=form.mail.data,
            guild=form.guild.data,
            specialfoods=form.specialfoods.data,
            alcohol=form.alcohol.data,
            wine=form.wine.data,
            beer=form.beer.data,
            name_consent = form.name_consent.data,
            datetime=nowtime
        )

        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)
    return render_template('index.html',
                            title='Fuksisitsit',
                            appurl=appurl,
                            f_count=f_count,
                            p_count=p_count,
                            h_count=h_count,
                            f_entries=f_entries,
                            p_entries=p_entries,
                            h_entries=h_entries,
                            starttime=starttime,
                            endtime=endtime,
                            nowtime=nowtime,
                            f_limit=f_limit,
                            p_limit=p_limit,
                            h_limit=h_limit,
                            form=form)


@app.route('/admin', methods=['GET'])
@basic_auth.required
def admin():
    f_entries = Model.query.filter_by(guild="fuksi")
    p_entries = Model.query.filter_by(guild="pro")
    h_entries = Model.query.filter_by(guild="hallitus")
    f_count = Model.query.filter_by(guild="fuksi").count()
    p_count = Model.query.filter_by(guild="pro").count()
    h_count = Model.query.filter_by(guild="hallitus").count()
    return render_template('admin.html',
                            title='Fuksisitsi ADMIN',
                            appurl=appurl,
                            f_entries=f_entries,
                            p_entries=p_entries,
                            h_entries=h_entries,
                            f_count=f_count,
                            p_count=p_count,
                            h_count=h_count,
                            f_limit=f_limit,
                            p_limit=p_limit,
                            h_limit=h_limit)