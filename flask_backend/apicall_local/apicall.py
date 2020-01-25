import json
from alpha_vantage.timeseries import TimeSeries

def get_ticker_info(ticker):
    k = []
    v = []
    ts = TimeSeries(key='FH0XYNHWNTKNS1PG')
    data, meta_data = ts.get_daily(ticker)
    for key, value in data.items():
        k.append(key)
        for key1, value1 in value.items():
            if key1 == "4. close":
                v.append(float(value1))
    v4 = v[:10]
    v4.reverse()
    k4 = k[:10]
    k4.reverse()
    k4 = json.dumps(k4).replace("\"","`")
    return (k4, v4)