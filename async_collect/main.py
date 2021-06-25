import aiohttp
from flask import Flask, jsonify

app = Flask(__name__)
# numbers of api
API_NUMS = 3


@app.route('/')
async def collect():
    result = []
    url = 'http://172.17.0.1:8000/remote/{}'
    async with aiohttp.ClientSession() as session:
        for i in range(1,API_NUMS+1):
            async with session.get(url.format(i),timeout=2) as response:
                resp = await response.json()
                if isinstance(resp,list):
                    resp = resp
                else:
                    resp = []
                result.extend(resp)

    # sort lists by dict value
    sorted_l = sorted(result,key=lambda k:k['id'])

    return jsonify(sorted_l)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
