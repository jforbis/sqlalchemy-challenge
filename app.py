# Dependencies
import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_

from flask import Flask, jsonify

# Setting up connection
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Database tables
measurements = Base.classes.measurement
stations = Base.classes.station 

# App info
app = Flask(__name__)

# Routes
# Home Page
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

# Precipitation

# Stations
# Tobs
# Start/End?