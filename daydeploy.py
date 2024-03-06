import streamlit as st
import pandas as pd
import altair as alt

day_mapping = {
    0: 'Minggu',
    1: 'Senin',
    2: 'Selasa',
    3: 'Rabu',
    4: 'Kamis',
    5: 'Jumat',
    6: 'Sabtu'
}

# Read data
data = pd.read_csv('output_file.csv')

# Dashboard title
st.title("Distribusi Rent Sepeda Berdasarkan Hari")


day_grouped_data = data.groupby('weekday')
casual_by_day = day_grouped_data['casual'].sum().reset_index()
registered_by_day = day_grouped_data['registered'].sum().reset_index()
max_casual_day = casual_by_day['casual'].idxmax()
max_registered_day = registered_by_day['registered'].idxmax()
selected_user_type = st.selectbox('Select user type', ['casual', 'registered'])

highlight_color = 'red'
highlight_weight = 2

if selected_user_type == 'casual':
    chart = alt.Chart(casual_by_day).mark_bar().encode(
        x='weekday:N',
        y=alt.Y('casual:Q', title='Casual Count'),
        tooltip=['casual:Q']
    ).properties(
        title='Rent Untuk Pengguna Casual',
        width=800,
        height=400
    ).encode(
        color=alt.condition(
            alt.datum.casual == casual_by_day['casual'].max(),
            alt.value(highlight_color),
            alt.value('steelblue')
        ),
        strokeWidth=alt.condition(
            alt.datum.casual == casual_by_day['casual'].max(),
            alt.value(highlight_weight),
            alt.value(0.5)
        )
    )
    st.altair_chart(chart)

else:
    chart = alt.Chart(registered_by_day).mark_bar().encode(
        x='weekday:N',
        y=alt.Y('registered:Q', title='Registered Count'),
        tooltip=['registered:Q']
    ).properties(
        title='Rent Untuk Pengguna Registered ',
        width=800,
        height=400
    ).encode(
        color=alt.condition(
            alt.datum.registered == registered_by_day['registered'].max(),
            alt.value(highlight_color),
            alt.value('steelblue')
        ),
        strokeWidth=alt.condition(
            alt.datum.registered == registered_by_day['registered'].max(),
            alt.value(highlight_weight),
            alt.value(0.5)
        )
    )
    st.altair_chart(chart)

st.caption('Copyright (c) Andika Dibya 2024')





























