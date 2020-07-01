# spending-visualizer
Tableau visualizations of consumer spending data over 34 years (from BLS API) to discover interesting trends
Data: in tableau_friendly_results.csv (scraped by running main.py) and displayed in visualization.twbx
Note that can specify the BLS series to analyze by adding results from [search](https://beta.bls.gov/dataQuery/find?fq=survey:[cx]&s=popularity:D) to hasSeriesID.csv 

Data was divided into four regions: Midwest, Northeast, South, West
Interesting results:
* The Northeast and West tend to spend more on food per capita than the South and Midwest
* All regions spent more per capita on meat than greens in 1985
* All regions spent more per capita on greens than meat in 2018
* All regions but the South spent per capita more on alcoholic beverages than non-alcoholic beverages over 32 years
    * The south spent more on alcohol in 27 out of 32 years
* Between 2016 and 2018, the North had a 64% increase in per capita spending on fish and seafood

Visualization Screenshots:

![image](https://user-images.githubusercontent.com/6019805/86255258-e3ca8900-bb84-11ea-91fa-adbf2e54fcf1.png)
![image](https://user-images.githubusercontent.com/6019805/86255080-b382ea80-bb84-11ea-9fea-19a73eda32eb.png)
![image](https://user-images.githubusercontent.com/6019805/86255631-576c9600-bb85-11ea-9974-ff2f3402b2e7.png)
![image](https://user-images.githubusercontent.com/6019805/86255934-baf6c380-bb85-11ea-97c9-fa99d3fc13a4.png)
