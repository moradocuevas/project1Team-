import pandas as pd

def countries():

    #Load each of the files of world population and gdp per capita of each country
    population_countries = pd.read_csv("WORLD_POPULATION.csv")
    percapita_gdp = pd.read_csv("GDP_PERCAPITA.csv")

    population_countries.head()




    #assign desired ranges of population in world population file

    selected_countries = population_countries[population_countries["2017"] > 60000000]
    selected_countries = selected_countries[population_countries["2017"] < 130000000]




    # convert countries within range to a list
    countries_range = (selected_countries["Country Name"].tolist())




    #clean up the list by deleting non-country lines
    countries_range.pop(0)




    percapita_gdp.head()



    #obtain maximum gdp per capita
    gdp_pc_2017_max = percapita_gdp["2017"].max()
    gdp_pc_2017_max




    #obtain minimum gdp per capita

    gdp_pc_2017_min = percapita_gdp["2017"].min()
    gdp_pc_2017_min




    #organize Gdp per capita 2017 in descending order
    percapita_gdp = percapita_gdp.sort_values("2017", ascending=False)




    percapita_gdp["Group"] ="A"



    #count the number of enlisted countries in gdp file
    percapita_gdp.shape[0]




    #assign ranges for the three groups of countries according to gpd per capita from the list of countries
    percapita_gdp.iloc[0:50,percapita_gdp.columns.get_loc("Group")] = "High Development"
    percapita_gdp.iloc[51:150,percapita_gdp.columns.get_loc("Group")] = "Medium Development"
    percapita_gdp.iloc[151:264,percapita_gdp.columns.get_loc("Group")] = "Low Development"




    percapita_gdp.columns.get_loc("Group")




    #create a dataframe containing the selected countries
    countries_range = pd.DataFrame(countries_range)
    countries_range.columns = ["Country Name"]




    #merge the list of countries selected by population with the dataframe to obtain the intersection
    selected_countries = pd.merge(countries_range, percapita_gdp, on="Country Name")




    selected_countries.head()



    #select the relevant columns and sort the dataframe in descending order from higher to lower GDPPC

    selected_countries = selected_countries.loc[ : ,["Country Name","2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2005", "2000", "1995", "1990", "Group"]]
    selected_countries = selected_countries.sort_values("2017", ascending=False)
    selected_countries



    #rename column 2017 to GDPPC 2017
    selected_countries = selected_countries.rename(columns = {'2017':'GDPPC 2017'})



    #Select just 3 countries of each gruop. Drop countries that have the least relevance according to industry presence 
    selected_countries = selected_countries.drop([1,7,6,3,0])



    #reset index
    selected_countries = selected_countries.reset_index(drop=True)


    #export csv file
    selected_countries.to_csv('COUNTRIES.csv')


    return(selected_countries)

