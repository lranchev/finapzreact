from flask import Flask
import flask
from alpha_vantage.timeseries import TimeSeries


app = Flask("__main__")

@app.route("/")
def my_index():
    ts = TimeSeries(key='FH0XYNHWNTKNS1PG')
    data, meta_data = ts.get_daily('AKAM')
    datastr = str(meta_data)
    token_str = "Hello world of react and Flask with a variable in the function"
    return flask.render_template("index.html",token=datastr)

app.run(debug=True)