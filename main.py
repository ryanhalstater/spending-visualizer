import requests
import json
import prettytable
import pandas as pd
import numpy as np
import math

#note this program was designed to save csv files at multiple steps for convenient editing and viewing
#Before running: go to BLS website and manually search for series names that are interesting, and add to hasSeriesIDs.csv

def main():
    #read series ids and get data from 32 years on each series
    get_data()
    prepare_inflation_csv()
    convert_to_present_value(2018)
    #format data so it is friendly for tableau
    reshape_data()

#make the index years rather than having many rows
def reshape_data():
    df = pd.read_csv('unshaped_results_in_pv.csv')
    new_df = pd.DataFrame(columns=['Year','Region','State for Tableau']+list(df['Name of Series'].unique()))
    for yr in df['Year'].unique():
        for rg in df['Region'].unique()[1:]: #to avoid when the region is none
            new_row = [yr,rg, region_to_state(rg)] + list(df.loc[(df.Region == rg) & (df.Year == yr)]['Dollars Spent'])
            new_df.loc[len(new_df)] = new_row
        #for case where no region
        new_row = [yr, 'All', np.nan] + list(df.loc[(df.Region.isna()) & (df.Year == yr)]['Dollars Spent'])
        new_df.loc[len(new_df)] = new_row
    new_df = new_df.set_index(['Year','Region'])
    new_df.to_csv("tableau_friendly_results.csv")

def adjust_for_inflation():
    fred = pd.read_csv('CPI_for_food_from_FRED')

def prepare_inflation_csv():
    df = pd.read_csv('CPI_for_food_from_FRED.csv')
    print(df.head())
    df['helper'] = df['DATE'].apply(lambda x: helper(x))

    res = df.loc[df['helper'] == 1]
    print(res.head())
    res['Year'] = res.apply(lambda x: x['DATE'][:4], axis=1)

    res = res.drop(['helper', 'DATE'], 1)
    res = res.set_index(['Year'])
    res.to_csv('CPI_food_cleaned.csv')
    print(res.head())

def helper(x):
    if str(x)[5:7] == '01':
        return 1
    return 0

def convert_to_present_value(ref_year):
    df = pd.read_csv('unshaped_results.csv')
    inflation_df = pd.read_csv('CPI_food_cleaned.csv')
    new_index = float(inflation_df.loc[inflation_df['Year'] == ref_year, 'CPIFABSL'])

    #map pandas of inflation to list file so can use
    #put the adding numbers part to the cleaning_csv if can later

    t1 = list(inflation_df['Year'])
    t2 = list(inflation_df['CPIFABSL'])
    inflation_dict = dict(zip(t1, t2))

    def convert(row):
        # return int(row['Year'])
        x = row['Year']
        # return (x == 1913)
        old_index = inflation_dict[x]
        # return old_index
        return (row['Dollars Spent']) * new_index / old_index

    dsa = df.apply(lambda x: convert(x), axis=1)
    df['Dollars Spent'] = dsa
    #clean out old index column
    df = df.drop(['Unnamed: 0'],axis=1)
    # df = df.set_index(['Year','Lower Bound'])
    print(df.head())
    df.to_csv('unshaped_results_in_pv.csv')

def get_data():
    #loop through csv doc from manual search and get all unique series ids
    series_ids = []
    data_source = pd.read_csv('hasSeriesIDs.csv')
    for name in data_source['Series ID']:
        if name not in series_ids:
            series_ids.append(name)

    #see if the series_id translators have been made, and if not, make them
    try:
        dfdc = pd.read_csv("dfdc.csv")
        dfic = pd.read_csv("fdic.csv")
    except:
        dfdc = text_to_pandas("demographics_codes_and_characteristic_codes_to_description.txt")
        dfic = text_to_pandas("item_code_to_description.txt")
        dfdc.to_csv("dfdc.csv")
        dfic.to_csv("dfic.csv")

    # note can only get 20 years at a time, and data starts at year 1984 for this dataset
    starting_years = [1984, 1984 + 20]
    #note can only grab 50 series at one time due to API restrictions
    starting_series_indexes = range(0,len(series_ids),50)

    # prepare to access and access BLS data from API
    usable_df = pd.DataFrame(columns=['Name of Series','Is Everyone','Region','State for Tableau','Year','Dollars Spent'])
    headers = {'Content-type': 'application/json'}
    for starting_index in starting_series_indexes: #ensures that grabs as much as possible in one go
        ending_index = starting_index + 50
        if ending_index > len(series_ids):
            ending_index = len(series_ids)

        for start_year in starting_years:
            data = json.dumps({"seriesid": series_ids[starting_index:ending_index], "startyear": str(start_year), "endyear": str(start_year+19),
                               "registrationkey": "9cab0895bf8746ff9aa39d2e0c93da3a"})
            p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
            json_data = json.loads(p.text)
            for series in json_data['Results']['series']:
                series_id = series['seriesID']
                tid_values = translate_id(series_id,dfic,dfdc) #translate series ID to values we want
                for item in series['data']:
                    year = item['year']
                    value = item['value']
                   # recall tid_values is in form [item_desc, is_everyone, region, state]
                    usable_df.loc[len(usable_df)] = [tid_values[0],tid_values[1],tid_values[2],tid_values[3],year,value]
    usable_df.to_csv("unshaped_results.csv")
    return


#for converting seriesID translation text documents into usable dataframes/csv files
def text_to_pandas(file_path):
    with open(file_path) as file:
        all_rows = file.readlines()
        col_names = all_rows[0].split()
        for name in col_names:
            name = name[:-1]
    data_for_df = []
    for row in all_rows[1:]:
        data_for_df.append(row.rstrip().split('\t'))
    df = pd.DataFrame(data=data_for_df,columns=col_names)
    return df

def region_to_state(region):
    region_to_state = {'northeast': 'New York', 'midwest': 'Iowa', 'south': 'Florida', 'west': 'California'}
    return region_to_state[region]

#given dataframes of how to translate series IDs, interpret and return array of information contained
def translate_id(id,dfic,dfdc):
    # how to break down id noted at https://www.bls.gov/help/hlpforma.htm#CX
    item_code = id[3:-7]
    demographics_code = id[-7:-3]
    characteristics_code = id[-3:-1]

    item_desc = dfic.loc[dfic.item_code == str(item_code)]['item_text'].values[0]
    char_desc = dfdc.loc[(dfdc.demographics_code == str(demographics_code)) & (
            dfdc.characteristics_code == str(characteristics_code))]['characteristics_text'].values[0]

    # now determine what fields we can fill in, if any
    is_everyone = 0
    region = np.nan
    state = np.nan
    if (char_desc[:6] == 'Region'):
        # break it apart to get what region, and then map to a state so Tableau can show geographic data visually
        region = char_desc.split()[-1]
        state = region_to_state(region)
    else:
        is_everyone = 1
    return [item_desc,is_everyone,region,state]

main()