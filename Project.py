#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:




#code to explore the Bikeshare of three cities inthe US



#Dictionary containing the Bikesharedata location of the 3 cities
cities= { 'Chicago':"chicago.csv",
         'Washington':"washington.csv",
         'NYC':"new_york_city.csv",
         'Glasgow':"Glasgow.csv",

       }


months= ['january', 'february','march', 'april', 'may', 'june', ]

#different ways by which the data can be filteresd
filter_type =['day','month', 'both', 'none']

days=['monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']
var = ['yes','no']


#function to request for the various information required

def infos(m):

    #calculating for the most common month
    print('\ncalculating for the most common month...')
    most_common_month=m['month'].mode()[0]
    months= ['january', 'february','march', 'april', 'may', 'june']
    most_common_months=months[most_common_month -1]
    print('The most common month is: ', most_common_months)

   #calculating for the most common hour
    print('\ncalculating for the most common hour...')
    most_common_hour=m['hour'].mode()[0]
    print('The most common hour is: ', most_common_hour)

   #calculating for the most common day of the week
    print('\ncalculating for the most common day of the week ...')
    most_common_Day_of_week=m['Day_week'].mode()[0]
    print('most_common Day of week: ', most_common_Day_of_week)


   #calculating for the most common Start Station
    print('\ncalculating for the most common Start Station ...')
    most_common_start_station= m["Start Station"].mode()[0]
    print('The most common start station: ', most_common_start_station)


   #calculating for the most common end Station
    print('\ncalculating for the most common end Station ...')
    most_common_end_station= m["End Station"].mode()[0]
    print('The most common end station:', most_common_end_station)


   #calculating for the most common trip from start to end (i.e., most frequent combination of start station and end station)
    print('\ncalculating for the most common trip from start to end ...')
    var1=m.groupby(['Start Station','End Station']).count()
    most_common_trip_start_to_end = var1['Start Time'].idxmax()
    print('The most common trip start to end is: ', most_common_trip_start_to_end)


   #calculating for the total travel time
    print('\ncalculating for the Total travel time ...')
    total_travel_time = m["Trip Duration"].sum()
    print('The total travel time: ',total_travel_time)

    #calculating for the Average travel time
    print('\ncalculating for the Average travel time ...')
    Average_travel_time = m["Trip Duration"].mean()
    print('The Average travel time: ',Average_travel_time)
    Average_travel_time = m["Trip Duration"].mean()
    print('The Average travel time: ',Average_travel_time)

    #calculating for the count of each user type
    print('\ncalculating for the count of each user type ...')
    user_count =m['User Type'].value_counts()
    print('The counts of each user type: \n', user_count)

#if the city is NYC or Chicago, call this function to calculate  counts of each gender and the earliest, most recent, most common year of birth  because they aer only available for NYC and Chicago

def callf2(m):
       #calculating the count of each gender
       print('\ncalculating the count of each gender ...')
       gender=m['Gender'].value_counts()
       print('The count of each gender is: \n',gender)

       #calculating the birth year of the oldest user
       print('\ncalculating the birth year of the oldest user...')
       oldest_user= m['Birth Year'].min()
       print('The oldest user was born in the year: ', oldest_user)

       #calculating the birth year of the youngest user
       print('\ncalculating the birth year of the youngest user...')
       youngest_user= m['Birth Year'].max()
       print('The youngest user was born in the year: ', youngest_user)

       #calculating the most common birth year
       print('\ncalculating the most common birth year ...')
       most_common_birth_year = m['Birth Year'].mode()[0]
       print('The most common birth year is: ',most_common_birth_year)



#the main function
def main():

   #request the name of a city. Run this loop until the user inputs a valid
   while True:
        user_input1 = input(' which city will you like to explore?\n please input one of the cities listed above (NYC for new_york_city)\n')
        if user_input1 in cities:

            break


   #take the name of the city and loads it corresponding table
   p= pd.read_csv(cities[user_input1])

    # convert the Start Time column to datetime
   p['Start Time'] = pd.to_datetime(p['Start Time'])

   # extract hour,year,month and day of week from Start Time to create new columns
   p['hour'] = p['Start Time'].dt.hour
   p['year'] = p['Start Time'].dt.year
   p['month'] = p['Start Time'].dt.month
   p['Day_week'] = p['Start Time'].dt.weekday_name


   print("\n How would you like to filter the data; 'day','month', 'both' or  'none' ('none' for no time filter)")
   #requset for how the user will like to filter the data. Run this loop until the user inputs a valid way
   while True:
        user_input=input('\n Please input one of the above ways: ')
        if user_input in filter_type:

            break
   #if the user doesn't want to filter by time
   if user_input == 'none':
       p==p

   #if the user wants to filter by both the month and the day



   elif user_input == 'both':

       #requset for a month between jan and jun. Run this loop until the user inputs a valid month
       while True:
            months= ['january', 'february','march', 'april', 'may', 'june']
            user_input2=input("please input one of the following month 'january', 'february','march', 'april', 'may', 'june'")
            if user_input2 in months:

                break
       #requset for a day of the week. Run this loop until the user inputs a valid day of the week
       while True:
            user_input3=input('please input the name of a valid day of the week: ')
            if user_input3 in days:

                break

       months= ['january', 'february','march', 'april', 'may', 'june']
       month = months.index(user_input2) + 1

       p = p[p['month'] ==month]

       p = p[p['Day_week'] == user_input3.title()]

   #if the user wants to filter by month only




   elif user_input == 'month':
       #requset for a month between jan and jun. Run this loop until the user inputs a valid month
       while True:
            months= ['january', 'february','march', 'april', 'may', 'june']
            user_input4=input("please input one of the following month 'january', 'february','march', 'april', 'may', 'june'")
            if user_input4 in months:

                break

       month = months.index(user_input4) + 1
       p = p[p['month'] ==month]




   #if the user wants to filter by day only
   elif user_input == 'day':
       #requset for a day of the week. Run this loop until the user inputs a valid day of the week
       while True:
            user_input5=input('please input the name of a valid day of the week: ')
            if user_input5 in days:

                break
       p = p[p['Day_week'] == user_input5.title()]

   #pass in the generated Dataframe into the infos function to for the various information of interest
   infos(p)



#check if city is NYC or Chicago,and request for counts of each gender and the earliest, most recent, most common year of birth


   #check if city is Chicago
   if user_input1 == 'Chicago' :
     callf2(p)
     print('\n this data was for', user_input1)

        #check if city is Chicago
        if user_input1 == 'Chicago' :
          callf2(p)
          print('\n this data was for', user_input1)

   #check if city is NYC
   elif user_input1 == 'NYC' :
     callf2(p)
     print('\n this data was for', user_input1)

      elif user_input1 == 'NYC' :
        callf2(p)
        print('\n this data was for', user_input1)

          #check if city is NYC
          elif user_input1 == 'NYC' :
            callf2(p)
            print('\n this data was for', user_input1)

             elif user_input1 == 'NYC' :
               callf2(p)
               print('\n this data was for', user_input1)

    #check if city is Washington
   elif user_input1 == 'Washington' :
       print('counts of each gender and the earliest, most recent, most common year of birth does not apply to Washington')
       print('\n this data was for', user_input1)


           #check if city is Washington
          elif user_input1 == 'Washington' :
              print('counts of each gender and the earliest, most recent, most common year of birth does not apply to Washington')
              print('\n this data was for', user_input1)




   #ask if the user wants to see the first five rows of data
   user_input7=input('would you like to see the first five rows of data \n please enter "yes" or "no" ')
   a=0
   b=5
   var=['yes','no']
   if user_input7 == 'yes':
       print(p.iloc[a:b])
        #ask if the user wants to see the next five rows of data
       while True:

           while True:
               print('\n\nwould you like to see the next five rows')
               user_input8=input('please enter "yes" or "no" ')
               if user_input8 in var:
                   break

           if user_input8 == 'yes':
               b+=5
               a+=5
               print(p.iloc[a:b])
           elif user_input8 == 'no':
               print('program continuing ...\n\n')
               break


   elif user_input7 == 'no':
       print('Program continueing...\n\n')




#Start of code

print('\n\nHello! let\'s Explore some US bikeshare Data.\n')
print(" This program contains data for three cities over a period of sixe months; jan-jun \n\n Chicago,\n Washington and\n New York City(NYC)")

while True:
   #run this loop until user enters a valid answer
   while True:
       print('\nwould you like to explore any city?')
       user_input7=input('please enter "yes" or "no" \n')
       if user_input7 in var:
           break

   if user_input7 == 'yes':
       main()
   elif user_input7 == 'no':
       print('Program has stop runnng')
       print('Thanks for using this program')
       break




# In[ ]:
