import streamlit as st
import pandas as pd
import pickle
teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Kolkata Knight Riders',
 'Delhi Capitals',
 'Kings XI Punjab']

cities = ['Durban', 'Mumbai', 'Bloemfontein', 'Centurion', 'Hyderabad',
       'Chennai', 'Jaipur', 'Kolkata', 'Ranchi', 'Bangalore', 'Delhi',
       'Port Elizabeth', 'Bengaluru', 'Chandigarh', 'Abu Dhabi', 'Pune',
       'Indore', 'Cape Town', 'Dharamsala', 'Visakhapatnam', 'Raipur',
       'East London', 'Ahmedabad', 'Mohali', 'Johannesburg', 'Cuttack',
       'Nagpur', 'Sharjah', 'Kimberley']

st.title('IPL Win Prediction')

pipe = pickle.load(open('pipe.pkl','rb'))

col1 , col2 = st.columns(2)

with col1:
   batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
   bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select Host City',sorted(cities))


target = st.number_input("Target")

col3 , col4 , col5 = st.columns(3)

with col3:
    score=st.number_input("Score")

with col4:
   overs = st.number_input('Overs Completed')

with col5:
    wickets = st.number_input("Wickets Out")

if st.button("Predict Probability"):
   runs_left = target-score
   balls_left = 120-(overs*6)
   wickets = 10 - wickets
   crr = score/overs
   rrr =(runs_left*6)/balls_left
   input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
   
   result = pipe.predict_proba(input_df);
   loss = result[0][0]
   win = result[0][1]
   st.header(batting_team+"-"+ str(round(loss*100))+"%")
   st.header(bowling_team+"-"+ str(round(win*100))+"%")
