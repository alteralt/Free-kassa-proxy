from aiohttp import web

import utils
from configreader import Config


async def free_kassa_notification(request: web.Request):
    config: Config = request.app["config"]

    # Список ip free-kassы на этой странице https://docs.freekassa.ru/#section/1.-Vvedenie/1.4.-Opoveshenie-o-platezhe
    allowed_ips = ["168.119.157.136", "168.119.60.227", "138.201.88.124", "178.154.197.79"]
    # if request.headers.get("cf-connecting-ip") not in allowed_ips:
    #     raise web.HTTPUnauthorized

    kwargs = {
        "params": dict(request.query),
        "data": await request.post(),
    }
    print(config.notification_url)
    print(kwargs)
    response = await utils.request(
        request.method, str(config.notification_url), **{key: value for key, value in kwargs.items() if value}
    )
    return web.Response(body=await response.text(), headers=response.headers, status=response.status)


# Сюда редиректит пользователя при удачной оплате
async def free_kassa_success(request: web.Request):
    config: Config = request.app["config"]

    response = await utils.request(request.method, str(config.success_url))
    return web.Response(body=await response.text(), headers=response.headers, status=response.status)


# Сюда редиректит пользователя при неудачной оплате
async def free_kassa_failure(request: web.Request):
    config: Config = request.app["config"]

    response = await utils.request(request.method, str(config.failure_url))
    return web.Response(body=await response.text(), headers=response.headers, status=response.status)


routes = [
    web.route("*", "/free-kassa/notification", free_kassa_notification),
    web.get("/free-kassa/success", free_kassa_success),
    web.get("/free-kassa/failure", free_kassa_failure),
]


app = web.Application()
app["config"] = Config()
app.add_routes(routes)

web.run_app(app, host="127.0.0.1", port=8001)
