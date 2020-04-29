from flask import render_template, flash, redirect, request
from app import app, db
from app.forms import Form
from app.models import Hallitus, Tapahtuma, Ehdotus, Muuta
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
        h_sub = Hallitus(
            palaute = form.hallitus.data,
            datetime = nowtime,
            arkisto = False
        )
        t_sub = Tapahtuma(
            palaute = form.tapahtuma.data,
            datetime = nowtime,
            arkisto = False
        )
        e_sub = Ehdotus(
            palaute = form.ehdotus.data,
            datetime = nowtime,
            arkisto = False
        )
        m_sub = Muuta(
            palaute = form.muuta.data,
            datetime = nowtime,
            arkisto = False
        )
        db.session.add(h_sub)
        db.session.add(t_sub)
        db.session.add(e_sub)
        db.session.add(m_sub)
        db.session.commit()
        return redirect(appurl)
    return render_template('index.html', title='Palautetta OTiT:lle',
                                         form=form,
                                         appurl=appurl)


@app.route('/admin', methods=['GET', 'POST'])
@basic_auth.required
def admin():
    h_entries = Hallitus.query.all()
    t_entries = Tapahtuma.query.all()
    e_entries = Ehdotus.query.all()
    m_entries = Muuta.query.all()
    h_new = Hallitus.query.filter_by(arkisto = False).count()
    t_new = Tapahtuma.query.filter_by(arkisto = False).count()
    e_new = Ehdotus.query.filter_by(arkisto = False).count()
    m_new = Muuta.query.filter_by(arkisto = False).count()
    new = h_new + t_new + e_new + m_new

    if request.form:

        for h_entry in h_entries:
            if ("h_" + str(h_entry.id)) in request.form.keys():
                if request.form[("h_" + str(h_entry.id))] == "arkisto":
                    h_entry.arkisto = True
                    flash("Palaute arkistoitu")
                elif request.form[("h_" + str(h_entry.id))] == "remove":
                    db.session.delete(h_entry)
                    flash("Palaute poistettu")
        for t_entry in t_entries:
            if ("t_" + str(t_entry.id)) in request.form.keys():
                if request.form[("t_" + str(t_entry.id))] == "arkisto":
                    t_entry.arkisto = True
                    flash("Palaute arkistoitu")
                elif request.form[("t_" + str(t_entry.id))] == "remove":
                    db.session.delete(t_entry)
                    flash("Palaute poistettu")
        for e_entry in e_entries:
            if ("e_" + str(e_entry.id)) in request.form.keys():
                if request.form[("e_" + str(e_entry.id))] == "arkisto":
                    e_entry.arkisto = True
                    flash("Palaute arkistoitu")
                elif request.form[("e_" + str(e_entry.id))] == "remove":
                    db.session.delete(e_entry)
                    flash("Palaute poistettu")
        for m_entry in m_entries:
            if ("m_" + str(m_entry.id)) in request.form.keys():
                if request.form[("m_" + str(m_entry.id))] == "arkisto":
                    m_entry.arkisto = True
                    flash("Palaute arkistoitu")
                elif request.form[("m_" + str(m_entry.id))] == "remove":
                    db.session.delete(m_entry)
                    flash("Palaute poistettu")
        db.session.commit()
        return redirect(appurl + '/admin')
    return render_template('admin.html', title='Palaute boxi',
                                         h_entries=h_entries,
                                         t_entries=t_entries,
                                         e_entries=e_entries,
                                         m_entries=m_entries,
                                         new=new,
                                         appurl=appurl)
