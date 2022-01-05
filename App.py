#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import numpy as np
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


# In[2]:


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')


# In[5]:


#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2) 
    return render_template('index.html', prediction_text='Price    Crude oil price prediction:{}'.format(output))


# In[ ]:


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    app.run()


# In[ ]:




