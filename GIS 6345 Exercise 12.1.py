#!/usr/bin/env python
# coding: utf-8

# In[1]:


t = tuple('lupins')


# In[2]:


t


# In[3]:


t1 = 'a'


# In[4]:


type(t1)


# In[5]:


t1 = 'a',


# In[6]:


type(t1)


# In[7]:


def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


# In[8]:


text = 'I am a survivor'


# In[9]:


def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
       print letter, count 


# In[10]:


def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
       print('letter, count')


# In[11]:


most_frequent(text)


# In[12]:


from __future__ import print_function, division


# In[13]:


def most_frequent(s):
    s: string
    hist = make_histogram(s)
    t = []
    for x, freq in hist.items():
        t.append((freq, x))
    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)
    return res


# In[14]:


def make_histogram(s):
    s: string
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


# In[15]:


def read_file(filename):
    return open(filename).read()


# In[16]:


if __name__ == '__main__':
    string = read_file('emma.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)


# In[17]:


def read_file(filename):
    return open(filename).read()


# In[18]:


if __name__ == '__main__':
    string = read_file('words.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)


# In[19]:


most_frequent(string)


# In[20]:


if __name__ == '__main__':
    string = read_file('sgb-words.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)


# In[21]:


most_frequent(string)


# In[22]:


def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d


# In[23]:


print (most_frequent(W))


# In[24]:


N = (I am a Survivor)


# In[25]:


N = I am a Survivor


# In[26]:


N = 'I am a Survivor'


# In[27]:


def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d


# In[28]:


print (most_frequent(N))


# In[29]:


N = 'Imagine living on this planet for eternity'


# In[30]:


def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d


# In[31]:


print (most_frequent(N))


# In[ ]:




