
# coding: utf-8

# In[42]:

# 1. Min GPA
import csv
f = open("F:/ClassData.csv")
csv = csv.reader(f)

A=[]

for row in csv:
    A.append(row[1])
    

print(min(A))
    


# In[45]:

# 1. Max GPA
import csv
f = open("F:/ClassData.csv")
csv = csv.reader(f)

A=[]

i=0
for row in csv:
    if i:
        A.append(row[1])
    i=i+1;

print(max(A))


# In[61]:

# 1. Median GPA
import csv
import statistics
f = open("F:/ClassData.csv")
csv = csv.reader(f)

a =[]

i=0
for row in csv:
    if i:
        a.append(row[1])
    i=i+1;

cd = [float(i) for i in a]

print(statistics.median(cd))


# In[63]:

# 1. Average GPA
import csv
import statistics
f = open("F:/ClassData.csv")
csv = csv.reader(f)

a =[]

i=0
for row in csv:
    if i:
        a.append(row[1])
    i=i+1;

cd = [float(i) for i in a]

print(statistics.mean(cd))


# In[82]:

# 1. Min YearofWorkExp
import csv
f = open("F:/ClassData.csv")
csv = csv.reader(f)

A=[]

for row in csv:
    A.append(row[2])
    

print(min(A))


# In[83]:

# 1.Max YearofWorkExp
import csv
f = open("F:/ClassData.csv")
csv = csv.reader(f)

A=[]

i=0
for row in csv:
    if i:
        A.append(row[2])
    i=i+1;

print(max(A))


# In[86]:

# 1. Median YearofWorkExp
import csv
import statistics
f = open("F:/ClassData.csv")
csv = csv.reader(f)

a =[]

i=0
for row in csv:
    if i:
        a.append(row[2])
    i=i+1;

cd = [float(i) for i in a]

print(statistics.median(cd))


# In[87]:

# 1. Average YearofWorkExp
import csv
import statistics
f = open("F:/ClassData.csv")
csv = csv.reader(f)

a =[]

i=0
for row in csv:
    if i:
        a.append(row[2])
    i=i+1;

cd = [float(i) for i in a]

print(statistics.mean(cd))


# In[64]:

# 2.  Find the mode of the Salary
import csv
import statistics
f = open("F:/ClassData.csv")
csv = csv.reader(f)

a =[]

i=0
for row in csv:
    if i:
        a.append(row[3])
    i=i+1;

cd = [float(i) for i in a]

print(statistics.mode(cd))


# In[74]:

# 3. % of students having Co/op and not having Co/op
import csv
import statistics
f = open("F:/ClassData.csv")
csv = csv.reader(f)

a =[]

i=0
for row in csv:
    if i:
        a.append(row[6])
    i=i+1;
    
cd = [i.upper() for i in a]
    
var_yes = cd.count("Y")
var_no = cd.count("N")
var_total = len(cd)

percentage = var_yes/var_total * 100

print(percentage)


# In[81]:

# 4. No of students with more than 500 LinkedIn contacts
import csv
import statistics
f = open("F:/ClassData.csv")
csv = csv.reader(f)

a =[]

i=0
for row in csv:
    if i:
        a.append(row[7])
    i=i+1;

cd =list(map(int,a))
    
linkedInCount=0;
for link in cd:
    if link>500:
        linkedInCount = linkedInCount+1;
    
print(linkedInCount)


# In[94]:

#5. Find the Inter Quartile Range for the Expected Salalry Range?

import numpy as np 
import csv
import statistics

f = open("F:/ClassData.csv")
csv = csv.reader(f)

a =[]

i=0
for row in csv:
    if i:
        a.append(row[8])
    i=i+1;

cd =list(map(int,a))

q25 = np.percentile(cd, 25)
q75 = np.percentile(cd,75)

iqr = q75 - q25

print(iqr)


# In[ ]:



