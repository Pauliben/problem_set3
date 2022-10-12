#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Problem 1
#Write a script (or Jupyter Notebook code block) that opens the file, uses a for loop to read through the file line by line and reports the highest water level and the date and time that was observed.

import os
os.chdir('/Users/paul.adunola/Desktop')

import pandas as pd
fhand = pd.read_csv(r'CO-OPS__8729108__wl.csv')

water_level = 0
for line in fhand.index:
    max_water_level = fhand[' Water Level'][line]
    if max_water_level > water_level:
        water_level = max_water_level
print(f"The maximum water level is {water_level}")
max_water_level = fhand[fhand[' Water Level'] == water_level]
print(f"The average water level was recorded on {max_water_level['Date Time'].to_string(index=False)}")


# In[3]:


#Problem 2
#Either in a new script or modifying the above script, calculate the lowest, highest and average water level observed during the time period. As above, print the date and time for the lowest and highest readings. 

contain_max_water_level = fhand[fhand['Date Time'].str.contains('2018-10-10')]

water_level_dat = []
for line in contain_max_water_level.index:
    num = contain_max_water_level[' Water Level'][line]
    if str(num) != 'nan':
        water_level_dat.append(num)

#Average water level
avg_water_level = sum(water_level_dat)/len(water_level_dat)
print(f"The average water level on 2018-10-10 is {avg_water_level}")

#Highest water level
highest_water_level = contain_max_water_level[contain_max_water_level[' Water Level'] == contain_max_water_level[' Water Level'].max()]
print(f"The highest water level on 2018-10-10 is {highest_water_level['Date Time'].to_string(index=False)}")

#Lowest water level
lowest_water_level = contain_max_water_level[contain_max_water_level[' Water Level'] == contain_max_water_level[' Water Level'].min()]
print(f"The lowest water level on 2018-10-10 is {lowest_water_level['Date Time'].to_string(index=False)}")


# In[4]:


#Problem 3
#Write a script (or Jupyter Notebook) that calculates the fastest rise in water level per 6-minute period between measurements (for this assignment, assume that each line of the dataset is a 6-minute interval) and reports the date and time that was observed and the change in water level from the previous recording.

water_rise = 0
for line in fhand.index:
    if line > 1:
        new_water_level = fhand[' Water Level'][line]
        diff_water_level = new_water_level - fhand[' Water Level'][line-1]
        if diff_water_level > water_rise:
            water_rise = diff_water_level
            water_level = new_water_level
print(f"The maximum water level is {round(water_rise,2)}")
max_water_rise_dat = fhand[fhand[' Water Level'] == water_level]
print(f"The maximum water level occured on {max_water_rise_dat['Date Time'].to_string(index=False)}")


# In[5]:


#Problem 4
#Imagine that the file is providing live readings of the water level. Write a script (or Jupyter Notebook) to print a line of text with a warning if any of these events occur:
#The water level increases more than 0.25 since the previous recording.
#The water level is over 5.0.
#No reading is received at a time point.

for line in fhand.index:
    if line > 1:
        new_water_level = fhand[' Water Level'][line]
        diff_water_level = new_water_level - fhand[' Water Level'][line-1]
        if diff_water_level > 0.25:
            water_rise = fhand[fhand[' Water Level'] == new_water_level]
            water_rise = water_rise['Date Time']
            print(f"Warning: Water level increases more than 0.25. Water level rise by {round(diff_water_level,2)} at {water_rise.to_string(index=False)}")
        if diff_water_level > 0.5:
            water_rise = fhand[fhand[' Water Level'] == new_water_level]
            water_rise = water_rise['Date Time']
            print(f"Warning: Water level increases more than 0.5. Water level rise by {round(diff_water_level,2)} at {water_rise.to_string(index=False)}")
        if str(new_water_level) == 'nan':
            #water_rise = fhand[fhand[' Water Level'] == 'nan']
            #water_rise = water_rise['Date Time']
            print(f"Warning: No reading is received at {fhand.loc[line,'Date Time']}")


# In[ ]:




