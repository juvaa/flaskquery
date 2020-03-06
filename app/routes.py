from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime
from flask_basicauth import BasicAuth
import os


appurl = os.environ.get("URL")
app.config['BASIC_AUTH_USERNAME'] = os.environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("ADMIN_PASSWORD") or 'helevetinhyvasalasana' # TODO: this could be somewhere else

basic_auth = BasicAuth(app)

limit = 17

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2020, 3, 11, 12, 00, 00)
    endtime = datetime(2020, 3, 24, 23, 59, 59)
    nowtime = datetime.now()


    o_count = Model.query.filter_by(guild="otit").count()
    s_count = Model.query.filter_by(guild="sik").count()
    b_count = Model.query.filter_by(guild="blanko").count()
    h_count = Model.query.filter_by(guild="henkilokunta").count()

    if form.validate_on_submit():
        flash('Kiitos ilmoittautumisesta!')
        if form.attend.data and Model.query.filter_by(guild=form.guild.data).count() >= limit:
            flash('Olet varasijalla!')

        sub = Model(

            name=form.name.data,
            mail=form.mail.data,
            guild=form.guild.data,
            specialfoods=form.specialfoods.data,
            hopesndreams=form.hopesndreams.data,
            attend=form.attend.data,
            wine=form.wine.data,
            beer=form.beer.data,
            datetime=nowtime
        )

        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)
    return render_template('index.html', title='Opetuksenkehittämisseminaari ja proffasitsit 2020',
                        appurl=appurl,
                        o_count=o_count,
                        s_count=s_count,
                        b_count=b_count,
                        h_count=h_count,
                        starttime=starttime,
                        endtime=endtime,
                        nowtime=nowtime,
                        limit=limit,
                        form=form)


@app.route('/admin', methods=['GET'])
@basic_auth.required
def admin():
    o_entries = Model.query.filter_by(guild="otit")
    s_entries = Model.query.filter_by(guild="sik")
    b_entries = Model.query.filter_by(guild="blanko")
    h_entries = Model.query.filter_by(guild="henkilokunta")
    o_count = Model.query.filter_by(guild="otit").count()
    s_count = Model.query.filter_by(guild="sik").count()
    b_count = Model.query.filter_by(guild="blanko").count()
    h_count = Model.query.filter_by(guild="henkilokunta").count()
    return render_template('admin.html', title='OKS-2020 ADMIN', rooturl=appurl,
                           o_entries=o_entries,
                           s_entries=s_entries,
                           b_entries=b_entries,
                           h_entries=h_entries,
                           o_count=o_count,
                           s_count=s_count,
                           b_count=b_count,
                           h_count=h_count,
                           limit=limit)