import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title='Market Basket Analysis', 
                        page_icon = ':rocket:', 
                        initial_sidebar_state = 'auto',
                        layout='wide')
st.image("ch.png",use_column_width=True,width=800)
st.title("Market Basket Analysis Demo :shopping_trolley:🤖")
data = pd.read_excel("result.xlsx")

selected_antecedent = st.selectbox('Select an Item :shopping_trolley:', data['item1'].unique())
dataframe,chart = st.columns([6,4])








with dataframe:
    
    
    filtered_data = data[data['item1'] == selected_antecedent]
    filtered_data['support']=(filtered_data['support'] * 100).apply(lambda x: f'{x:.2f}%')
    filtered_data = filtered_data.sort_values(by='support', ascending=False)
    
    st.dataframe(filtered_data[['item2', 'support']],hide_index=True,width=600)

with chart:
    filtered_scatter_data = data[data['item1'] == selected_antecedent]
    fig = px.scatter(
        filtered_scatter_data,
        x='support',
        y='lift',
        
        hover_name=filtered_scatter_data['item2']  # Set hover_name to show item names
    )
    fig.update_layout(margin=dict(t=0))  # Set the top margin to 0, moving the chart closer to the dataframe
    st.plotly_chart(fig)









