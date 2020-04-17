import json

from HiCityData import ForeCast
from ..app import app


@app.route("/forecast/<code>", methods=["GET"])
def get(code):
    # 101070101
    success, data = ForeCast.get_forecast_json(code)
    if not success:
        return json.dumps({"state": 404, "message": "invalid code or network error"})
    for i in data:
        print(i, " ", data[i])
    return json.dumps(data)
