import streamlit as st
import pandas as pd



data = pd.read_excel("result.xlsx")




selected_antecedent = st.selectbox('Select an Item', data['item1'].unique())

# Filter the data based on the selected antecedent
filtered_data = data[data['item1'] == selected_antecedent]
filtered_data['support']=(filtered_data['support'] * 100).apply(lambda x: f'{x:.2f}%')
filtered_data = filtered_data.sort_values(by='support', ascending=False)

# Display the table of consequents with support
st.dataframe(filtered_data[['item2', 'support']],hide_index=True,width=800)









