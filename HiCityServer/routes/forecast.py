import asyncio
import json
import time
from multiprocessing import Process

from HiCityData import ForeCast
from ..app import app
from ..crontab.caches import ForeCastCache
from ..crontab.tools import Tool


async def request(code):
    success, data = ForeCast.get_forecast_json(code)
    return success, data


def request_get(code):
    if (code not in ForeCastCache.data) or (Tool.get_regular_now() not in ForeCastCache.data[code]):
        success, data = asyncio.run(request(code))
        if success:
            ForeCastCache.add(code, data["forecast"])
        else:
            return json.dumps({"state": 404, "message": "invalid code"})
    js = json.loads(ForeCastCache.data[code][Tool.get_regular_now()])
    return json.dumps(js["all"])


def heavyTask_5s():
    time.sleep(5)
    print("sleep 5s over")


def heavyTask_10s():
    time.sleep(10)
    print("sleep 10s over")


@app.route("/forecast/<code>", methods=["GET"])
def get(code):
    Process(target=heavyTask_5s).start()
    Process(target=heavyTask_10s).start()
    return request_get(code)
