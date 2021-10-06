#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:09:12 2021

@author: carolinapacheco
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importing files for 10 years 
dfData2018 = pd.read_csv('/Users/carolinapacheco/Documents/DSA4lWomen/DS4A Women _Capstone_Data/2018.csv')
dfData2017 = pd.read_csv('/Users/carolinapacheco/Documents/DSA4lWomen/DS4A Women _Capstone_Data/2017.csv')
dfData2016 = pd.read_csv('/Users/carolinapacheco/Documents/DSA4lWomen/DS4A Women _Capstone_Data/2016.csv')
dfData2015 = pd.read_csv('/Users/carolinapacheco/Documents/DSA4lWomen/DS4A Women _Capstone_Data/2015.csv')
dfData2014 = pd.read_csv('/Users/carolinapacheco/Documents/DSA4lWomen/DS4A Women _Capstone_Data/2014.csv')
dfData2013 = pd.read_csv('/Users/carolinapacheco/Documents/DSA4lWomen/DS4A Women _Capstone_Data/2013.csv')
dfData2012 = pd.read_csv('/Users/carolinapacheco/Documents/DSA4lWomen/DS4A Women _Capstone_Data/2012.csv')
dfData2011 = pd.read_csv('/Users/carolinapacheco/Documents/DSA4lWomen/DS4A Women _Capstone_Data/2011.csv')
dfData2010 = pd.read_csv('/Users/carolinapacheco/Documents/DSA4lWomen/DS4A Women _Capstone_Data/2010.csv')


#2018 flights data exploration
print (dfData2018.head)
print (dfData2018.columns)
dfData2018.columns
dfData2018.head
dfData2018.isna().sum()
dfData2018.info()
dfData2018.describe() #stats

#check number of cancelled flights and number of delayed flights
dfData2018['CANCELLED'].value_counts()
dfData2018['DIVERTED'].value_counts()
dfData2018['DEP_DELAY'].value_counts()

#flight date - converted 'date' from object to datetime
dfData2018['FL_DATE'] = pd.to_datetime(dfData2018['FL_DATE'])  
dfData2018['FL_DATE'].value_counts()

#carriers
dfData2018['OP_CARRIER'].nunique()

#show total number of flights per day 
d_flights = dfData2018[['FL_DATE', 'OP_CARRIER']].groupby(['FL_DATE'], as_index = False).count()
d_flights.plot(x = 'FL_DATE', y = 'OP_CARRIER')
plt.xlabel('Flight Date')
plt.ylabel('# of Flights')
plt.title('# of Flights per Day - 2018')

#number of flights per airline
sns.countplot(dfData2018['OP_CARRIER'])
plt.xlabel('Airline')
plt.ylabel('# of Flights')
plt.title('# of Flights by Airline - 2018')

#departue delays
d_delays= dfData2018['DEP_DELAY'].value_counts()
plt.plot(d_delays)
plt.xlabel('Minutes')
plt.ylabel('# of Delayed Flights')
plt.title('Total Delayed Flights - 2018')

#departure delays by airline
d_delays_airline = dfData2018[['OP_CARRIER', 'DEP_DELAY']].groupby(['OP_CARRIER']).count()
#plt.plot(d_delays_airline)
d_delays_airline.plot.bar()
plt.xlabel('Airline')
plt.ylabel('# of Delayed Flights')
plt.title('Delayed Flights by Airline - 2018')
plt.boxplot(d_delays_airline)

#departure delays by airport (there are more than 5K airports in the US)
d_delays_airport = dfData2018[['ORIGIN','DEP_DELAY']].groupby(['ORIGIN']).count()
d_delays_airport.plot.bar()
plt.xlabel('Airport')
plt.ylabel('# of Delayed Flights')
plt.title('Delayed Flights by Airport - 2018')
#plt.boxplot(d_delays_airport)

                
#diverted flights
diverted = dfData2018['DIVERTED'].value_counts()
print(diverted)
diverted.plot.bar()
plt.title('Diverted Flights 0 = No 1=Yes')

#cancelled flights
cancelled = dfData2018['CANCELLED'].value_counts()
print(cancelled)
cancelled.plot.bar()
plt.title('Cancelled Flights 0 = No 1=Yes')

#Cancelled and diverted flights
dfData2018.loc[:, ['CANCELLED','DIVERTED']]


#cancelled flights by airline
cancelled_airline = dfData2018[['CANCELLED', 'OP_CARRIER']].groupby(['OP_CARRIER']).count()
print(cancelled_airline)
cancelled_airline.plot.bar()
plt.xlabel('Airline')
plt.ylabel('# of Cancelled Flights')
plt.title('Cancelled Flights by Airline - 2018')

#diverted flights by airlined
diverted_airline = dfData2018[['DIVERTED', 'OP_CARRIER']].groupby(['OP_CARRIER']).count()
print(diverted_airline)
diverted_airline.plot.bar()
plt.xlabel('Airline')
plt.ylabel('# of Diverted Flights')
plt.title('Diverted Flights by Airline - 2018')

#cancelled & diverted flights
dcancelled_airline = dfData2018[['CANCELLED', 'DIVERTED','OP_CARRIER']].groupby(['OP_CARRIER']).count()
print(dcancelled_airline)
dcancelled_airline.plot.bar()
plt.xlabel('Airline')
plt.ylabel('# of Cancelled Flights')
plt.title('Cancelled & Diverted Flights by Airline - 2018')



