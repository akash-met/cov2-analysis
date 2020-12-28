import streamlit as st

import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns 
#matplotlib.use('Agg')
import seaborn as sns 


#Remove Warnings
st.set_option('deprecation.showPyplotGlobalUse', False)


st.markdown("<h1 style='text-align: center; color: red;'>Performance of Cars</h1>", unsafe_allow_html=True)

#st.title("Performance of Cars")
#import dataset
car = pd.read_csv('mtcars.csv')
pd.set_option('display.max_rows', None)
car
st.write("Here is 31 models of car with it's specifications")

#Display the table
#st.table(car)
#bar plot
car1 = car.sort_values(by=['wt'])
cy = sns.barplot(x=car1.model[0:20],y=car1.wt)
cy.set_xticklabels(cy.get_xticklabels(),rotation=90)
cy.set(xlabel="Model")
cy.set_ylabel("Weight of car", rotation=90)
cy.set_title('Weight of Cars', fontsize=20,)
st.pyplot()

#violin plot
cylhp = sns.violinplot(x='cyl', y="hp", data=car, palette='Set1')
cylhp.set(xlabel="Number of Cylinders")
cylhp.set_ylabel("Horse power of vehicle", rotation=90)
cylhp.set_title('Relationship between Number of Cylinders \n and Power of Vehicle', fontsize=15,)
st.pyplot()
st.write("From the figure above it is clear that the vehicles having higher number of cylinders can give more power")


#Displot
qsecs = sns.distplot(car['qsec'])
qsecs.set_xlabel("qsec(Time in seconds to travel 1/4 mile from standstill)")
qsecs.set_title('Speed performance of Cars from Standstill', fontsize=15,)
st.pyplot()

st.write("Most cars are taking 17 to 18 seconds to cover 1/4 miles from standstill")



#line plot
st.header("Relationship between Hourse Power and Weight of Vehicle")
sns.lineplot(x='wt', y='hp', data=car)
st.pyplot()

#joinplot
st.header("JointPlot of Weight and Horse power of vehicle")
sns.jointplot(x='wt',y='hp',data=car,kind='scatter')
st.pyplot()




#Correation
st.header("Heatmap showing the Correlation between different variables")
sns.heatmap(car.corr(),cmap='coolwarm',annot=True)
st.pyplot()
st.write("Number of cylinders to Horse power and displacement show a correlation of 0.83and 0.9 respectively")


