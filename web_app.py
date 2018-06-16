import urllib.request
import requests
import json
import time
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_script import Domain, Url, Base, IP
from config import *


app = Flask(__name__)


@app.route('/')
def main_page():
    rows = session.query(Url.url, Url.submission, Url.resource).order_by(Url.id)[0:25]
    return render_template('MainPage.html', rows=rows)


@app.route('/CheckDomain', methods=['POST', 'GET'])
def check_domain():
    if request.method == 'POST':
        dom = request.form['InputDomain']
        rows = session.query(Url.url, Url.submission, Url.resource).filter(Domain.domain == dom).filter(Url.domain_id == Domain.id).all()
        if rows:
            answer = "This domain exists in database"
            return render_template('Domain.html', answer=answer, rows=rows)
        else:
            answer = "This domain doesn't exist in database"
            return render_template('Domain.html', answer=answer)
    else:
        return render_template('Domain.html')


@app.route('/CheckUrl', methods=['POST', 'GET'])
def check_url():
    if request.method == 'POST':
        link = request.form['InputLink']
        row = session.query(Url.url, Url.submission).filter(Url.url == link).first()
        if not row:
            answer = json.dumps('The link was not found in base')
        else:
            t = row.submission.split('T')
            s = t[1].split('+')
            p = time.strftime("%d.%m.%Y", time.strptime(t[0], "%Y-%m-%d"))
            answer = json.dumps('The link exists in base. Submission time: '+s[0]+' '+p)
        return render_template('Url.html', answer=answer)
    else:
        return render_template('Url.html')


@app.route('/CheckIP', methods=['POST', 'GET'])
def check_ip():
    if request.method == 'POST':
        ip = request.form['InputIP']
        row = session.query(IP.ip).filter(IP.ip == ip).first()
        if not row:
            answer = json.dumps('IP was not found in base')
        else:
            answer = json.dumps('IP exists in base.')
        return render_template('IP.html', answer=answer)
    else:
        return render_template('IP.html')


if __name__ == "__main__":
    engine = create_engine('sqlite:///DBMaliciousURL.db', echo=True)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    app.run(debug=True)
