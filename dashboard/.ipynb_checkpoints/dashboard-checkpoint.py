import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('bikes_df.csv')

def create_byseason_df(df):
    byseason_df = df

    return byseason_df

def create_byworkingday_df(df):
    byworkingday_df = df

    return byworkingday_df

def create_byholiday_df(df):
    byholiday_df = df

    return byholiday_df

def create_byhour_df(df):
    byhour_df = df

    return byhour_df

df['datetime'] = pd.to_datetime(df["datetime"])

min_date = df["datetime"].min()
max_date = df["datetime"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    # st.image("https://i.pinimg.com/originals/ce/56/99/ce5699233cbc0f142250b520d967dff7.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


main_df = df[(df["datetime"] >= str(start_date)) & 
                (df["datetime"] <= str(end_date))]

byseason_df = create_byseason_df(main_df)
byworkingday_df = create_byworkingday_df(main_df)
byholiday_df = create_byholiday_df(main_df)
byhour_df = create_byhour_df(main_df)

colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

st.header('Bike Sharing Dashboard')

st.subheader("Count of Bikes During Weekdays and Weekend")
 
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(
    data= byhour_df,
    y='total_count', 
    x='hour',  
    hue='weekday', 
    ax=ax
)
# ax.set(title='')
st.pyplot(fig)

st.subheader("Count of Bikes During Season")

fig, ax = plt.subplots(figsize=(20,5))
sns.barplot(
    data= byseason_df,
    y='total_count',
    x='season',  
    # hue='weekday', 
    ax=ax
)
# ax.set(title='')
st.pyplot(fig)

st.subheader("Count of Bike During Workingday and Holiday")

col1, col2 = st.columns(2)
 
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
 
    sns.barplot(
        y="total_count", 
        x="is_workingday",
        data=byworkingday_df.sort_values(by="total_count", ascending=False),
        # palette=colors,w
        ax=ax
    )
    ax.set_title("Count of Bike During Workingday", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
 
with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    # colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
    sns.barplot(
        x="is_holiday", 
        y="total_count",
        data=byholiday_df.sort_values(by="total_count", ascending=False),
        # palette=colors,
        ax=ax
    )
    ax.set_title("Count of Bike During Holiday", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
 