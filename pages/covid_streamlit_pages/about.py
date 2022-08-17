import streamlit as st


def write(df):
    url = "https://towardsdatascience.com/interactive-dashboard-in-streamlit-to-analyse-owid-covid-19-data-180b1c3372e4"
    st.header('About Me')
    st.write('My name is Raguram ,'
             ' I replicated this streamlit app from the git codebase of Sam Ho ,'
             'since the link shared by him in his [blog](%s) is not working anymore,'
             ' I created this app to showcase my datascience and code abilities and also as originally stated by Sam '
             'for '
             'EDA of the available Covid data ' % url)

    st.header('Overview')
    st.markdown('This Streamlit app uses a range of Covid-19 data sources that have been kindly curated by "Our World in Data" (OWID). \
    My intention with this app was was to design a user friendly, interface for people to do their own exploratory analysis using\
    the Covid-19 OWID data.')

    st.subheader('Data')

    st.markdown('To keep the app *light*, I did not include every single feature available in the data set but did \
    include the following:')

    import plotly.graph_objects as go
    # col_1 = df[df.columns[0]].values
    # col_2 = df[df.columns[1]].values
    # col_3 = df[df.columns[2]].values

    st.write("*Note I can't be held accountable for the quality of the data in this dataset*")

    st.write('For a detailed breakdown of the data sources used by OWID and other features not included here, \
    they have some great documentation on their repo which can be found here: https://github.com/owid/covid-19-data/blob/master/public/data/README.md')
    st.dataframe(df)
    # fig_table = go.Figure(data=[go.Table(header=dict(values=[df.columns[0], df.columns[1], \
    #                                                          df.columns[2]]),
    #                                      cells=dict(values=[col_1, col_2, col_3], align='left',fill_color='white'))])
    # st.plotly_chart(fig_table, height=800, width=1200,use_container_width=True)

    # fill_color = [[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor] * 5],

    st.subheader('Libraries & Tools')
    st.write("This app was built in Streamlit and all visualisations were generated using Plotly Express or Plotly Graph \
    Objects. The code for the app is freely available on the app's repo on Github.")

    st.header('About The Original Creator')
    st.write('The creator of this app is Sam Ho ,a Data scientist at Shutterstock AI')

    return
