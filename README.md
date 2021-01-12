# Modular, Bias-free Robo-Advisor/Portfolio Optimization Package

## Importing the libraries


```python
from customlibs import database as db
from customlibs import core as co
```

## Built-in ticker scraping function

The ticker scraping function in db scrapes a list of tickers from a given Wikipedia page.

A few Wikipedia page urls have been hardcoded into the db library for convenience


```python
etf_list = []
etf_list += db.get_etf_list(db.america_etfs)
etf_list += db.get_etf_list(db.japan_etfs)
etf_list += db.get_etf_list(db.hongkong_etfs)
etf_list += db.get_etf_list(db.europe_etfs)
etf_list = list(set(etf_list))
```

## Creating the Database object

The Database object found in the db library is used to download, manage, and save historical price data.


```python
database = db.Database()
```

## Adding tickers to the Database

Pass a list of tickers to the Database.add_tickers() function to add them to the Database. The list of tickers is stored as part of the Database object, and the missing historical asset price data is downloaded and appended.


```python
database.add_tickers(etf_list)
```
    

## Adding dates to the Database

Pass a single date as a string to the Database.add_date() function to expand the date range to include the new date. The Database will keep track of the date range, and missing historical asset price data is downloaded and appended.

Database objects must have at least one ticker added before dates can be added.

Database objects are initialised with start and end date 2000-01-01 23:59:59


```python
database.add_date("2020-01-01")
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SHE</th>
      <th>AADR</th>
      <th>AAXJ</th>
      <th>ACCU</th>
      <th>ACWI</th>
      <th>ACWX</th>
      <th>AGG</th>
      <th>ALD</th>
      <th>AMLP</th>
      <th>AND</th>
      <th>...</th>
      <th>XLE</th>
      <th>XLF</th>
      <th>XLI</th>
      <th>XLK</th>
      <th>XLP</th>
      <th>XLU</th>
      <th>XLV</th>
      <th>XLY</th>
      <th>XOP</th>
      <th>YPRO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-03</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>16.67</td>
      <td>9.44</td>
      <td>19.72</td>
      <td>43.14</td>
      <td>14.12</td>
      <td>13.15</td>
      <td>22.41</td>
      <td>23.36</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>16.36</td>
      <td>9.03</td>
      <td>19.18</td>
      <td>40.96</td>
      <td>13.72</td>
      <td>12.75</td>
      <td>21.90</td>
      <td>22.65</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>16.79</td>
      <td>8.96</td>
      <td>19.09</td>
      <td>40.35</td>
      <td>13.97</td>
      <td>13.08</td>
      <td>21.71</td>
      <td>22.38</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>17.44</td>
      <td>9.35</td>
      <td>19.35</td>
      <td>39.01</td>
      <td>14.23</td>
      <td>13.05</td>
      <td>21.78</td>
      <td>22.63</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>17.62</td>
      <td>9.51</td>
      <td>20.09</td>
      <td>39.69</td>
      <td>15.13</td>
      <td>13.17</td>
      <td>22.04</td>
      <td>23.70</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2019-12-24</th>
      <td>NaN</td>
      <td>54.00</td>
      <td>72.53</td>
      <td>NaN</td>
      <td>78.41</td>
      <td>48.35</td>
      <td>110.66</td>
      <td>NaN</td>
      <td>40.28</td>
      <td>NaN</td>
      <td>...</td>
      <td>58.10</td>
      <td>30.23</td>
      <td>80.79</td>
      <td>90.52</td>
      <td>62.07</td>
      <td>62.92</td>
      <td>101.39</td>
      <td>123.65</td>
      <td>93.19</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-26</th>
      <td>NaN</td>
      <td>54.30</td>
      <td>72.98</td>
      <td>NaN</td>
      <td>78.83</td>
      <td>48.56</td>
      <td>110.76</td>
      <td>NaN</td>
      <td>40.79</td>
      <td>NaN</td>
      <td>...</td>
      <td>58.08</td>
      <td>30.40</td>
      <td>80.98</td>
      <td>91.19</td>
      <td>62.13</td>
      <td>63.03</td>
      <td>101.32</td>
      <td>125.16</td>
      <td>93.54</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-27</th>
      <td>NaN</td>
      <td>54.51</td>
      <td>73.42</td>
      <td>NaN</td>
      <td>78.88</td>
      <td>48.65</td>
      <td>110.90</td>
      <td>NaN</td>
      <td>40.14</td>
      <td>NaN</td>
      <td>...</td>
      <td>57.84</td>
      <td>30.32</td>
      <td>80.91</td>
      <td>91.18</td>
      <td>62.40</td>
      <td>63.21</td>
      <td>101.35</td>
      <td>125.15</td>
      <td>91.97</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-30</th>
      <td>NaN</td>
      <td>54.10</td>
      <td>72.98</td>
      <td>NaN</td>
      <td>78.41</td>
      <td>48.35</td>
      <td>110.90</td>
      <td>NaN</td>
      <td>39.53</td>
      <td>NaN</td>
      <td>...</td>
      <td>57.65</td>
      <td>30.23</td>
      <td>80.53</td>
      <td>90.66</td>
      <td>62.08</td>
      <td>63.20</td>
      <td>100.74</td>
      <td>124.35</td>
      <td>91.85</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-31</th>
      <td>NaN</td>
      <td>53.89</td>
      <td>73.22</td>
      <td>NaN</td>
      <td>78.59</td>
      <td>48.55</td>
      <td>110.65</td>
      <td>NaN</td>
      <td>39.81</td>
      <td>NaN</td>
      <td>...</td>
      <td>57.98</td>
      <td>30.33</td>
      <td>80.49</td>
      <td>90.94</td>
      <td>62.14</td>
      <td>63.45</td>
      <td>100.94</td>
      <td>124.52</td>
      <td>93.19</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5031 rows × 425 columns</p>
</div>



## Saving Database objects to a local file

Database objects can be saved locally in one of two ways: .csv or pickle. For each function, the name of the local file to save to must be specified.


```python
database.save_to_csv("db.csv")
database.save_to_pickle("db.pickle")
```

## Reading Database objects a local file

Database objects can be read from local files using the functions corresponding to how they were saved.


```python
database = db.read_from_csv("db.csv")
database = db.read_from_pickle("db.pickle")
```

## Accessing Database historical asset prices

Historical asset prices stored in Database objects can be accessed simply by calling the .data attribute.


```python
database.data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SHE</th>
      <th>AADR</th>
      <th>AAXJ</th>
      <th>ACCU</th>
      <th>ACWI</th>
      <th>ACWX</th>
      <th>AGG</th>
      <th>ALD</th>
      <th>AMLP</th>
      <th>AND</th>
      <th>...</th>
      <th>XLE</th>
      <th>XLF</th>
      <th>XLI</th>
      <th>XLK</th>
      <th>XLP</th>
      <th>XLU</th>
      <th>XLV</th>
      <th>XLY</th>
      <th>XOP</th>
      <th>YPRO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-03</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>16.67</td>
      <td>9.44</td>
      <td>19.72</td>
      <td>43.14</td>
      <td>14.12</td>
      <td>13.15</td>
      <td>22.41</td>
      <td>23.36</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>16.36</td>
      <td>9.03</td>
      <td>19.18</td>
      <td>40.96</td>
      <td>13.72</td>
      <td>12.75</td>
      <td>21.90</td>
      <td>22.65</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>16.79</td>
      <td>8.96</td>
      <td>19.09</td>
      <td>40.35</td>
      <td>13.97</td>
      <td>13.08</td>
      <td>21.71</td>
      <td>22.38</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>17.44</td>
      <td>9.35</td>
      <td>19.35</td>
      <td>39.01</td>
      <td>14.23</td>
      <td>13.05</td>
      <td>21.78</td>
      <td>22.63</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>17.62</td>
      <td>9.51</td>
      <td>20.09</td>
      <td>39.69</td>
      <td>15.13</td>
      <td>13.17</td>
      <td>22.04</td>
      <td>23.70</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2019-12-24</th>
      <td>NaN</td>
      <td>54.00</td>
      <td>72.53</td>
      <td>NaN</td>
      <td>78.41</td>
      <td>48.35</td>
      <td>110.66</td>
      <td>NaN</td>
      <td>40.28</td>
      <td>NaN</td>
      <td>...</td>
      <td>58.10</td>
      <td>30.23</td>
      <td>80.79</td>
      <td>90.52</td>
      <td>62.07</td>
      <td>62.92</td>
      <td>101.39</td>
      <td>123.65</td>
      <td>93.19</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-26</th>
      <td>NaN</td>
      <td>54.30</td>
      <td>72.98</td>
      <td>NaN</td>
      <td>78.83</td>
      <td>48.56</td>
      <td>110.76</td>
      <td>NaN</td>
      <td>40.79</td>
      <td>NaN</td>
      <td>...</td>
      <td>58.08</td>
      <td>30.40</td>
      <td>80.98</td>
      <td>91.19</td>
      <td>62.13</td>
      <td>63.03</td>
      <td>101.32</td>
      <td>125.16</td>
      <td>93.54</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-27</th>
      <td>NaN</td>
      <td>54.51</td>
      <td>73.42</td>
      <td>NaN</td>
      <td>78.88</td>
      <td>48.65</td>
      <td>110.90</td>
      <td>NaN</td>
      <td>40.14</td>
      <td>NaN</td>
      <td>...</td>
      <td>57.84</td>
      <td>30.32</td>
      <td>80.91</td>
      <td>91.18</td>
      <td>62.40</td>
      <td>63.21</td>
      <td>101.35</td>
      <td>125.15</td>
      <td>91.97</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-30</th>
      <td>NaN</td>
      <td>54.10</td>
      <td>72.98</td>
      <td>NaN</td>
      <td>78.41</td>
      <td>48.35</td>
      <td>110.90</td>
      <td>NaN</td>
      <td>39.53</td>
      <td>NaN</td>
      <td>...</td>
      <td>57.65</td>
      <td>30.23</td>
      <td>80.53</td>
      <td>90.66</td>
      <td>62.08</td>
      <td>63.20</td>
      <td>100.74</td>
      <td>124.35</td>
      <td>91.85</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-31</th>
      <td>NaN</td>
      <td>53.89</td>
      <td>73.22</td>
      <td>NaN</td>
      <td>78.59</td>
      <td>48.55</td>
      <td>110.65</td>
      <td>NaN</td>
      <td>39.81</td>
      <td>NaN</td>
      <td>...</td>
      <td>57.98</td>
      <td>30.33</td>
      <td>80.49</td>
      <td>90.94</td>
      <td>62.14</td>
      <td>63.45</td>
      <td>100.94</td>
      <td>124.52</td>
      <td>93.19</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5031 rows × 425 columns</p>
