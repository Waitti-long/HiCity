import json

from HiCityData import ForeCast
from ..crontab.caches import ForeCastCache
from ..crontab.tools import Tool
from ..app import app


@app.route("/forecast/<code>", methods=["GET"])
def get(code):
    if code not in ForeCastCache.data:
        success, data = ForeCast.get_forecast_json(code)
        if success:
            ForeCastCache.add(code, data["forecast"])
        else:
            return json.dumps({"state": 404, "message": "invalid code"})
    if Tool.get_regular_now() not in ForeCastCache.data[code]:
        success, data = ForeCast.get_forecast_json(code)
        if success:
            ForeCastCache.add(code, data["forecast"])
        else:
            return json.dumps({"state": 404, "message": "something error"})
    js = json.loads(ForeCastCache.data[code][Tool.get_regular_now()])
    return json.dumps(js["all"])

