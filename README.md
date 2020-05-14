# Temperature Analysis of Honolulu, HI 
<br> 


### Programs used - SQLalchemy & Flask 

## Background 
<br>
Climate analysis needs to be done on Honolulu before we take a trip by analysing precipitation and temperature data from 2010 to 2017 

## Precipitation Analysis 
<br>
    (1) Design a query to retrieve the last 12 months of precipitation data.
    (2) Select only the date and prcp values.
    (3) Load the query results into a Pandas DataFrame and set the index to the date column.
    (4) Sort the DataFrame values by date.
    (5) Plot the results using the DataFrame plot method.
    
## Station Analysis 
<br>
    (1) Design a query to calculate the total number of stations.
    (2) Design a query to find the most active stations.
           .List the stations and observation counts in descending order.
           .Which station has the highest number of observations?
    (3) Design a query to retrieve the last 12 months of temperature observation data (TOBS)
           .Filter by the station with the highest number of observations.
           .Plot the results as a histogram with bins=12.
           
## Climate App 
<br>

#### /Home .

List all routes that are available.

#### /api/v1.0/precipitation

Convert the query results to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.

#### /api/v1.0/stations

Return a JSON list of stations from the dataset.

#### /api/v1.0/tobs

Query the dates and temperature observations of the most active station for the last year of data.

Return a JSON list of temperature observations (TOBS) for the previous year.

#### /api/v1.0/start and /api/v1.0/start/end

Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

## Bonus 

### Temperature Analysis I 

Identify the average temperature in June at all stations across all available years in the dataset. Did the same for December temperature.

Use the t-test to determine whether the difference in the means, if any, is statistically significant. 

### Temperature Analysis II 

The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.

Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

Plot the min, avg, and max temperature from your previous query as a bar chart.

Use the average temperature as the bar height.

Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

