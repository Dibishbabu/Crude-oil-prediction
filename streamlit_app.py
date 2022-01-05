#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import matplotlib.pyplot as plt
import datetime


# In[2]:


with open("model.pkl", "rb") as f:
 mp=pickle.load(f)


# In[8]:


def run():
 st.title("Oil prices prediction")
 st.caption("Prices Forecasting")
if st.button("Forecast"):
 prediction = mp.predict(start=start_date,end=end_date)
run()


# In[ ]:




