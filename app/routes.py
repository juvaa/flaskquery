from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime
from flask_basicauth import BasicAuth
import os


rooturl = os.environ.get("ROOT_URL")
app.config['BASIC_AUTH_USERNAME'] = os.environ.get("ADMIN_USER") or 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get("ADMIN_PASSWORD") or 'helevetinhyvasalasana' # TODO: this could be somewhere else

basic_auth = BasicAuth(app)

limit = 17

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    starttime = datetime(2018, 3, 8, 12, 00, 00)
    endtime = datetime(2019, 3, 26, 00, 00, 00)
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
        return redirect(rooturl)
    return render_template('index.html', title='Opetuksenkehittämisseminaari ja proffasitsit 2019', rooturl=rooturl,
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
    o_entries = Model.query.filter_by(guild="otit", attend=True)
    s_entries = Model.query.filter_by(guild="sik", attend=True)
    b_entries = Model.query.filter_by(guild="blanko", attend=True)
    h_entries = Model.query.filter_by(guild="henkilokunta", attend=True)
    entries = Model.query.filter_by(attend=False)
    o_count = Model.query.filter_by(guild="otit", attend=True).count()
    s_count = Model.query.filter_by(guild="sik", attend=True).count()
    b_count = Model.query.filter_by(guild="blanko", attend=True).count()
    h_count = Model.query.filter_by(guild="henkilokunta", attend=True).count()
    count = Model.query.filter_by(attend=False).count()
    return render_template('admin.html', title='OKS-2019 ADMIN', rooturl=rooturl,
                           o_entries=o_entries,
                           s_entries=s_entries,
                           b_entries=b_entries,
                           h_entries=h_entries,
                           entries=entries,
                           o_count=o_count,
                           s_count=s_count,
                           b_count=b_count,
                           h_count=h_count,
                           count=count,
                           limit=limit)