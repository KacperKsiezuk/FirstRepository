#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <center><img src='../../BlueSoft_logo.png' width="500" height="208"/></center>
# 
# ___

# # Flow control assessment test
# 
# Let's test your knowledge!

# 1. Using <code>for</code> loop, from the string below print out words that start with 's'.

# In[9]:


sentence = 'Print only the words that start with s in this sentence'


# In[5]:


for i in sentence:
    if sentence(i(0)) == 's':
        print(sentence(i))


# 2. Use <code>range()</code> to print all the even numbers from 0 to 10.

# In[2]:


for x in range(0, 11):
    if x % 2 == 0:
        print(x)
        continue


# 3. Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

# In[3]:


for x in range(1, 51):
    if x % 3 == 0:
        print(x)
        continue


# 4. Go through the string below and if the length of a word is even print "even!".

# In[13]:


another_sentence = 'Print every word in this sentence that has an even number of letters'


# In[4]:


for i in another_sentence:
    if len(i) % 2 == 0:
        print(i)


# 5. (*) Take two lists below and return a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your code works on two lists of different sizes.

# In[15]:


a = [1, 1, 2, 3, 5, 5, 5, 5, 8, 13, 21, 34]
b = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13]


# In[16]:




