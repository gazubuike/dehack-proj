#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify, render_template, url_for
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_parameter, get_page_args
#from mongonator import MongoClientWithPagination, ASCENDING

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb+srv://am4:MM412Proj@cluster0.kfpl9.mongodb.net/farms?ssl=true&ssl_cert_reqs=CERT_NONE"
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

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 12

    totalLen = farms.count()
    pagination = Pagination(page=page, per_page=per_page, total= totalLen, 
        record_name='farms')

    return render_template('farms.html', farms= farms, total =totalLen, pagination=pagination,
    title="Pearsist | We make sure that you eat healthy")

def skiplimit(page_size, page_num):
        """returns a set of documents belonging to page number `page_num`
        where size of each page is `page_size`.
        """
        # Calculate number of documents to skip
        skips = page_size * (int(page_num/page_size) - 1)

        if skips < 0:
            skips = 0
        
        print('skip', skips, 'pages', page_size,'num', page_num )
        # Skip and limit
        cursor = db['farms'].find().skip(skips).limit(page_size)
        print('curs', [x for x in cursor])

        # Return documents
        return [x for x in cursor]

def getSelectFarms(offset=0, per_page=12):

    farms = db.farms.find({})
    farmList = [x for x in farms]
    return farmList[offset: offset + per_page]



@app.route('/farms/',methods=['GET','POST'])
def all_farms():
    
    """ col = db.farms

    query_filter = {}

    all_pages = []
    #  Paginate automatically in batches of 5
    for d in col.paginate(query=query_filter, limit=5,
                            ordering_field='LocationName', ordering=ASCENDING):
        all_pages.append(d.response)                    
        print(d.response)
        print(d.batch_size)    """
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    per_page = 12                            
    pagination_farms = getSelectFarms(offset=offset, per_page=per_page)

    
    if request.method == 'GET':
        # Set the pagination configuration
        #all_farms = db.farms.find({})
        all_farms = db.farms.find({})

        totalLen =all_farms.count()

        

        pagination = Pagination(page=page, per_page=per_page, total= totalLen, 
        record_name='farms')
    
    return render_template('farms.html', farms= pagination_farms,
                           page=page,
                           per_page=per_page,
                           pagination=pagination, total=totalLen, title="Pearsist | We make sure that you eat healthy")


""" @app.route('/farms/<int:pageNum>',methods=['GET','POST'])
def all_farms(pageNum):

    
    if request.method == 'GET':
        # Set the pagination configuration
        #all_farms = db.farms.find({})
        all_farms = skiplimit(10, pageNum)
    
    return render_template('farms.html', farms= all_farms, 
    title="Pearsist | We make sure that you eat healthy") """



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