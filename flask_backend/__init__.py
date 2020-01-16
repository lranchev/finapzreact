
from flask import Flask
import flask
from alpha_vantage.timeseries import TimeSeries

app = Flask(__name__)
k = []
v = []
@app.route("/")


def my_index():
    ts = TimeSeries(key='FH0XYNHWNTKNS1PG')
    data, meta_data = ts.get_daily('AKAM')
    token_str = "Hello world of react and Flask with a variable in the function"
    for key, value in data.items():
        k.append(key)
        for key1, value1 in value.items():
            if key1 == "4. close":
                v.append(value1)
    return flask.render_template("index.html",token=k[:4],token2=v[:4])


#    return flask.render_template("index.html",token=data)


# def test():
#     d = {"2019-08-23":{"1. open":"88.3300","2. high":"89.9571","3. low":"86.6800","4. close":"86.9900","5. volume":"1239091"},"2019-08-26":{"1. open":"88.4500","2. high":"88.4500","3. low":"87.0600","4. close":"87.8500","5. volume":"766175"},"2019-08-27":{"1. open":"88.6800","2. high":"89.2900","3. low":"87.2501","4. close":"88.2100","5. volume":"1126970"}}
#     #token_str = "Hello world of react and Flask with a variable in the function"
#     for key, value in d.items():
#         a.append(key)
#     return flask.render_template("index.html",token=a)