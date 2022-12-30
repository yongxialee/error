from flask import Flask, render_template,request
from models import Todo,connect_db
from flask import Flask,request ,render_template,redirect,session,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,Todo


app = Flask(__name__)
# i need you to talk to postgresql using database movies_example
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///todos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ThisisHappyyuy123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
debug = DebugToolbarExtension(app)
app.debug = True
app.app_context().push()
# call connect_db
connect_db(app)





















############## other practice ############

# import requests

# API_BASE_URL = 'http://www.mapquestapi.com/geocoding/v1'
# key = 'r6m58hHfRdC1ULRYmjG9FHtZDgTfPbU8'

# from flask import Flask, request, jsonify
# from models import db, connect_db

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///todos_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

# connect_db(app)
# app.app_context().push()

# app = Flask(__name__)

# @app.route('/')
# def show_address_form():
#     return render_template("address_form.html")
# @app.route('/geocode')
# def get_location():
#     address = request.args["address"]
#     res = requests.get(f"{API_BASE_URL}/address",params={'key':key, 'location':address})
    
    
#     data = res.json()
#     lat =data["results"][0]["locations"][0]['latLng']['lat']
#     lng = data["results"][0]["locations"][0]['latLng']['lng']
#     print("*****************")
#     print(lat,lng)
    
#     coords={'lat':lat,'lng':lng}
#     return render_template('address_form.html',coords=coords)