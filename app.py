#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify, render_template,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb+srv://am4:MM412Proj@cluster0.kfpl9.mongodb.net/dehack?ssl=true&ssl_cert_reqs=CERT_NONE"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route('/')
def index():
    return render_template('index.html', title="Pearsist | We make sure that you eat healthy")

@app.route("/foodtool/")
def foodtool():
    return render_template('foodtool.html', title="Pearsist | We make sure that you eat healthy")

@app.route("/community/")
def community():
    return render_template('community.html', title="Pearsist | We make sure that you eat healthy")

@app.route("/events/")
def events():
    return render_template('events.html', title="Pearsist | We make sure that you eat healthy")

@app.route("/contact/")
def contact():
    return render_template('contact.html', title="Pearsist | We make sure that you eat healthy")

@app.route("/search_zip/")
def search_zip():
    query = request.args.get('search')
    farms = db.farms.find({"Zip": query})
    return render_template('farms.html', farms= farms, 
    title="Pearsist | We make sure that you eat healthy")


def farm_info():
    todo = db.farms.find_one_or_404({"City": "Ashburnham"})
    print('t', todo)
    return jsonify(message= str(todo))


@app.route('/farms/',methods=['GET','POST'])
def all_farms():
    if request.method == 'GET':
        all_farms = db.farms.find({})
    
    return render_template('farms.html', farms= all_farms, 
    title="Pearsist | We make sure that you eat healthy")

@app.route('/farm/<ObjectId:fid>')
def farm(fid):
    farmInfo = db.farms.find_one_or_404({'_id': fid})
    print('farm', farmInfo)
    return render_template('farm-info.html', farm= farmInfo, 
    title="Pearsist | We make sure that you eat healthy")

if __name__ == "__main__":
    import sys, os
    if len(sys.argv) > 1:
        # arg, if any, is the desired port number
        port = int(sys.argv[1])
        assert(port>1024)
    else:
        port = os.getuid()
    app.debug = True
    app.run()