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
            datetime = nowtime
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)
    return render_template('index.html', title='Palautetta OTiT:lle',
                                         form=form,
                                         appurl=appurl)


@app.route('/admin', methods=['GET'])
@basic_auth.required
def admin():
    h_entrys = Model.query.all()
    h_count = Model.query.count()
    return render_template('admin.html', title='Palaute boxi',
                                         h_entrys=h_entrys,
                                         h_count=h_count,
                                         appurl=appurl)
