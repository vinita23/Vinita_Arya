#!/usr/bin/env python
# coding: utf-8

# In[7]:


numbers = [1, 2, 3, 4, 5]
sqr=list(map(lambda x:x**2,numbers))
print(sqr)


# In[9]:


fil=list(filter(lambda x:x%2==0,numbers))
print(fil)


# In[14]:


new=[i*i if i>1 else 0 for i in numbers]
new


# In[19]:


numbers[::-1]


# In[24]:


def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
                
x=7          
print(factorial(x))                


# In[28]:


def fac(n):
    if n==1:
        return 1
    else:
        return 1
        while count<n:
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
n=7
print(fac(n))


# In[3]:


pip install requests


# In[12]:


def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            num=max_num
    return max_num


# In[41]:


import requests as re
import warnings

def get_pincode(address):
    url=f"https://postalpincode.in/api/pincode/{address}"# url for pincode
    
    try:
        
        response=re.get(url,verify=False)# request to the URL
        
        if response.status_code==200:
            data=response.json()
        
            if data and data["Status"]=="Success":
                return data["PostOffice"][0]["Pincode"]
            
    except Exception as e:
        print(f"Error:{e}")
        return None   
    
addr= "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050"

pincode=get_pincode(addr)

if pincode:
    print("Correct Pincode is", (pincode))
else:
    print("pincode not found")


# In[ ]:




