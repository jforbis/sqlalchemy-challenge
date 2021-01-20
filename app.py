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
        f"/api/v1.0/stationlist<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

# Precipitation - Route Works
# Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation/")
def precipitation():
    session = Session(engine)
    results = session.query(measurements.date, measurements.prcp).all()

    prcp_data = []
    for date, prcp in results:
        dict_data = {}
        dict_data[date] = prcp
        prcp_data.append(dict_data)

    session.close()
    
    return jsonify(prcp_data)

# Station List - Route Works but not every time
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stationlist/")
def stationlist():
    session = Session(engine)
    results = session.query(stations.station, stations.name).all()
    station_data = {}
    for station, name in results:
        station_data[station] = name

    session.close()
    return jsonify(station_data)

# Tobs - Route Works but not every time
# Query the dates and temperature observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs/")
def tobs():
    session = Session(engine)

    recent_date = session.query(measurements.date).order_by(measurements.date.desc()).first()
    recent_date_minus1year = (dt.datetime.strptime(recent_date[0],'%Y-%m-%d')-dt.timedelta(days=365)).strftime('%Y-%m-%d')

    results = session.query(measurements.date, measurements.tobs).filter(measurements.date >= recent_date_minus1year).order_by(measurements.date).all()

    date_data = []
    for date,tobs in results:
        dict_data = {}
        dict_data[date] = tobs
        date_data.append(dict_data)    
    session.close()
    return jsonify(date_data)

# Start/End?
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine)

    results = session.query(func.min(measurements.tobs), func.avg(measurements.tobs), func.max(measurements.tobs)).filter(measurements.date >= start).all()

    tobs_data = []
    for min, avg, max in results:
        tobs_dict = {}
        tobs_dict["min"] = min
        tobs_dict["mean"] = avg
        tobs_dict["max"] = max
    session.close()
    return jsonify(tobs_dict)

# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>/<end>")
def start_date(start, end):
    session = Session(engine)

    results = session.query(func.min(measurements.tobs), func.avg(measurements.tobs), func.max(measurements.tobs)).filter(measurements.date >= start).filter(measurements.date <= end).all()

    tobs_data = []
    for min, avg, max in results:
        tobs_dict = {}
        tobs_dict["min"] = min
        tobs_dict["mean"] = avg
        tobs_dict["max"] = max
    session.close()
    return jsonify(tobs_dict)

# HINTS:
# You will need to join the station and measurement tables for some of the queries.

# Use Flask `jsonify` to convert your API data into a valid JSON response object.

if __name__ == '__main__':
    app.run(debug=True)