from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine

#create app
app=Flask(__name__)

#connect to database
engine = create_engine('sqlite:///data/db.sqlite')

@app.route('/data')
def data():
    return jsonify(['a','b','c'])

#define routes
@app.route('/')
def index():
    return render_template('index_pie.html')

@app.route('/heatmap')
def heatmap():
    conn = engine.connect()
    result = conn.execute("SELECT Country, 'population of country', City, AirQuality, WaterPollution, 'population of city', lat, lng, 'proportion of population', 'Mortality rate of country (per 100,000)', 'Gross domestic product ($ billions)', 'Agriculture (% of GDP)', 'Industry (% of GDP)', 'Manufacturing (% of GDP)', 'Services (% of GDP)', 'Weighted mortality rate of city (per 100,000)' FROM data")
    data_dict = {}
    for row in result:
        country = row[0]
        country_population = int(row[1])
        city = row[2]
        air_quality = int(row[3])
        water_pollution = int(row[4])
        city_population = int(row[5])
        lat = int(row[6])
        lng=int(row[7])
        percentage_population=int(row[8])
        country_mortality_rate=int(row[9])
        gdp=int(row[10])
        agriculture=int(row[11])
        industry=int(row[12])
        manufacturing=int(row[13])
        services=int(row[14])
        weighted_mortality_rate=int(row[15])
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
