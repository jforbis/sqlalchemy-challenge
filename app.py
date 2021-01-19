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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Precipitation
# Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation/")

def precipitation():
    session = Session(engine)
    results = session.query(measurements.date, measurements.prcp).order_by(measurements.date).all()

    prcp_data = []
    for date, prcp in results:
        dict_data = {}
        dict_data[date] = prcp
        prcp_data.append(dict_data)

    session.close()

    return jsonify(prcp_data)

# Stations
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")

def station():
    session = Session(engine)
    results = session.query(stations.id, stations.name).order_by(stations.id).all()
    station_data = []
    for id, name, station in results:
        dict_data = {}
        dict_data[id] = name
        station_data.append(dict_data)

    session.close()
    return results

# Tobs
# Query the dates and temperature observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.

# Start/End?
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


# HINTS:
# You will need to join the station and measurement tables for some of the queries.

# Use Flask `jsonify` to convert your API data into a valid JSON response object.