</div>



## Filtering data based on data availability requirement

For portfolio construction, it may sometimes be desirable to consider only assets for which the data available exceeds a certain threshold.

This is done using the co.filter() function.

The function takes an unfiltered dataset and a constant, min_frac, as its inputs, and returns the filtered dataset. If the length of the unfiltered dataset is x, assets with fewer than x * min_frac historical price data points available are removed.

Alternatively, manually screening the dataset based on other requirements can be achieved using pandas functions.


```python
data = co.filter(database.data, 0.5)
```

## Calculating forward-looking returns

The returns for each asset are calculated using the co.get_return_df() function.

The function takes a filtered dataset and a constant, periods, as its inputs, and returns a dataframe with the forward-looking returns of each asset over the specified number of periods at each point in time.


```python
return_df = co.get_return_df(data, 252)
```

# Filtering anomalous behaviour

The downloading function provided above does not guarantee that the data downloaded is free from artifacts, which may occur if the source from which the data is downloaded contains errors. As such, it is important to filter the data for assets with anomalous behaviours, and to remove these assets before proceeding. This can be done using the co.anomaly_filter() function.

The function takes return_df and a constant, max_dev, as its inputs. The higher the value of max_dev, the greater the tolerance for deviation in asset behaviour. The function returns a copy of return_df with the anomalous assets removed.


```python
return_df = co.anomaly_filter(return_df, 3)
```

## Calculating summary data

Basic functions are provided to calculate the expected returns for each asset (mean_series), and the covariance matrix for all assets (cov_df)


```python
mean_series = co.get_mean_series(return_df)
cov_df = co.get_cov_df(return_df)
```

## Shortlisting assets

It may be unwieldly or otherwise inefficient to generate portfolios based on a very large set of assets. As such, a utility is provided to narrow down the number of asssets in consideration.

The co.get_shortlist() function takes cov_df and a constant, n_clusters, as its inputs. The assets are clustered using a K-means clustering algorithm into n_clusters number of clusters, based on their characteristics as reflected in the covariance matrix. A shortlist comprising the asset that best represents each sector is returned.

There are many other ways to construct an asset shortlist, however, most involve some extent of subjective decision-making, which introduces bias. Nonetheless, these can also be implemented with relative ease, by hardcoding the list of tickers.


```python
shortlist = co.get_shortlist(cov_df, 100)
```

## Generating optimized portfolios

The co.plot_optimize() function takes mean_series, cov_df, and a constant, n_points as inputs. n_points number of optimized portfolios are returned. The optimized portfolios are evenly spread out across a range of expected returns.

