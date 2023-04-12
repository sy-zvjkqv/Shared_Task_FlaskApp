from flask import Flask, render_template, request
from estimate import geo_code_estimater
from map import polygon

app = Flask(__name__)
PREFIX = "/texttolocation"


@app.route(PREFIX + "/")
def index():
    name = request.args.get("name")
    return render_template("index.html")


@app.route(PREFIX + "/index", methods=["post"])
def post():
    tweet_text = request.form["name"]
    region = request.form.get("radio")
    geo_code = geo_code_estimater(tweet_text, region)
    if region == "全国" or region == None:
        zoom = 6
    else:
        zoom = 10
    start_coords, sw, se, ne, nw = polygon(geo_code, region)
    return render_template(
        "map.html",
        tweet_text=tweet_text,
        geo_code=geo_code,
        start_coords=start_coords,
        sw=sw,
        se=se,
        ne=ne,
        nw=nw,
        zoom=zoom,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=10000)
    # app.run(debug=True, port=5001)
