import json
from flask import Flask
import flask
from alpha_vantage.timeseries import TimeSeries

app = Flask(__name__)

@app.route("/")


def my_index(ticker):
    k = []
    v = []
    print(ticker, 'testing')
    ts = TimeSeries(key='FH0XYNHWNTKNS1PG')
    print(ticker, 'testing')
    data, meta_data = ts.get_daily(ticker)
    # token_str = "Hello world of react and Flask with a variable in the function"
    for key, value in data.items():
        k.append(key)
        for key1, value1 in value.items():
            if key1 == "4. close":
                v.append(float(value1))
    v4 = v[:4]
    v4.reverse()
    k4 = k[:4]
    k4.reverse()
    k4 = json.dumps(k4).replace("\"","`")
    # k4 = k4.replace("-","")
    return (k4, v4)


amaz_d, amaz_p = my_index('AMZN')
akam_d, akam_p = my_index('AKAM')

print(f"{ amaz_d = }")
print(f"{ amaz_p = }")

print('akam_d: {1}, akam_p: {0}'.format(akam_d, akam_p))




#    return flask.render_template("index.html",token=data)


# def test():
#     d = {"2019-08-23":{"1. open":"88.3300","2. high":"89.9571","3. low":"86.6800","4. close":"86.9900","5. volume":"1239091"},"2019-08-26":{"1. open":"88.4500","2. high":"88.4500","3. low":"87.0600","4. close":"87.8500","5. volume":"766175"},"2019-08-27":{"1. open":"88.6800","2. high":"89.2900","3. low":"87.2501","4. close":"88.2100","5. volume":"1126970"}}
#     #token_str = "Hello world of react and Flask with a variable in the function"
#     for key, value in d.items():
#         a.append(key)
#     return flask.render_template("index.html",token=a)