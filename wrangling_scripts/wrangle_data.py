import pandas as pd
import plotly.graph_objs as go


#Clean the dataset

df_br = pd.read_csv('data/birth_rate.csv', skiprows=4)
df_le = pd.read_csv('data/life_expectancy.csv', skiprows=4)
df_le = df_le.drop(['Country Code','Indicator Name','Indicator Code','2018','2019','Unnamed: 64'],axis=1)
df_meta = pd.read_csv('data/Metadata_Country_API_SP.DYN.LE00.IN_DS2_en_csv_v2_820880.csv')
df = df_br.merge(df_meta, on=['Country Code'], how='left')
df = df.drop(['Country Code','Indicator Name','Indicator Code','2018','2019','Unnamed: 64','SpecialNotes','TableName','Unnamed: 5'],axis=1)

countrylist = ['United States', 'China', 'Japan', 'Korea','Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Nigeria']
regionlist = ['East Asia & Pacific','Europe & Central Asia','Latin America & Caribbean','Middle East & North Africa','North America','South Asia','Sub-Saharan Africa']
incomelist= ['High income','Upper middle income','Lower middle income','Low income']







def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """


    # first chart plots birth rates from 1960 to 2017 in top selected countries
    # as a line chart

    graph_one = []

    dfc = df[df['Country Name'].isin(countrylist)]
    dfc = dfc.melt(id_vars='Country Name', value_vars = dfc.columns[1:-2])
    dfc.columns = ['country','year', 'birth_rate']
    dfc['year'] = dfc['year'].astype('datetime64[ns]').dt.year

    for country in countrylist:
        x_val = dfc[dfc['country'] == country].year.tolist()
        y_val =  dfc[dfc['country'] == country].birth_rate.tolist()
        graph_one.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country)
        )

    layout_one = dict(title = 'Birth Rates from Year 1960 to 2017',
                xaxis = dict(title = 'Year', dtick=5),
                yaxis = dict(title = 'Birth Rate (%)'),
                )



# second chart plots ararble land for 2015 as a bar chart
    graph_two = []


    dfr = df.groupby('Region').mean().reset_index()
    dfr = dfr.melt(id_vars='Region', value_vars = dfr.columns[1:])
    dfr.columns = ['region','year', 'birth_rate']
    dfr['year'] = dfr['year'].astype('datetime64[ns]').dt.year

    for region in regionlist:
        x_val = dfr[dfr['region'] == region].year.tolist()
        y_val =  dfr[dfr['region'] == region].birth_rate.tolist()
        graph_two.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = region)
        )

    layout_two = dict(title = 'Birth Rates by Region',
                xaxis = dict(title = 'Year', dtick=5),
                yaxis = dict(title = 'Birth Rate (%)'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []


    dfi = df.groupby('IncomeGroup').mean().reset_index()
    dfi = dfi.melt(id_vars='IncomeGroup', value_vars = dfi.columns[1:])
    dfi.columns = ['income','year', 'birth_rate']
    dfi['year'] = dfi['year'].astype('datetime64[ns]').dt.year

    for income in incomelist:
        x_val = dfi[dfi['income'] == income].year.tolist()
        y_val =  dfi[dfi['income'] == income].birth_rate.tolist()
        graph_three.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = income)
        )

    layout_three = dict(title = 'Birth Rates by Income Group',
                xaxis = dict(title = 'Year', dtick=5),
                yaxis = dict(title = 'Birth Rate (%)'),
                )

# fourth chart shows rural population vs arable land
    graph_four = []

    dfl = df_le[df_le['Country Name'].isin(countrylist)]
    dfl = dfl.melt(id_vars='Country Name', value_vars = dfl.columns[1:])
    dfl.columns = ['country','year', 'life_expectancy']
    dfl['year'] = dfl['year'].astype('datetime64[ns]').dt.year

    for country in countrylist:
        x_val = dfl[dfl['country'] == country].year.tolist()
        y_val =  dfl[dfl['country'] == country].life_expectancy.tolist()
        graph_four.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country)
        )

    layout_four = dict(title = 'Life Expectancy from Year 1960 to 2017',
                xaxis = dict(title = 'Year', dtick=5),
                yaxis = dict(title = 'Life Expectancy (years)'),
                )


    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
