from flask import Flask, jsonify
import numpy as np
import time 
import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Station = Base.classes.station
Measurement = Base.classes.measurement

app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<b> Welcome </b>"
        f"<br/>"
        f"<br/>"
        f"Available Routes: <br/>"
        f"<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"<br/>"
        f"/api/v1.0/stations <br/>"
        f"<br/>"
        f"/api/v1.0/tobs <br/>"
        f"<br/>"
        f"/api/v1.0/start/(date) <br/>"
        f"<br/>"
        f"/api/v1.0/start/end/(start_date)/(end_date)"
    )

@app.route("/api/v1.0/precipitation")
def precipitation(): 

    session = Session(engine)
    results = session.query(Measurement.date,Measurement.prcp).all()
    session.close()

    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/stations")
def stations(): 

    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()

    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs(): 

    session = Session(engine)
    Recent_Date = session.query(Measurement.date).order_by(Measurement.date.desc()).limit(10).all()
    Last_Date = Recent_Date[0][0]

    Last_Unix = time.mktime(datetime.datetime.strptime(Last_Date,"%Y-%m-%d").timetuple())
    First_Unix = round(Last_Unix - 31500000)
    First_Date = datetime.datetime.fromtimestamp(First_Unix).strftime('%Y-%m-%d')

    Twelve_Month_Query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= First_Date).all()
                                 
    session.close()

    all_months = list(np.ravel(Twelve_Month_Query))

    return jsonify(all_months)


@app.route("/api/v1.0/start/<start>")

def start_only(start): 

    session = Session(engine)

    func_start = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    session.close()

    all_maxs = list(np.ravel(func_start))

    return jsonify(all_maxs)


@app.route("/api/v1.0/start/end/<start>/<end>")

def start_end(start,end): 

    session = Session(engine)

    func_start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all() 
    
    session.close()

    all_max = list(np.ravel(func_start_end))

    return jsonify(all_max)


if __name__ == "__main__":
    app.run(debug=True)

