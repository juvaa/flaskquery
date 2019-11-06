from flask import render_template, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import Form
from app.models import Model
from datetime import datetime
from flask_basicauth import BasicAuth
import random
import os


appurl = os.environ.get("URL")
basic_auth = BasicAuth(app)

names = [
    "matti_", "veldoodles", "OlenAnanas", "nahka", "kala-", "Seinä", "Runtu", "elobubu", "Glukoosi", "sandalf", "jrintama", "Jupe_", "Jatana", "T3mu", "LateLJ", "Walden", "Leipo", "Pene", "Zhatelier", "sandalf", "Mega_Tron", "corile", "jsloth", "imhughbliss", "asor", "Nanni", "kilponen", "Oulaboi", "Pintti", "ippelixd"
]
words = [
    "Vauhtijuoksu", "is", "a", "speedrun-marathon", "organized", "by", "Oulun", "Tietoteekkarit", "ry.", "In", "the", "marathon,", "numerous", "players", "will", "challenge", "themselves", "in", "different", "video", "games,", "with", "the", "goal", "of", "finishing", "them", "as", "fast", "as", "possible.", "The", "first", "Vauhtijuoksu", "arranged", "in", "May", "was", "a", "great", "success;", "its", "fundraiser", "collecting", "almost", "6000", "euros", "for", "the", "children’s", "clinic", "of", "the", "Oulu", "University", "Hospital.", "The", "games", "played", "during", "the", "spring", "event", "can", "be", "viewed", "at", "Oulun", "Tietoteekkarit", "ry", "YouTube-channel.", "Building", "off", "of", "the", "first", "event’s", "success,", "this", "autumn", "we", "are", "launching", "Vauhtijuoksu+", "charity", "speedrun,", "this", "time", "welcoming", "all", "students", "of", "the", "university", "to", "apply", "for", "playing", "at", "the", "event.", "More", "information", "is", "available", "at", "https://vauhtijuoksu.otit.fi/.", "You", "can", "apply", "to", "play", "at", "the", "event", "starting", "NOW!", "Vauhtijuoksu+", "will", "take", "place", "on", "8.-10.11.2019", "at", "Tellus", "Business", "Kitchen", "and", "the", "event", "will", "be", "streamed", "to", "the", "internet", "using", "Twitch", "streaming", "service.", "The", "target", "for", "the", "charity", "fundraising", "hasn’t", "been", "decided", "yet", "and", "we", "are", "open", "for", "ideas!"
]
hashtags = [
    "vauhtista", "huutista", "swag", "menkäätöihin", "okboomer", "meetoo", "eimittää", "", "haloo", "luuranki"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    d = str(datetime.now().date()).split("-")
    form = Form()

    if form.validate_on_submit():
        flash('sent!')
        if not form.amount.data:
            amount = random.randint(1, random.randint(1, random.randint(1, 200)))
            if random.randint(0,10) == 0:
                name = "Anonyymi"
                message = ""
            else:
                name = names[random.randint(0,len(names)-1)]
                message = ""
                for i in range(0, random.randint(0, 15)):
                    message += " " + words[random.randint(0,len(words)-1)]
                for i in range(0, random.randint(0, random.randint(1, random.randint(1, 5)))):
                    message += " #" + hashtags[random.randint(0,len(hashtags)-1)]
                if message:
                    message = message[1:]
        else:
            amount = form.amount.data
            if form.name.data:
                name = form.name.data
            else:
                name = "Anonyymi"
            message = form.message.data

        sub = Model(
            Name=name,
            Amount=amount,
            Message=message,
            MessageAnswer="",
            CollectorImageUrl="",
            CurrencySymbol="€",
            CollectionUrl="/lahjaksitulevaisuus/6-3619",
            TransactionDate=d[2]+"."+d[1]+"."+d[0]
        )

        db.session.add(sub)
        db.session.commit()
        return redirect(appurl)



    return render_template('index.html', form=form)

@app.route('/donates', methods=['GET'])
def api():
    content = []
    if Model.query.first():
        content = Model.query.all()
    c = []
    for e in content:
        c.append({
            "DonationId": e.DonationId,
            "Name": e.Name,
            "Message": e.Message,
            "MessageAnswer": e.MessageAnswer,
            "CollectorImageUrl": e.CollectorImageUrl,
            "CurrencySymbol": e.CurrencySymbol,
            "CollectionUrl": e.CollectionUrl,
            "TransactionDate": e.TransactionDate
        })
    c = c[::-1]
    return jsonify(c)

