# coidng=utf-8
import json,requests
data = {"code":200,"msg":"成功","data":{"userId":4525388,"accessToken":"d1d10e2c3cf2478399822832ba4e8c9d","accessTokenV2":"f98e19881570448c84011106ff78f880","expireAt":1532762644465}}
userid = data["data"]["userId"]

pram ={"userId":userid}
print(pram)
