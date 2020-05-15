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
        flash('Kiitos palautteesta!')
        if form.hallitus.data:
            h_sub = Hallitus(
                palaute = form.hallitus.data,
                nimi = form.nimi.data,
                email = form.email.data,
                datetime = nowtime,
                arkisto = False
            )
            db.session.add(h_sub)
        if form.tapahtuma.data:
            t_sub = Tapahtuma(
                palaute = form.tapahtuma.data,
                nimi = form.nimi.data,
                email = form.email.data,
                datetime = nowtime,
                arkisto = False
            )
            db.session.add(t_sub)
        if form.ehdotus.data:
            e_sub = Ehdotus(
                palaute = form.ehdotus.data,
                nimi = form.nimi.data,
                email = form.email.data,
                datetime = nowtime,
                arkisto = False
            )
            db.session.add(e_sub)
        if form.muuta.data:
            m_sub = Muuta(
                palaute = form.muuta.data,
                nimi = form.nimi.data,
                email = form.email.data,
                datetime = nowtime,
                arkisto = False
            )
            db.session.add(m_sub)
        db.session.commit()
        return redirect(appurl)
    return render_template('index.html', title='Palautetta OTiT:lle',
                                         form=form,
                                         appurl=appurl)


@app.route('/admin', methods=['GET', 'POST'])
@basic_auth.required
def admin():
    h_entries = Hallitus.query.filter_by(arkisto = False)
    t_entries = Tapahtuma.query.filter_by(arkisto = False)
    e_entries = Ehdotus.query.filter_by(arkisto = False)
    m_entries = Muuta.query.filter_by(arkisto = False)
    h_new = Hallitus.query.filter_by(arkisto = False).count()
    t_new = Tapahtuma.query.filter_by(arkisto = False).count()
    e_new = Ehdotus.query.filter_by(arkisto = False).count()
    m_new = Muuta.query.filter_by(arkisto = False).count()
    h_arkistot = Hallitus.query.filter_by(arkisto = True)
    t_arkistot = Tapahtuma.query.filter_by(arkisto = True)
    e_arkistot = Ehdotus.query.filter_by(arkisto = True)
    m_arkistot = Muuta.query.filter_by(arkisto = True)
    new = h_new + t_new + e_new + m_new
    arkistoitu = False
    poistettu = False

    if request.form:

        for h_entry in h_entries:
            if ("h_" + str(h_entry.id)) in request.form.keys():
                if request.form[("h_" + str(h_entry.id))] == "arkisto":
                    h_entry.arkisto = True
                    arkistoitu = True
                elif request.form[("h_" + str(h_entry.id))] == "remove":
                    db.session.delete(h_entry)
                    poistettu = True
        for t_entry in t_entries:
            if ("t_" + str(t_entry.id)) in request.form.keys():
                if request.form[("t_" + str(t_entry.id))] == "arkisto":
                    t_entry.arkisto = True
                    arkistoitu = True
                elif request.form[("t_" + str(t_entry.id))] == "remove":
                    db.session.delete(t_entry)
                    poistettu = True
        for e_entry in e_entries:
            if ("e_" + str(e_entry.id)) in request.form.keys():
                if request.form[("e_" + str(e_entry.id))] == "arkisto":
                    e_entry.arkisto = True
                    arkistoitu = True
                elif request.form[("e_" + str(e_entry.id))] == "remove":
                    db.session.delete(e_entry)
                    poistettu = True
        for m_entry in m_entries:
            if ("m_" + str(m_entry.id)) in request.form.keys():
                if request.form[("m_" + str(m_entry.id))] == "arkisto":
                    m_entry.arkisto = True
                    arkistoitu = True
                elif request.form[("m_" + str(m_entry.id))] == "remove":
                    db.session.delete(m_entry)
                    poistettu = True
        for h_arkisto in h_arkistot:
            if ("h_" + str(h_arkisto.id)) in request.form.keys():
                if request.form[("h_" + str(h_arkisto.id))] == "remove":
                    db.session.delete(h_arkisto)
                    poistettu = True
        for t_arkisto in t_arkistot:
            if ("t_" + str(t_arkisto.id)) in request.form.keys():
                if request.form[("t_" + str(t_arkisto.id))] == "remove":
                    db.session.delete(t_arkisto)
                    poistettu = True
        for e_arkisto in e_arkistot:
            if ("e_" + str(e_arkisto.id)) in request.form.keys():
                if request.form[("e_" + str(e_arkisto.id))] == "remove":
                    db.session.delete(e_arkisto)
                    poistettu = True
        for m_arkisto in m_arkistot:
            if ("m_" + str(m_arkisto.id)) in request.form.keys():
                if request.form[("m_" + str(m_arkisto.id))] == "remove":
                    db.session.delete(m_arkisto)
                    poistettu = True
        db.session.commit()
        if arkistoitu:
            flash("Palaute arkistoitu")
        if poistettu:
            flash("Palaute poistettu")
        return redirect(appurl + '/admin')
    return render_template('admin.html', title='Palaute boxi',
                                         h_entries=h_entries,
                                         t_entries=t_entries,
                                         e_entries=e_entries,
                                         m_entries=m_entries,
                                         new=new,
                                         h_arkistot=h_arkistot,
                                         t_arkistot=t_arkistot,
                                         e_arkistot=e_arkistot,
                                         m_arkistot=m_arkistot,
                                         appurl=appurl)
