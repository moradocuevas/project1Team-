import requests
import json
import pandas as pd
import numpy as np

def Api_requests():

    country = ["jp","gb","fr","tr","mx","th","ph","eg","vn"]
    id_indicator = ['EG.ELC.ACCS.ZS','EG.ELC.LOSS.ZS','EG.ELC.HYRO.ZS','EG.ELC.RNWX.ZS','EG.ELC.COAL.ZS','EG.ELC.NUCL.ZS',
                'EG.ELC.PETR.ZS']
    mx_bcountry = []
    mx_jason = []
    for y in country:
        for x in id_indicator:
            url = 'http://api.worldbank.org/v2/country/'+y+'/indicators/'+x+'?format=json'
            mx_jason.append(requests.get(url).json())
        mx_bcountry.append(mx_jason)
        mx_jason = []
    
    n_datos = np.arange(0,len(mx_bcountry[0][0][1])) #n de iteraciones para los datos
    n_id = np.arange(0,len(id_indicator)) #n de iteraciones para indicadores
    n_country = np.arange(0,len(country))

    date = []
    for x in n_datos:
        date.append(mx_bcountry[1][0][1][x]['date'])
    dates = {"Date":date}

    data = {'Access to electricity (% of population)':[],'Electric power transmission and distribution losses (% of output)':[],
        'Electricity production from hydroelectric sources (% of total)':[],
        'Electricity production from renewable sources, excluding hydroelectric (% of total)':[],
        'Electricity production from coal sources (% of total)':[],'Electricity production from nuclear sources (% of total)':[],
        'Electricity production from oil sources (% of total)':[]}
    data_2 = {'Access to electricity (% of population)':[],'Electric power transmission and distribution losses (% of output)':[],
        'Electricity production from hydroelectric sources (% of total)':[],
        'Electricity production from renewable sources, excluding hydroelectric (% of total)':[],
        'Electricity production from coal sources (% of total)':[],'Electricity production from nuclear sources (% of total)':[],
        'Electricity production from oil sources (% of total)':[]}
    data_3 = {'Access to electricity (% of population)':[],'Electric power transmission and distribution losses (% of output)':[],
        'Electricity production from hydroelectric sources (% of total)':[],
        'Electricity production from renewable sources, excluding hydroelectric (% of total)':[],
        'Electricity production from coal sources (% of total)':[],'Electricity production from nuclear sources (% of total)':[],
        'Electricity production from oil sources (% of total)':[]}
    data_4 = {'Access to electricity (% of population)':[],'Electric power transmission and distribution losses (% of output)':[],
        'Electricity production from hydroelectric sources (% of total)':[],
        'Electricity production from renewable sources, excluding hydroelectric (% of total)':[],
        'Electricity production from coal sources (% of total)':[],'Electricity production from nuclear sources (% of total)':[],
        'Electricity production from oil sources (% of total)':[]}
    data_5 = {'Access to electricity (% of population)':[],'Electric power transmission and distribution losses (% of output)':[],
        'Electricity production from hydroelectric sources (% of total)':[],
        'Electricity production from renewable sources, excluding hydroelectric (% of total)':[],
        'Electricity production from coal sources (% of total)':[],'Electricity production from nuclear sources (% of total)':[],
        'Electricity production from oil sources (% of total)':[]}
    data_6 = {'Access to electricity (% of population)':[],'Electric power transmission and distribution losses (% of output)':[],
        'Electricity production from hydroelectric sources (% of total)':[],
        'Electricity production from renewable sources, excluding hydroelectric (% of total)':[],
        'Electricity production from coal sources (% of total)':[],'Electricity production from nuclear sources (% of total)':[],
        'Electricity production from oil sources (% of total)':[]}
    data_7 = {'Access to electricity (% of population)':[],'Electric power transmission and distribution losses (% of output)':[],
        'Electricity production from hydroelectric sources (% of total)':[],
        'Electricity production from renewable sources, excluding hydroelectric (% of total)':[],
        'Electricity production from coal sources (% of total)':[],'Electricity production from nuclear sources (% of total)':[],
        'Electricity production from oil sources (% of total)':[]}
    data_8 = {'Access to electricity (% of population)':[],'Electric power transmission and distribution losses (% of output)':[],
        'Electricity production from hydroelectric sources (% of total)':[],
        'Electricity production from renewable sources, excluding hydroelectric (% of total)':[],
        'Electricity production from coal sources (% of total)':[],'Electricity production from nuclear sources (% of total)':[],
        'Electricity production from oil sources (% of total)':[]}
    data_9 = {'Access to electricity (% of population)':[],'Electric power transmission and distribution losses (% of output)':[],
        'Electricity production from hydroelectric sources (% of total)':[],
        'Electricity production from renewable sources, excluding hydroelectric (% of total)':[],
        'Electricity production from coal sources (% of total)':[],'Electricity production from nuclear sources (% of total)':[],
        'Electricity production from oil sources (% of total)':[]}
    columns = [*data]
    datass = [data,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9]

    for z,n in zip(n_country,datass):
        for x in n_datos:
            for i,j in zip(columns,n_id):
                n[i].append(mx_bcountry[z][j][1][x]['value'])
            
    data.update(dates)
    data_2.update(dates)
    data_3.update(dates)
    data_4.update(dates)
    data_5.update(dates)
    data_6.update(dates)
    data_7.update(dates)
    data_8.update(dates)
    data_9.update(dates)

    listaFinal = {
        "jp": pd.DataFrame(data),
        "gb":pd.DataFrame(data_2),
        "fr":pd.DataFrame(data_3),
        "tr":pd.DataFrame(data_4),
        "mx":pd.DataFrame(data_5),
        "th":pd.DataFrame(data_6),
        "ph":pd.DataFrame(data_7),
        "eg":pd.DataFrame(data_8),
        "vn":pd.DataFrame(data_9)
    }

    return(listaFinal)






