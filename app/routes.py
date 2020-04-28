from flask import render_template, flash, redirect
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
    h_entrys = Model.query.with_entities(Model.hallitus)
    t_entrys = Model.query.with_entities(Model.tapahtuma)
    e_entrys = Model.query.with_entities(Model.ehdotus)
    m_entrys = Model.query.with_entities(Model.muuta)
    count = Model.query.count()
    return render_template('admin.html', title='Palaute boxi',
                                         h_entrys=h_entrys,
                                         t_entrys=t_entrys,
                                         e_entrys=e_entrys,
                                         m_entrys=m_entrys,
                                         count=count,
                                         appurl=appurl)
