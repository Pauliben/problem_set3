#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem 1
#Write a script (or Jupyter Notebook code block) that opens the file, uses a for loop to read through the file line by line and reports the highest water level and the date and time that was observed.

#Open data
data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS_8729108_wl.csv', mode='r')

#Create vectors and lists
max_water_level = 0
date_time = " "
data2 = []

#Restructure data
for line in data:
    line = line.rstrip()
    columns = line.split(sep = ',')
    #print(columns[1])
    data2.append(columns)

#Reports of the highest water level and the date and time
for index in range(len(data2)):
    columns = data2[index]
    try:
        water_level = float(columns[1])
    except:
        continue
    date= columns[0]
    #print(water_level)
    #print(date)
    if water_level > max_water_level:
        max_water_level = water_level
        date_time = date

print(f"The maximum water level is {max_water_level}")
print(f"The average water level was recorded on {date_time}")

data.close()


# In[ ]:


#Problem 2
#Either in a new script or modifying the above script, calculate the lowest, highest and average water level observed during the time period. As above, print the date and time for the lowest and highest readings. 

#Open data
data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS_8729108_wl.csv', mode='r')

#Define vectors and lists
contain_max_water_level = []
max_water_level = 0
min_water_level = [0]
date_time = " "

#Extract data on the day when maximum water level occured
for line in data:
    line = line.rstrip()
    columns = line.split(sep = ',')
    try:
        water_level = float(columns[1])
    except:
        continue
    date= columns[0]
    try:
        water_level = float(columns[1])
        if '2018-10-10' in date:
            contain_max_water_level.append(columns) 
    except:
        continue
    
#Calculate the lowest, highest and average water level observed    

water_level_dat = []

for line in range(len(contain_max_water_level)):
    columns = contain_max_water_level[line]
    date= columns[0]
    
    #To calculate average water level, remove nan
    try:
        num = float(columns[1])
        water_level = float(columns[1])
        if str(num) != 'nan':
            water_level_dat.append(num)
    except:
        continue
    
    #Determine maximum water level
    try:
        water_level = float(columns[1])
        if water_level > max_water_level:
            max_water_level = water_level
            max_date_time = date
    except:
        continue
    
    #Determine minimum water level
    try:
        water_level = float(columns[1])
        if line == 0:
            min_water_level = water_level
        if water_level < min_water_level:
            min_water_level = water_level
            min_date_time = date
    except:
        continue

#Average water level
avg_water_level = sum(water_level_dat)/len(water_level_dat)
print(f"The average water level is {round(avg_water_level,3)} on 2018-10-10")

#Highest water level
print(f"The highest water level is {max_water_level} on {max_date_time}")

#Lowest water level
print(f"The lowest water level is {min_water_level} on {min_date_time}")

data.close()


# In[ ]:


#Problem 3
#Write a script (or Jupyter Notebook) that calculates the fastest rise in water level per 6-minute period between measurements (for this assignment, assume that each line of the dataset is a 6-minute interval) and reports the date and time that was observed and the change in water level from the previous recording.

#Open data
data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS_8729108_wl.csv', mode='r')

#Define vectors and lists
water_rise = 0
data2 = []

#Restructure data
for line in data:
    line = line.rstrip()
    columns = line.split(sep = ',')
    data2.append(columns)

#calculates the fastest rise in water level
for index in range(len(data2)):
    columns = data2[index]
    try:
        if index > 1 and str(columns[1]) != 'nan':
            #Old water level
            Old_columns = data2[index-1]
            old_water_level = Old_columns[1]
            new_water_level = columns[1]
            diff_water_level = float(new_water_level) - float(old_water_level)
            if diff_water_level > water_rise:
                water_rise = diff_water_level
                water_level = new_water_level
                date_water_rise = columns[0]
    except:
        continue
        

print(f"The fastest rise in water level is {round(water_rise,2)}")
print(f"The fastest rise in occured on {date_water_rise}")

data.close()


# In[ ]:


#Problem 4
#Imagine that the file is providing live readings of the water level. Write a script (or Jupyter Notebook) to print a line of text with a warning if any of these events occur:
#The water level increases more than 0.25 since the previous recording.
#The water level is over 5.0.
#No reading is received at a time point.

#Open data
data = open('/blue/bsc4452/share/Class_Files/data/CO-OPS_8729108_wl.csv', mode='r')

#Define vectors and lists
water_rise = 0
data2 = []

#Restructure data
for line in data:
    line = line.rstrip()
    columns = line.split(sep = ',')
    #print(columns[1])
    data2.append(columns)

#The water level increases more than 0.25
for index in range(len(data2)):
    columns = data2[index]
    if index > 1:
        new_water_level = columns[1]
        Old_columns = data2[index-1]
        old_water_level = Old_columns[1]
        try:
            diff_water_level = float(new_water_level) - float(old_water_level)
            if diff_water_level > 0.25:
                #water_rise = diff_water_level
                date_water_rise = columns[0]
                print(f"Warning: Water level increases more than 0.25. Water level rise by {round(diff_water_level,2)} at {date_water_rise}")
        except:
            continue
        
#The water level is over 5.0
for index in range(len(data2)):
    columns = data2[index]
    if index > 1:  
        new_water_level = columns[1]
        try:
            new_water_level = float(new_water_level)
            if new_water_level > 5:
                water_level_gt_5 = new_water_level
                date_water_level_gt_5 = columns[0]
                print(f"Warning: Water level greater than 5. Water level is {round(water_level_gt_5,2)} at {date_water_level_gt_5}")
        except:
            continue

#No reading is received at a time point.
for index in range(len(data2)):
    columns = data2[index]
    if index > 1:
        new_water_level = columns[1]
        try:
            if len(new_water_level) == 0:
                date_no_reading = columns[0]
                print(f"Warning: No reading is received at {date_no_reading}")
        except:
            continue

data.close()


# In[ ]:





# In[ ]:




