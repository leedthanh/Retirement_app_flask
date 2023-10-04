from flask import Flask, render_template, send_file

app = Flask(__name__)

# Define a route to serve the GeoJSON file
# if go the route it will automatically download the geojson file
@app.route('/bestNS')
def bestNS():
    filename = 'static/DatasetManipulations/best_nsHomes.json'
    return send_file(filename, as_attachment=False)

@app.route('/dashboardjson')
def dashboardjson():
    geojson_filename3 = 'static/DatasetManipulations/dashboard_tx.json'
    return send_file(geojson_filename3, as_attachment=False)

@app.route('/geojson')
def geojson():
    geojson_filename = 'static/DatasetManipulations/All_nursing_homes.geojson'
    return send_file(geojson_filename, as_attachment=False) 

# adding route for 5 stars nursing home 
@app.route('/mappingjson')
def another_geojson():
    geojson_filename2 = 'static/DatasetManipulations/mapping.json'
    return send_file(geojson_filename2, as_attachment=False) 

# Define routes for your existing pages
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/maps')
def maps():
    return render_template("homesInMaps.html")

@app.route('/Dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)