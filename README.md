# Deploy a data dashboard for web application
# Table of Contents
1. [Installation.](#inst)
2. [Project Motivation.](#motiv)
3. [File Descriptions.](#file)
4. [Results.](#res)
5. [Licensing, Authors, and Acknowledgements.](#ac)

<a name="inst"></a>
## 1. Installation
The packages that I used in the Jupyter Notebook include:

Flask==1.1.1
gunicorn==20.0.4
Jinja2==2.11.1
numpy==1.18.1
pandas==1.0.1
plotly==4.5.4


<a name="motiv"></a>
## 2. Project Motivation

* Obtained relavant dataset files in `.csv` from World Bank 
* Created a **Flask back-end** 
* Cleaned and wranggled using **Pandas** and visualized the data using **Plotly**
* Displayed the result on **front end** and deployed the app to a **Heroku** server

<a name="file"></a>
## 3. File Descriptions

The back-end data cleaning, wraggling, and visualization process is in wrangling_scripts/wrangle_data.py
Front-end design is in myapp/templates/index.html

<a name="res"></a>
## 4. Results


<a name="ac"></a>
## 5. Licensing, Authors, and Acknowledgements

This project is licensed under the MIT License. You can find the original dataset via World Bank [here](https://www.kaggle.com/airbnb/seattle). 
