from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine

#create app
app=Flask(__name__)

#connect to database
engine = create_engine('sqlite:///data/db.sqlite')

#define routes
@app.route('/')
def index():
    return render_template("dashboard.html")


@app.route('/heatmap')
def heatmap():
    conn = engine.connect()
    result = conn.execute("SELECT * FROM data")
    data_dict = {}
    for row in result:
        country = row[0]
        country_population = row[1]
        city = row[2]
        air_quality = row[3]
        water_pollution = row[4]
        city_population = row[5]
        lat = row[6]
        lng=row[7]
        percentage_population=row[8]
        country_mortality_rate=row[9]
        gdp=row[10]
        agriculture=row[11]
        industry=row[12]
        manufacturing=row[13]
        services=row[14]
        weighted_mortality_rate=row[15]
        data_dict[country] = {'country': country,
                              'country_population': country_population,
                              'city': city,
                              'air_quality': air_quality,
                              'water_pollution': water_pollution,
                              'city_population': city_population,
                              'lat': lat,
                              'lng': lng,
                              'percentage_population': percentage_population,
                              'country_mortality_rate': country_mortality_rate,
                              'gdp': gdp,
                              'agriculture':agriculture,
                              'industry': industry,
                              'manufacturing': manufacturing,
                              'services': services,
                              'weighted_mortality_rate': weighted_mortality_rate}
    conn.close()
    return jsonify(data_dict)
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
