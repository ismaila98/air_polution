from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine

#create app
app=Flask(__name__)

#connect to database
engine = create_engine('sqlite:///db.sqlite')

#define routes
@app.route('/')
def index():
    return render_template('heatmap.html')

@app.route('/heatmap')
def heatmap():
    conn = engine.connect()
    result = conn.execute("SELECT country, lat, lng, air_quality, water_pollution, population, mortality_rate FROM data")
    data_dict = {}
    for row in result:
        country = row[0]
        lat = row[1]
        lng = row[2]
        air_quality = row[3]
        water_pollution = row[4]
        population = row[5]
        mortality_rate = row[6]
        data_dict[country] = {'lat': lat,
                              'lng': lng,
                              'air_quality': air_quality,
                              'water_pollution': water_pollution,
                              'population': population,
                              'mortality_rate': mortality_rate}
    conn.close()
    return jsonify(data_dict)
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
