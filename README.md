# spending-visualizer
Tableau visualizations of consumer spending data over 34 years (from BLS API, adjusted to [2018 dollars](https://fred.stlouisfed.org/series/CPIFABSL)) to discover interesting trends  
Python Libraries used: Pandas, Numpy  
  
Data: in tableau_friendly_results.csv (scraped and reformatted by running main.py) and displayed in visualization.twbx  
Note that can specify the BLS series to analyze by adding results from [search](https://beta.bls.gov/dataQuery/find?fq=survey:[cx]&s=popularity:D) to hasSeriesID.csv  
  
Data was divided into four regions: Midwest, Northeast, South, West  
   
Interesting results:
* The Northeast and West tend to spend more on food per capita than the South and Midwest
* All regions spent more per capita on meat than greens in 1985
   * 2005 was the first recorded year where any region spent more on greens than meat
   * All regions spent more per capita on greens than meat in 2016
* In the USA, the amount of money spent on Alcoholic Beverages consistenly exceeded the amount spent on non-alcoholic beverages
    * All regions except the South spent per capita more on alcoholic beverages than non-alcoholic beverages over 32 years
        * The South spent more on alcoholic beverages than non-alcoholic beverages in 26 out of 32 years
* Certian regions tend to have more spending on food groups than others (may be indicative of culture or resources available)
  * The Northeast and West tend to spend more on seafood than other regions
  * The Northeast tend to spend more on sugar and other sweets than other regions
  * The Northeast tend to spend more on poultry than other regions, especially between 1983 and 2004
  * The South maintained high spending on pork products, more so than most other regions
  * There was no region that maintained consistently higher spending on fats and oils than other regions
  <br/>
Visualization Screenshots (all Y axis units are annual dollars spend):


![image](https://user-images.githubusercontent.com/6019805/92264407-35a4cd80-eeac-11ea-852d-d5e9ba4597da.png)
![image](https://user-images.githubusercontent.com/6019805/92264403-3178b000-eeac-11ea-98f8-99f15abbafa9.png)
![image](https://user-images.githubusercontent.com/6019805/92264423-39d0eb00-eeac-11ea-914e-d4499c371700.png)
![image](https://user-images.githubusercontent.com/6019805/92264431-3b021800-eeac-11ea-9883-9fd403214aba.png)
![image](https://user-images.githubusercontent.com/6019805/92264443-3dfd0880-eeac-11ea-8106-45ad71eb22b9.png)
![image](https://user-images.githubusercontent.com/6019805/92264454-405f6280-eeac-11ea-8b6c-475093f3e5f9.png)
![image](https://user-images.githubusercontent.com/6019805/92264475-46edda00-eeac-11ea-9dd0-c85bd4ad4f59.png)
![image](https://user-images.githubusercontent.com/6019805/92264482-49503400-eeac-11ea-8366-04eea07ae3f3.png)
![image](https://user-images.githubusercontent.com/6019805/92264486-4b19f780-eeac-11ea-959a-4fe985191243.png)
