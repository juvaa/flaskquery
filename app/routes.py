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

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    nowtime = datetime.now()

    entrys = Model.query.all()
    count = Model.query.count()

    if form.validate_on_submit():
        flash('Thank you for participating')
        sub = Model(
            string = form.string.data,
            boolean = form.boolean.data,
            radio = form.string.data,
            text = form.text.data,
            datetime = nowtime,
        )
        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)
    return render_template('index.html', title='Query',
                                         entrys=entrys,
                                         count=count,
                                         nowtime=nowtime,
                                         form=form,
                                         appurl=appurl)


@app.route('/admin', methods=['GET'])
@basic_auth.required
def admin():
    entrys = Model.query.all()
    count = Model.query.count()
    return render_template('admin.html', title='Query',
                                         entrys=entrys,
                                         count=count,
                                         appurl=appurl)