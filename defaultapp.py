#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        income1 = request.form.get("income")
        age1 = request.form.get("age")
        loan1 = request.form.get("loan")
        income = float(float(income1) - 45133.788162)/(14426.484876)
        age = float(float(age1) - 34.860629)/(12.654700)
        loan = float(float(loan1) - 5591.682849)/(3174.972365)
        print (income, age, loan)
        model = joblib.load("Default")
        pred = model.predict([[float(income), float(age), float(loan)]])
        
        pred = pred[0]
        s = "The predicted default is : " + str(pred)
        return(render_template("index.html", result = s))
        print(pred)
    else:
        return(render_template("index.html", result = "Predicting Credit Card Default Risk, 1 meaning default and 0 meaning no default"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




