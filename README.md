# air_polution project

![Alt text](https://tse4.mm.bing.net/th?id=OIP.9CHU8At7mmETOCicvJyNgQHaE8&pid=Api&P=0)
-------------------------------------
Presentation-https://prezi.com/view/xBYjOGb65rZfOgURz8ZC/
## Overview

In the first part of our project, we took four different datasets from online. These included one for Mortalilty Rate for Air Pollution from WHO, country GDP from Worldbank, World air and water quality from IQAir, and a database with lat/long for countries across the world.
We then did multiple merges of these datasets, cleaning them so that we had the columns we wanted in one table. We also added a weighted mortality rate, which took the mortality rate of each city within the country and multiplied that by what proportion of the country's population that city was.
The data was then loaded into an SQLite database. We created the Flask app which created the endpoint of "heatmap" to pull all of the columns from the database so that it is accessible for the visualization files, thus being the link between the database and webpage. 


## Resources

- WHO: Mortality rate for all polution dataset https://www.who.int/data/gho/data/indicators/indicator-details/GHO/ambient-and-household-air-pollution-attributable-death-rate-(per-100-000-population)

- WorldBank: Sector of GDP % per country 
    http://wdi.worldbank.org/table/4.2

- IQAir: World cities air quality and water pollution https://www.kaggle.com/datasets/cityapiio/world-cities-air-quality-and-water-polution

- Kaggle: Lat/Lng info for world cities https://www.kaggle.com/datasets/juanmah/world-cities




## Instructions

### Step 1: ETL
- Import dependencies and read in the CSV files using Pandas
- Clean the data and ensure that all columns are named consistently through out all of the 4 datasets.
- Merge 2 datasets at a time and merge the 2 merged datasets to output a final DF that includes all of the useful columns that we decided to keep.
- Create an engine that creates a sqlite file and pass our final DF to the sqlite file.
 
### Step 2: Flask 
Create an app to house, jsonyfying, and send all data to a local host. The flask app served the data from the SQlite database to 5000/heatmap.



### Step 3: Visualizations 
The visualizations below capture the results of our analysis 
 * A heat map with a drop down function to view three different analysis:
    * Mortality by weighted population of countries
    * Air Quality by weighted population of countries 
    * Water Pollution by weighted populaiton of contries 
* Chart showing populated countries by their average pollution results: 
    * Population- 20 most populated countries
    * AirQuality Average-  of the 20 most populated countries
    * Water Pollution Average- of the 20 most populated countries 
* Pie Chart analyzing each countries GDP contributions
    * Manufacturing 
    * Agriculture
    * Industry
    * Services
 
 
