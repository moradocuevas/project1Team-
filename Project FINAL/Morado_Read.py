import pandas as pd
import os

def csv():

    #Creates a path to the document
    pollution_path="World pollution KPI.csv"

    #Transforms the info into a dataframe
    pollution_df=pd.read_csv(pollution_path, encoding="latin-1")
    pollution_df.head()
    pollution_df.count()

    #Replaces the NaN with 0. In case of being needed, we can delete the null data easily. 
    pollution_df=pollution_df.fillna(0)

    pollution_df

    #DataFrame with just our assigned standards.
    developed= pollution_df[pollution_df['Country Name'].isin([ 'France','Japan', 'United Kingdom'])]
    developed


    developing= pollution_df[pollution_df['Country Name'].isin([ 'Turkey','Mexico', 'Thailand'])]
    developing


    underdeveloped=pollution_df[pollution_df['Country Name'].isin(['Philippines','Egypt, Arab Rep.', "Vietnam"])]
    underdeveloped

    developed_1 = developed.set_index('Country Name').transpose().reset_index().drop([0,1,2])
    developed_1 = developed_1.loc[developed_1['France'] != 0,:]
    developed_1 = developed_1.rename(
   columns={"index":"Date"}).set_index('Date')
    developed_1
    developing_1 = developing.set_index('Country Name').transpose().reset_index().drop([0,1,2])
    developing_1 = developing_1.loc[developing_1['Mexico'] != 0,:]
    developing_1 = developing_1.rename(
   columns={"index":"Date"}).set_index('Date')
    developing_1
    underdeveloped_1 = underdeveloped.set_index('Country Name').transpose().reset_index().drop([0,1,2])
    underdeveloped_1 = underdeveloped_1.loc[underdeveloped_1['Philippines'] != 0,:]
    underdeveloped_1 = underdeveloped_1.rename(
   columns={"index":"Date"}).set_index('Date')
    underdeveloped_1

    csv_lista = {
        'Developed': developed_1,
        'Developing': developing_1,
        'Underdeveloped': underdeveloped_1
    }

    return(csv_lista)

