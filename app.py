from flask import Flask, jsonify, render_template
import requests
from numerize.numerize import numerize

app = Flask(__name__)

CHANNELS = {
    'qazi': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
    'mrbeast': 'UCX6OQ3DkcsbYNE6H8uQQuVA',
    'mkbhd': 'UCBJycsmduvYEL83R_U4JriQ',
    'pm': 'UC3DkFux8Iv-aYnTRWzwaiBA',
    'lloud':'UC6-BgjsBa5R3PZQ_kZ8hKPg'
}


@app.route('/')
def index():
    url = "https://yt-api.p.rapidapi.com/channel/videos"

    querystring = {"id": CHANNELS['mrbeast']}

    headers = {
        "x-rapidapi-key": "8aadc37053msh48669ed89c80e2cp1f1eb6jsn2d28ec5d5657",
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    datas = response.json()
    contents = datas['data']
    return render_template('index.html', contents=contents)


@app.template_filter()
def numberize(views):
    if isinstance(views, str):
        import re
        numbers_only = re.sub(r'[^\d]', '', views)
        numbers_only = numbers_only.replace(',', '')
        if numbers_only:
            return numerize(int(numbers_only), 1)
        else:
            return views
    return numerize(int(views), 1)


app.run()