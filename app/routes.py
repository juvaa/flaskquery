from flask import render_template, flash, redirect, request
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

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    nowtime = datetime.now()

    if form.validate_on_submit():
        flash('Thank you for participating')
        sub = Model(
            hallitus = form.hallitus.data,
            tapahtuma = form.tapahtuma.data,
            ehdotus = form.ehdotus.data,
            muuta = form.muuta.data,
            datetime = nowtime,
            arkisto = False
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)
    return render_template('index.html', title='Palautetta OTiT:lle',
                                         form=form,
                                         appurl=appurl)


@app.route('/admin', methods=['GET', 'POST'])
@basic_auth.required
def admin():
    h_entries = Model.query.with_entities(Model.hallitus)
    t_entries = Model.query.with_entities(Model.tapahtuma)
    e_entries = Model.query.with_entities(Model.ehdotus)
    m_entries = Model.query.with_entities(Model.muuta)
    count = Model.query.count()
    entries = Model.query.all()

    if request.form:

        for h_entry in h_entries:
            if str(h_entry.id) in request.form.keys():
                if request.form[str(h_entry.id)] == "arkisto":
                    h_entry.arkisto = True
                    flash("Palaute arkistoitu")
                elif request.form[str(h_entry.id)] == "remove":
                    h_entry.hallitus = ""
                    flash("Palaute poistettu")
        for t_entry in t_entries:
            if str(t_entry.id) in request.form.keys():
                if request.form[str(t_entry.id)] == "arkisto":
                    t_entry.arkisto = True
                    flash("Palaute arkistoitu")
                elif request.form[str(t_entry.id)] == "remove":
                    t_entry.tapahtuma = ""
                    flash("Palaute poistettu")
        for e_entry in e_entries:
            if str(e_entry.id) in request.form.keys():
                if request.form[str(e_entry.id)] == "arkisto":
                    e_entry.arkisto = True
                    flash("Palaute arkistoitu")
                elif request.form[str(e_entry.id)] == "remove":
                    e_entry.ehdotus = ""
                    flash("Palaute poistettu")
        for m_entry in m_entries:
            if str(m_entry.id) in request.form.keys():
                if request.form[str(m_entry.id)] == "arkisto":
                    m_entry.arkisto = True
                    flash("Palaute arkistoitu")
                elif request.form[str(m_entry.id)] == "remove":
                    m_entry.muuta = ""
                    flash("Palaute poistettu")
        for entry in entries:
            if (entry.hallitus and entry.tapahtuma and entry.ehdotus
                and entry.muuta):
                db.session.delete(entry)
        db.session.commit()
        return redirect(appurl + '/admin')
    return render_template('admin.html', title='Palaute boxi',
                                         h_entries=h_entries,
                                         t_entries=t_entries,
                                         e_entries=e_entries,
                                         m_entries=m_entries,
                                         count=count,
                                         appurl=appurl)
