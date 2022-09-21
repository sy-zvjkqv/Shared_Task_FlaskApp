from flask import Flask,render_template,request
import folium
from estimate import estimater
from map import view,first,second,third,polygon
app = Flask(__name__)
PREFIX="/texttolocation"
@app.route(PREFIX+"/")
def index():
    name = request.args.get("name")
    return render_template("index.html")

@app.route(PREFIX+"/index",methods=["post"])
def post():
    text = request.form["name"]
    select = request.form.get('radio')
    if select=="東京":
        code=estimater(text,select)
        zoom=10
    else:
        select="全国"
        code=estimater(text,select)
        zoom=6
    start_coords,sw,se,ne,nw=polygon(code,select)
    #folium_map=view(name,select)
    #folium_map.save('templates/map.html')
    return render_template("map.html",text=text,code=code, start_coords= start_coords,sw=sw,se=se,ne=ne,nw=nw,zoom=zoom)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5125)
    #app.run(debug=True,port=5001)
