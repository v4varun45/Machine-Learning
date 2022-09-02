#!/usr/bin/env python
# coding: utf-8

# # Question1

# In[4]:


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)


# In[5]:


min(ages)


# In[6]:


max(ages)


# In[7]:


ages


# In[8]:


z=len(ages)
z


# In[6]:


ages.append(ages[0])
ages.append(ages[z-1])


# In[7]:


ages

Median
# In[8]:


x=len(ages)//2 # Middle item
if len(ages)%2==0:
    y=(ages[x]+ages[x-1])/2
else:
    y=ages[x]/2


# In[9]:


print(y)

Average
# In[10]:


average=sum(ages)/len(ages)
average


# In[ ]:


Range


# In[11]:


range=max(ages)-min(ages)
range


# # Question2

# In[12]:


Dog={}


# In[13]:


Dog[0]='name'
Dog[1]='colour'
Dog[2]='breed'
Dog[3]='legs'
Dog[4]='age'


# In[14]:


Dog


# In[16]:


Student={}
Student['first_name'] = 'Sai'
Student['last_name'] = 'Vamshi'
Student['gender'] = 'Male'
Student['age'] = '25'
Student['maritual status'] = 'No'
Student['skills'] =['speaking' ,'reading']
Student['country'] = 'USA'
Student['city'] = 'Kansas'
Student['address'] = 'Apt 115, Armour Blvd'


# In[10]:


Student


# In[11]:


len(Student)


# In[12]:


Student['skills']=['speaking' ,'reading', 'writing']


# In[13]:


type('skills')


# In[14]:


Student


# In[21]:


key_list=list(Student.keys())
values_list=list(Student.values())
print(key_list)
print(values_list)


# # Question3

# In[18]:


Sisters=('Priyanka', 'Akanksha')
Brothers=('Anand', 'Sai')


# In[19]:


Siblings=Sisters+Brothers
Siblings


# In[20]:


len(Siblings)


# In[24]:


Modify=list(Siblings)


# In[25]:


type(Modify)


# In[26]:


Modify.append('Raju')


# In[27]:


Modify.append('Lakshmi')


# In[28]:


Siblings=tuple(Modify)


# In[29]:


Family_members=Siblings


# In[30]:


Family_members


# In[31]:


type(Family_members)


# # Question4

# In[21]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


# In[22]:


len(it_companies)


# In[23]:


it_companies.add('Twitter')


# In[24]:


it_companies


# In[25]:


it_companies.update(['Cognizant', 'Infosis'])


# In[26]:


it_companies


# In[27]:


it_companies.discard('Cognizant')


# In[28]:


it_companies


# In[29]:


it_companies.discard('TCS')


# In[30]:


it_companies.remove('TCS')

# Difference between discard and remove?

 Discard will not give error if you want to discard the item which is not present in the set but remove will give error


# In[31]:


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# In[32]:


c= A.union(B)
c


# In[33]:


d=A.intersection(B)
d


# In[34]:


print(A.issubset(B))


# In[35]:


print(A.isdisjoint(B))


# In[36]:


e=A.union(B)
f= B.union(A)
print(e)
print(f)


# In[37]:


g=A.symmetric_difference(B)
g


# In[38]:


h=A.clear()
print(h)


# In[39]:


i=B.clear()
print(i)


# In[40]:


age = [22, 19, 24, 25, 26, 24, 25, 24]


# In[41]:


new=set(age)
new


# In[42]:


len(age)


# In[43]:


len(new)


# In[44]:


len(age)==len(new)


# # Question5

# In[45]:


import math


# In[46]:


math.pi


# In[47]:


radius= 30
area_of_circle= math.pi * radius * radius
area_of_circle


# In[48]:


circum_of_circle= 2 * math.pi * radius
circum_of_circle


# In[49]:


r= float(input('Radius of circle'))
Area= math.pi * r * r
Area


# # Question6

# In[50]:


words= " I am a teacher and I love to inspire and teach people ".split()


# In[51]:


words


# In[55]:


len(words)


# In[52]:


unique = set(words)
unique


# In[56]:


len(unique)


# # Question7

# In[53]:


print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")


# # Question8

# In[54]:


rad=10
Area= int(3.14 * rad**2)
print("The area of a circle with radius {} is {} meters square".format(rad,Area))


# # Question9

# In[2]:


n=int(input('Enter how many values '))
lbs=[]
kgs=[]
for i in range(0,n):
    N =int(input(''))
    lbs.append(N)
    kgs.append(N*0.453592)
print(lbs) 
print(kgs)


# In[ ]:





# In[ ]:




