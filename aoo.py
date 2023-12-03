import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

# read csv
df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv") #https://github.com/Lexie88rus/bank-marketing-analysis.git")

st.set_page_config(
    page_title="Bank Marketing Analysis",
    page_icon=":bar_chart:",
    layout="wide",
    
)

st.title("Dynamic- Time Dashboard")
 
 
job_filter = st.selectbox("Select the aera to work ", pd.unique(df['job']))

placeholder = st.empty()

df = df[df['job']==job_filter]

for seconds in range(200):
    df['age_new'] = df['age'] *np.random.choice(range(1,5))
    df['balance_new'] = df['balance'] *np.random.choice(range(1,5))
    
    avg_age = np.mean(df['age_new'])
    
    count_marriage = int(df[(df["marital"]=='married')]['marital'].count() +np.random.choice(range(1,5)))
    
    balance = np.mean(df['balance_new'])
    
    with placeholder.container():
        #create three columns
        kpi1, kpi2, kpi3 = st.columns(3)
        
        #fill in those three columns with respective metrics
        kpi1.metric(label="Age", value=round(avg_age), delta = round(avg_age - 10))
        kpi2.metric(label="Marriage", value=int(count_marriage), delta = int(count_marriage - 2))
        kpi3.metric(label="Balance", value=f"$ {round(balance,2)}", delta = -round(balance - 100))
        
        fig_col1 , fig_col2 = st.columns(2)
        with fig_col1:
           st.markdown("### First Chart")
           fig = px.density_heatmap(data_frame=df, x="age_new", y="marital")
           st.write(fig)
        with fig_col2:
           st.markdown("### Second Chart")
           fig = px.histogram(data_frame=df, x="age_new")
           st.write(fig)
        st.markdown("### Detailed view ")
        st.dataframe(df)
        time.sleep(1)
        
        
        