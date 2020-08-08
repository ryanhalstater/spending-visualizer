# spending-visualizer
Tableau visualizations of consumer spending data over 34 years (from BLS API) to discover interesting trends  
Python Libraries used: Pandas, Numpy  
  
Data: in tableau_friendly_results.csv (scraped and reformatted by running main.py) and displayed in visualization.twbx  
Note that can specify the BLS series to analyze by adding results from [search](https://beta.bls.gov/dataQuery/find?fq=survey:[cx]&s=popularity:D) to hasSeriesID.csv  
  
Data was divided into four regions: Midwest, Northeast, South, West  
   
Interesting results:
* The Northeast and West tend to spend more on food per capita than the South and Midwest
* All regions spent more per capita on meat than greens in 1985
* All regions spent more per capita on greens than meat in 2018
* All regions but the South spent per capita more on alcoholic beverages than non-alcoholic beverages over 32 years
    * The South spent more on alcohol in 27 out of 32 years
* Between 2016 and 2018, the North had a 64% increase in per capita spending on fish and seafood

Visualization Screenshots:

![image](https://user-images.githubusercontent.com/6019805/86258217-905a3a00-bb88-11ea-8b10-2865c2b0848a.png)
![image](https://user-images.githubusercontent.com/6019805/86258270-a23bdd00-bb88-11ea-8e4a-2c37ed18afb0.png)
![image](https://user-images.githubusercontent.com/6019805/86255631-576c9600-bb85-11ea-9974-ff2f3402b2e7.png)
![image](https://user-images.githubusercontent.com/6019805/89701921-9969c400-d909-11ea-86bb-1c333b457337.png)
![image](https://user-images.githubusercontent.com/6019805/86259597-3490b080-bb8a-11ea-9ac7-2123bce3ed97.png)
