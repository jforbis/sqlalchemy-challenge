# sqlalchemy-challenge

In this project I created a jupyter notebook file that read a _sqllite_ database, performed a few queries on two different tables in the database and then used the _func_ method to calculate date ranges. These calculations looked at precipitation amounts at specific weather stations, obtained temperatures for each day from 2010-2017, and then found the min and max values of temperature for a years worth of the data.

The second part of the project utilized the _flask_ app to generate _sqllite_ query results onto a localhost website. I created five different routes (endpoints) for the website and each pointed to different queries that I accomplished previously with my jupyter notebook file.

### Flask App Routes & Info Generated Per Route:
1. /api/v1.0/precipitation
    * This route will show you a list of precipitation by each day for all weather stations.
    <img src="images/precipitation.jpg">
2. /api/v1.0/stationlist
    * This route will show you a list of all the weather stations
    <img src="images/station-list.jpg">

3. /api/v1.0/tobs
    * This route will show you all temperature information
    <img src="images/tobs.jpg">

4. /api/1.0/start
    * This route will show you the minimum, max, and average (mean) temperatures of all dates GREATER than the date you put in
    * Please enter your date in this format yyyy-mm-dd
    <img src="images/start.jpg">
 
5. /api/v1.0/start/end
    * This route will show you the minimum, max, and average (mean) temperatures of all dates BETWEEN the START and END dates you put in
    <img src="images/start-end.jpg">
    
