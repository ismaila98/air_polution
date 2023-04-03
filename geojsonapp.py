from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
import geojson

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
    features = []
    for row in result:
        feature = geojson.Feature(
            geometry=geojson.Point((row[2], row[1])),
            properties={
                'country': row[0],
                'air_quality': row[3],
                'water_pollution': row[4],
                'population': row[5],
                'mortality_rate': row[6]
            }
        )
        features.append(feature)
    conn.close()
    feature_collection = geojson.FeatureCollection(features)
    return jsonify(feature_collection)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
