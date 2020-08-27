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

limit = 17

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2020, 3, 11, 12, 00, 00)
    endtime = datetime(2020, 3, 24, 23, 59, 59)
    nowtime = datetime.now()


    f_count = Model.query.filter_by(guild="fuksi").count()
    p_count = Model.query.filter_by(guild="pro").count()
    h_count = Model.query.filter_by(guild="hallitus").count()

    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        if Model.query.filter_by(guild=form.guild.data).count() >= limit:
            flash('Olet varasijalla!')

        sub = Model(

            name=form.name.data,
            mail=form.mail.data,
            guild=form.guild.data,
            specialfoods=form.specialfoods.data,
            wine=form.wine.data,
            beer=form.beer.data,
            datetime=nowtime
        )

        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)
    return render_template('index.html', title='Opetuksenkehittämisseminaari ja proffasitsit 2020',
                            appurl=appurl,
                            f_count=f_count,
                            p_count=p_count,
                            h_count=h_count,
                            starttime=starttime,
                            endtime=endtime,
                            nowtime=nowtime,
                            limit=limit,
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
    return render_template('admin.html', title='fuksisitsi ADMIN',
                            rooturl=appurl,
                            f_entries=f_entries,
                            p_entries=p_entries,
                            h_entries=h_entries,
                            f_count=f_count,
                            p_count=p_count,
                            h_count=h_count,
                            limit=limit)