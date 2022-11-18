import streamlit as st
import pandas as pd
import plotly.express as px

st.write("# Avocado Prices dashboard")
# st.title("if write on Avocado Prices dashboard in use .title, same as '# Avocado Prices dashboard'sentence")
st.markdown('''
This is a dashboard showing the *average prices* of different types of :avocado:  
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')
# st.header('Summary statistics')
# st.header('Line chart by geographies')

# 표
st.header('Summary statistics')
avocado = pd.read_csv('avocado-updated-2020.csv')
avocado_stats = avocado.groupby('type')['average_price'].mean()
st.dataframe(avocado_stats)

# 그래프
st.header('Line chart by geographies')
line_fig = px.line(avocado[avocado['geography'] == 'Los Angeles'],
                   x='date', y='average_price',
                   color='type',
                   title='Avocado Prices in Los Angeles')
st.plotly_chart(line_fig)

# 정적 페이지 만들기위한 select box
selected_geography = st.selectbox(label='Geography', options=avocado['geography'].unique())
submitted = st.button('Submit')
if submitted:
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    st.plotly_chart(line_fig)