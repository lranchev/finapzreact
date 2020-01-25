import json
from flask import Flask
import flask
from flask_backend.apicall_local import get_ticker_info

app = Flask(__name__)



@app.route("/")
def main():
    amaz_d, amaz_p = get_ticker_info('AMZN')
    akam_d, akam_p = get_ticker_info('AKAM')
    # return flask.render_template("index.html",token1=amaz_d,token2=amaz_p)
    return flask.render_template("index.html", token1=amaz_d, token2=amaz_p, token3=akam_d, token4=akam_p)


# main(amaz_d,amaz_p,akam_d,akam_p)


#    return flask.render_template("index.html",token=data)


# def test():
#     d = {"2019-08-23":{"1. open":"88.3300","2. high":"89.9571","3. low":"86.6800","4. close":"86.9900","5. volume":"1239091"},"2019-08-26":{"1. open":"88.4500","2. high":"88.4500","3. low":"87.0600","4. close":"87.8500","5. volume":"766175"},"2019-08-27":{"1. open":"88.6800","2. high":"89.2900","3. low":"87.2501","4. close":"88.2100","5. volume":"1126970"}}
#     #token_str = "Hello world of react and Flask with a variable in the function"
#     for key, value in d.items():
#         a.append(key)
#     return flask.render_template("index.html",token=a)