The co.eliminate() function eliminates portfolios which are dominated (there is at least one other portfolio with higher or equal returns and lower or equal risk.


```python
portfolio_df = co.plot_optimize(
    mean_series[shortlist], cov_df.loc[shortlist, shortlist], 50
)
portfolio_df = co.eliminate(portfolio_df)
```

## Other portfolio calculations

Functions are provided to calculate other key metrics for the list of generated portfolios.

co.get_at_risk_series() will return the value-at-risk in the worst x percentile situation for each portfolio.

co.get_loss_prob_series() will return the probability of lower than x (default 0) returns for each portfolio.

co.get_coefs_dict() and co.get_coefs_string() convert the portfolio objects to a more readable form.


```python
portfolio_df["at_risk"] = co.get_at_risk_series(portfolio_df, 0.01)
portfolio_df["loss_prob"] = co.get_loss_prob_series(portfolio_df, 0)
portfolio_df["coefs_dict"] = co.get_coefs_dict(
    portfolio_df, mean_series[shortlist].index, 10 ** -3
)
portfolio_df["coefs_string"] = co.get_coefs_string(portfolio_df)
```


```python
portfolio_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coefs</th>
      <th>var</th>
      <th>mean</th>
      <th>at_risk</th>
      <th>loss_prob</th>
      <th>coefs_dict</th>
      <th>coefs_string</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[0.0, 0.0, 1.4040129971970912e-15, 0.0, 0.0, 0...</td>
      <td>0.112419</td>
      <td>0.366134</td>
      <td>-0.413867</td>
      <td>0.137418</td>
      <td>{'UPRO': 0.9999999945050864}</td>
      <td>UPRO0.9999999945050864</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[2.4929667044350543e-16, 5.898180178738709e-16...</td>
      <td>0.070281</td>
      <td>0.350560</td>
      <td>-0.266167</td>
      <td>0.093027</td>
      <td>{'UPRO': 0.31129334762116595, 'QLD': 0.6887066...</td>
      <td>UPRO0.31129334762116595 QLD0.6887066523788344</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[1.0913796901555277e-16, 1.0478089401777796e-1...</td>
      <td>0.055542</td>
      <td>0.334987</td>
      <td>-0.213271</td>
      <td>0.077600</td>
      <td>{'QLD': 0.963821787680155, 'EDV': 0.0361782123...</td>
      <td>QLD0.963821787680155 EDV0.0361782123198447</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[2.3578639411195112e-17, 0.0, 3.25881615654170...</td>
      <td>0.046668</td>
      <td>0.319413</td>
      <td>-0.183143</td>
      <td>0.069627</td>
      <td>{'QLD': 0.8978035125018592, 'EDV': 0.102196487...</td>
      <td>QLD0.8978035125018592 EDV0.10219648749814213</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[0.0, 9.520457073564802e-17, 1.703904856966290...</td>
      <td>0.038949</td>
      <td>0.303840</td>
      <td>-0.155275</td>
      <td>0.061833</td>
      <td>{'QLD': 0.8317852375001451, 'EDV': 0.168214762...</td>
      <td>QLD0.8317852375001451 EDV0.16821476249985579</td>
    </tr>
    <tr>
      <th>5</th>
      <td>[0.0, 9.741337104283444e-19, 4.698332757853279...</td>
      <td>0.032377</td>
      <td>0.288266</td>
      <td>-0.130326</td>
      <td>0.054572</td>
      <td>{'UPRO': 0.016012850273290673, 'QLD': 0.748219...</td>
      <td>UPRO0.016012850273290673 QLD0.7482191486450445...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[2.5891340802016966e-17, 0.06924811709839378, ...</td>
      <td>0.026710</td>
      <td>0.272692</td>
      <td>-0.107506</td>
      <td>0.047604</td>
      <td>{'FDN': 0.0692481170983938, 'UPRO': 0.01924083...</td>
      <td>FDN0.0692481170983938 UPRO0.019240835744114105...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>[1.2779006080724355e-17, 0.14156375293853124, ...</td>
      <td>0.021661</td>
      <td>0.257119</td>
      <td>-0.085262</td>
      <td>0.040317</td>
      <td>{'FDN': 0.1415637529385313, 'UPRO': 0.01331993...</td>
      <td>FDN0.1415637529385313 UPRO0.013319937517352814...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[9.591504633176178e-18, 0.20071553060253264, 0...</td>
      <td>0.017208</td>
      <td>0.241545</td>
      <td>-0.063623</td>
      <td>0.032786</td>
      <td>{'FDN': 0.20071553060253272, 'UPRO': 0.0115794...</td>
      <td>FDN0.20071553060253272 UPRO0.01157944712422396...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>[8.588439746708141e-17, 0.24164978486891836, 0...</td>
      <td>0.013324</td>
      <td>0.225972</td>
      <td>-0.042555</td>
      <td>0.025134</td>
      <td>{'FDN': 0.24164978486891847, 'QLD': 0.39449550...</td>
      <td>FDN0.24164978486891847 QLD0.39449550883596485 ...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>[6.244597937701822e-17, 0.27637504764048915, 0...</td>
      <td>0.010009</td>
      <td>0.210398</td>
      <td>-0.022345</td>
      <td>0.017733</td>
      <td>{'FDN': 0.27637504764048926, 'QLD': 0.31058936...</td>
      <td>FDN0.27637504764048926 QLD0.31058936197953 IDU...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>[0.0, 0.2591190265173822, 0.0, 7.1099637580545...</td>
      <td>0.007324</td>
      <td>0.194825</td>
      <td>-0.004271</td>
      <td>0.011410</td>
      <td>{'FDN': 0.2591190265173823, 'IYC': 0.113210158...</td>
      <td>FDN0.2591190265173823 IYC0.11321015808257925 Q...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>[0.0, 0.30656840977913763, 0.0, 0.0, 0.0, 0.0,...</td>
      <td>0.005102</td>
      <td>0.179251</td>
      <td>0.013089</td>
      <td>0.006043</td>
      <td>{'FDN': 0.3065684097791379, 'IYC': 0.099525841...</td>
      <td>FDN0.3065684097791379 IYC0.0995258414368219 QL...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>[8.521829075736061e-18, 0.33922123657600284, 1...</td>
      <td>0.003458</td>
      <td>0.163678</td>
      <td>0.026874</td>
      <td>0.002690</td>
      <td>{'FDN': 0.3392212365760029, 'XLF': 0.016211173...</td>
      <td>FDN0.3392212365760029 XLF0.01621117302701375 I...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>[9.88250280220537e-18, 0.34818619576994597, 0....</td>
      <td>0.002276</td>
      <td>0.148104</td>
      <td>0.037127</td>
      <td>0.000953</td>
      <td>{'FDN': 0.34805145367553886, 'DUG': 0.02725354...</td>
      <td>FDN0.34805145367553886 DUG0.027253549840543033...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>[6.2939550420372415e-18, 0.30191549036013565, ...</td>
      <td>0.001614</td>
      <td>0.132530</td>
      <td>0.039075</td>
      <td>0.000485</td>
      <td>{'FDN': 0.3019154903601357, 'GDXJ': 0.00433158...</td>
      <td>FDN0.3019154903601357 GDXJ0.004331583419245826...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>[0.0, 0.27221656795167404, 0.0, 0.0, 0.0200205...</td>
      <td>0.001209</td>
      <td>0.116957</td>
      <td>0.036083</td>
      <td>0.000384</td>
      <td>{'FDN': 0.2722165679516741, 'IAU': 0.020020501...</td>
      <td>FDN0.2722165679516741 IAU0.02002050104158107 D...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>[1.2764786515122345e-18, 0.22839286704256223, ...</td>
      <td>0.000887</td>
      <td>0.101383</td>
      <td>0.032115</td>
      <td>0.000331</td>
      <td>{'FDN': 0.2283928670425623, 'IAU': 0.009403203...</td>
      <td>FDN0.2283928670425623 IAU0.009403203364063894 ...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>[0.0, 0.19501365954710687, 0.0, 3.674584841099...</td>
      <td>0.000617</td>
      <td>0.085810</td>
      <td>0.028033</td>
      <td>0.000275</td>
      <td>{'FDN': 0.19501365954710687, 'IAU': 0.01281554...</td>
      <td>FDN0.19501365954710687 IAU0.012815549776528363...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>[3.832315866557355e-18, 0.16276510508471506, 0...</td>
      <td>0.000425</td>
      <td>0.070236</td>
      <td>0.022257</td>
      <td>0.000330</td>
      <td>{'FDN': 0.1627651050847151, 'IAU': 0.017671042...</td>
      <td>FDN0.1627651050847151 IAU0.01767104241965885 D...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>[0.0, 0.13699549514716214, 3.2671600659589207e...</td>
      <td>0.000278</td>
      <td>0.054663</td>
      <td>0.015905</td>
      <td>0.000517</td>
      <td>{'FDN': 0.13699549514716222, 'IAU': 0.01946434...</td>
      <td>FDN0.13699549514716222 IAU0.019464342578931527...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>[0.0, 0.11379819150718547, 4.977465902727108e-...</td>
      <td>0.000176</td>
      <td>0.039089</td>
      <td>0.008235</td>
      <td>0.001603</td>
      <td>{'FDN': 0.11379374706815905, 'IAU': 0.02277106...</td>
      <td>FDN0.11379374706815905 IAU0.02277106003867687 ...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>[0.0, 0.09517727295533802, 1.1076399591510155e...</td>
      <td>0.000101</td>
      <td>0.023516</td>
      <td>0.000127</td>
      <td>0.009669</td>
      <td>{'FDN': 0.09511204956703839, 'IAU': 0.01700711...</td>
      <td>FDN0.09511204956703839 IAU0.01700711332841013 ...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>[4.0386530925085287e-19, 0.06982869403400421, ...</td>
      <td>0.000060</td>
      <td>0.007942</td>
      <td>-0.010010</td>
      <td>0.151697</td>
      <td>{'FDN': 0.06975478074215634, 'IAU': 0.01438296...</td>
      <td>FDN0.06975478074215634 IAU0.014382962759648187...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>[8.131515696105904e-20, 0.048707248959899314, ...</td>
      <td>0.000045</td>
      <td>-0.007632</td>
      <td>-0.023240</td>
      <td>0.872326</td>
      <td>{'FDN': 0.04864496329544185, 'IAU': 0.01094283...</td>
      <td>FDN0.04864496329544185 IAU0.01094283664635013 ...</td>
    </tr>
  </tbody>
</table>
</div>



## Alternative targeting

In some cases, portfolios aim not for a particular expected level of return, but for some other target metric, such as value-at-risk or loss probability.

This can be accomplished as well. However, the steps for targeting alternative metrics are a little less straightforward.

An initial range of portfolios must first be generated, as we have done above. Then, the target metric must be calculated for each of the generated portfolios, as we have done for value-at-risk and loss probability.

Then a list of targeted values for the new metric must be hardcoded. The co.metric_to_mean() function is then used to convert the list of targeted values for the new metric into target levels of expected returns. Portfolios are then generated to target each of these levels of expected returns.


```python
at_risk_target_list = [
    -0.01,
    -0.02,
    -0.03,
    -0.04,
    -0.05,
    -0.06,
    -0.07,
    -0.08,
    -0.09,
    -0.10,
]
mean_target_list = co.metric_to_mean(
    portfolio_df["mean"], portfolio_df["at_risk"], 3, at_risk_target_list
)
portfolio_df = co.target_optimize(
    mean_series[shortlist], cov_df.loc[shortlist, shortlist], mean_target_list
)
```


```python
portfolio_df["at_risk"] = co.get_at_risk_series(portfolio_df, 0.01)
portfolio_df["loss_prob"] = co.get_loss_prob_series(portfolio_df, 0)
portfolio_df["coefs_dict"] = co.get_coefs_dict(
    portfolio_df, mean_series[shortlist].index, 10 ** -3
)
portfolio_df["coefs_string"] = co.get_coefs_string(portfolio_df)
```


```python
portfolio_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coefs</th>
      <th>var</th>
      <th>mean</th>
      <th>at_risk</th>
      <th>loss_prob</th>
      <th>coefs_dict</th>
      <th>coefs_string</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[0.0, 0.2807896554913968, 3.1156951919821916e-...</td>
      <td>0.009846</td>
      <td>0.209557</td>
      <td>-0.021282</td>
      <td>0.017349</td>
      <td>{'FDN': 0.2807896554913969, 'QLD': 0.304958784...</td>
      <td>FDN0.2807896554913969 QLD0.3049587842132876 ID...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[3.774573630543031e-17, 0.25665205380576245, 7...</td>
      <td>0.011823</td>
      <td>0.219250</td>
      <td>-0.033701</td>
      <td>0.021879</td>
      <td>{'FDN': 0.25665205380576256, 'QLD': 0.35822861...</td>
      <td>FDN0.25665205380576256 QLD0.35822861487390245 ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[1.6376619705509373e-17, 0.2362138870426717, 0...</td>
      <td>0.013776</td>
      <td>0.227907</td>
      <td>-0.045134</td>
      <td>0.026081</td>
      <td>{'FDN': 0.23621388704267188, 'QLD': 0.40542919...</td>
      <td>FDN0.23621388704267188 QLD0.4054291978552987 I...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[1.368064088934103e-17, 0.2167053386907145, 1....</td>
      <td>0.015705</td>
      <td>0.235782</td>
      <td>-0.055753</td>
      <td>0.029955</td>
      <td>{'FDN': 0.21670533869071457, 'UPRO': 0.0032930...</td>
      <td>FDN0.21670533869071457 UPRO0.00329300475634142...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[2.6970799589997804e-17, 0.20080934496399924, ...</td>
      <td>0.017611</td>
      <td>0.243039</td>
      <td>-0.065679</td>
      <td>0.033519</td>
      <td>{'FDN': 0.20080934496399933, 'UPRO': 0.0068781...</td>
      <td>FDN0.20080934496399933 UPRO0.00687816903555018...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>[0.0, 0.18073406979787648, 0.0, 0.0, 0.0, 8.48...</td>
      <td>0.019493</td>
      <td>0.249792</td>
      <td>-0.075008</td>
      <td>0.036798</td>
      <td>{'FDN': 0.18073406979787665, 'UPRO': 0.0131924...</td>
      <td>FDN0.18073406979787665 UPRO0.01319248187870787...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[9.319366711508742e-17, 0.14734163602374525, 9...</td>
      <td>0.021359</td>
      <td>0.256126</td>
      <td>-0.083864</td>
      <td>0.039842</td>
      <td>{'FDN': 0.1473416360237453, 'UPRO': 0.01371432...</td>
      <td>FDN0.1473416360237453 UPRO0.01371432357159465 ...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>[0.0, 0.12331075549121606, 3.5809257281717055e...</td>
      <td>0.023209</td>
      <td>0.262102</td>
      <td>-0.092302</td>
      <td>0.042674</td>
      <td>{'FDN': 0.12327273858846184, 'UPRO': 0.0234104...</td>
      <td>FDN0.12327273858846184 UPRO0.02341042061618548...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[2.7616704563926586e-17, 0.09787056266181571, ...</td>
      <td>0.025050</td>
      <td>0.267770</td>
      <td>-0.100424</td>
      <td>0.045338</td>
      <td>{'FDN': 0.09787056266181574, 'UPRO': 0.0266234...</td>
      <td>FDN0.09787056266181574 UPRO0.02662341678212844...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>[0.0, 0.06690179172284137, 1.0112992017602561e...</td>
      <td>0.026874</td>
      <td>0.273168</td>
      <td>-0.108195</td>
      <td>0.047822</td>
      <td>{'FDN': 0.06690179172284141, 'UPRO': 0.0192410...</td>
      <td>FDN0.06690179172284141 UPRO0.01924107776922459...</td>
    </tr>
  </tbody>
</table>
</div>




```python
portfolio_df.to_csv("result.csv")
```

## Installation

Install by downloading and copying the customlibs folder to your project directory.

# Design Decisions

Robo-advisors available to retail investors combine proprietary software and financial expertise to deliver investment strategy and construct portfolios. They are necessarily opaque and prone to bias. There is value to a transparent, bias-free robo-advisor. We have thus designed and developed python packages with the core functionality for such a project. Our product is modular and allows for more complicated and tailored strategies to be rapidly designed and tested. This report serves to detail and explain the architecture of and design decisions behind our product.

The design decisions we have made are (1) with regards to the input the algorithm accepts, (2) with regards to the output of the algorithm, and (3) with regards to the processes of the algorithm.

The robo-advisor core functionality package provides for robo-advisors which take as inputs the historical adjusted closing price data of various exchange-traded assets. The guiding principles behind this decision were simplicity and accessibility. Conventional financial advisors require detailed, highly-technical, and current knowledge on the mechanics of a large range of asset classes. Different asset classes have different properties and behaviors, and accommodating such a range of assets would dramatically increase the size of the package. Exchange-traded funds provide exposure to a large number of asset classes and greatly reduce the complexity associated with monitoring the value and performance of these assets. Adjusted closing prices are a sufficiently-accurate proxy for the value of an exchange-traded fund. Instead of performing different, more complicated (and perhaps less accurate) calculations to ascertain the value of assets of various types, by monitoring the adjusted closing prices of exchange-traded funds, the size and complexity of our product are greatly reduced.

The package provides for robo-advisors which generate a list of optimized portfolios to match a list of investment targets. The investment objectives of retail investors span a wide range, from financial milestones to retirement and succession planning. These objectives can often be complicated by conditions such as irregular cash inflows and large one-off expenses. We have opted not to include models for such a wide range of investment objectives in our package, as doing so would contribute greatly to the bloat of our package, and we do not consider such functionality to be essential. Instead, users will be able to choose from some key metrics that can be used as targets or to implement other custom metrics. Metrics included in the package are (1) target level of expected returns, (2) target level of risk as measured by variance, and (3) target level of risk as measured by value-at-risk. The output of robo-advisors built around the package will be a list of optimized portfolios, each targetting a particular value of the chosen metric. For example, three optimised portfolios with 10%, 20%, and 30% value-at-risk. The ability to create custom metrics and to target values at any interval allows for a great degree of flexibility without dramatically inflating the size of our package.

The process catered for by our package consists of: (1) extracting summary data from the input, (2) selecting a representative shortlist of assets, and (3) generating the list of target portfolios.

Summary data describes the key characteristics of each asset in the input dataset. Our package applies modern portfolio theory to optimize portfolios. Modern portfolio theory in turn requires the expected return of each asset and the covariance matrix relating all assets to each other. We can arrive at this data in a two-step process. First, calculating the returns for each asset over a given period, for investments made at each point in time. Second, by calculating the mean of these returns and the covariance matrix relating the returns of all assets to each other. One parameter in this process is the length of the period over which to calculate returns. A shorter period would allow for a larger dataset of returns, and more granular data may produce more accurate covariance values. A longer period increases interpretability, for example, by taking one-year periods. This parameter can be set by the user depending on preference, and will likely have little effect on the resulting portfolios.

A shortlist of assets is composed, each representing one cluster of similarly-behaved assets from the initial pool. The greater the number of assets in consideration, the more computationally intensive it becomes to generate optimal portfolios. The more assets in a portfolio, the more costly it is to manage and re-balance. As such, it does not make sense to optimize portfolios comprising the entire universe of exchange-traded funds. It becomes necessary to narrow down the list to a smaller number of exchange-traded funds which each represent some segment of the asset universe. This is done by applying a clustering algorithm to classify each asset based on its covariance with all other assets. Assets with similar relationships are grouped. The shortlist is assembled by selecting the asset which most closely matches the mean values for the cluster it belongs to. This process was chosen as it is entirely bias-free, and perfectly repeatable, given a target number of clusters. Robo-advisors in practice often shortlist several asset classes/types and select from within each category the exchange-traded fund with the highest volume, greatest liquidity, or some other factor. The identification of asset classes/types and the selection of criteria introduce bias and reduce transparency. Nonetheless, it is relatively hassle-free to implement a manual shortlist instead.

The final step in the process is to generate the portfolios which match a range of values for a target metric. There are two parts to this. First, the range of optimal portfolios is generated. Optimal portfolios are generated with target levels of expected returns, spanning the whole range of possible levels of return (from that of the lowest-returning asset to that of the highest-returning asset). Optimizing each portfolio is done using the scipy module’s optimize library. A set of weights for each asset are adjusted such that the total portfolio return variance is a minimum, given that the sum of weights is one and the total portfolio return mean is equal to the target value. Mean, variance, and other metrics are calculated for each of these portfolios. Second, a polynomial curve is fitted to approximate the relationship between the expected level of return and the chosen metric (for example, value-at-risk), with mean as the independent variable and the chosen metric as the dependent variable. Then, the mean values corresponding to each of a set of target values for the chosen metric are computed. Optimized portfolios are then generated with expected returns equal to these mean values. The resulting portfolios are the output of the robo-advisor.

The package constructed leaves room for further tuning and development, and the implementation of more complicated strategies. We elaborate on a few possibilities below.

Further functionality may attempt to move away from the naive assumption about future performance and behavior. One way to do this is to more heavily weight periods which better match a subjective expectation of future asset behavior in the computation of summary statistics. Weighted means of each asset’s return series and a weighted covariance matrix can be generated with relative ease. Weights can be used to (1) emphasize recent data, (2) emphasize data that matches a subjective expectation of future asset performance and behavior, or (3) emphasize either more bullish or more bearish periods. These options replace the assumption that future performance and behavior resemble past performance and behavior with more nuanced approaches. Greater control can be gained by manual tuning of summary statistics. One noteworthy use case would be to adjust the expected returns on various assets by different amounts based on the relevant tax policy for each asset class or geography.

Curated shortlists as opposed to automated shortlisting can also be implemented with relative ease. This leaves room for robo-advisors which prefer to stick with a more human-in-the-loop design. Manual selection of asset components may also be required for regulatory or other risk-management reasons.
