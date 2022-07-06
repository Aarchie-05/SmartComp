<p align="center">
    <img alt="smartcomp" width="180px" height="30px" src="https://github.com/Aarchie-05/SmartComp/blob/master/static/images/SMARTCOMP.png">
</p>

<p align="center">
   A smart tool to compare and analyse prices and reviews of products across various e-commerce websites.
</p>


## Project Description

Users access the internet and get the information through different E-commerce websites. This approach to find and compare data from different websites is a time-consuming task.

To ease this process, we will enable the user to use our search engine which launches web crawler that dynamically crawls different e-commerce websites for deals on the searched product, which is presented in an easy to compare format along with the analysis of the reviews provided by the customers.

<p align="center">
    <img alt="amazon" width="" height="" src="https://github.com/Aarchie-05/SmartComp/blob/master/static/images/Amazon%20logo.png">
    <img alt="flipkart" width="" height="" src="https://github.com/Aarchie-05/SmartComp/blob/master/static/images/Flipkart%20logo.png">
</p>

## Abstract

“SmartComp” is a smart tool to compare and analyse prices and reviews of products 
across various e-commerce websites. Our application is built on Django – a python 
backend framework, implementing HTML, CSS, Javascript and Jquery on the front end. 
We have also used various python libraries for various purposes. Selenium was used by 
us to scrape the data off of ecommerce websites. Celery – task scheduling library and 
Redis – message broker were also used to make the tasks of scraping of data 
asynchronous to boost our application speed. Certain other libraries like bs4, lxml, re, 
pandas, etc, were also used for developmental and testing purposes


## Steps to Run the Application

Run the following command inside the virtual environment in order to install all the 
packages needed.

<p>
  <code>
     pip install -r requirements.txt
  </code>
</p>

Activate the celery and redis servers by following commands:
   <p>
      <code>
         celery -A SmartComp worker -l info -P gevent
      </code>
   </p>
   <p align="center">
      <img alt="celery" width="" height="" src="https://github.com/Aarchie-05/SmartComp/blob/master/Screenshots/celery%20connection.PNG">
   </p>
   
To run the django application on the local server by running the following command on command prompt:
   <p>
      <code>
         python manage.py runserver
      </code>
   </p>
   <p align="center">
      <img alt="celery" width="" height="" src="https://github.com/Aarchie-05/SmartComp/blob/master/Screenshots/Django%20server.PNG">
   </p>
   
Click on the link that will appear after running the command.


## Application Images

#### Best Deals
<p align="center">
      <img alt="1" width="" height="" src="https://github.com/Aarchie-05/SmartComp/blob/master/Screenshots/1.PNG">
</p>

#### Primary Deals
<p align="center">
      <img alt="2" width="" height="" src="https://github.com/Aarchie-05/SmartComp/blob/master/Screenshots/2.PNG">
</p>

#### Other Deals
<p align="center">
      <img alt="3" width="" height="" src="https://github.com/Aarchie-05/SmartComp/blob/master/Screenshots/3.PNG">
</p>

#### Primary Deals
<p align="center">
      <img alt="4" width="" height="" src="https://github.com/Aarchie-05/SmartComp/blob/master/Screenshots/4.PNG">
</p>

  
  
## Links

1. [Project Report](https://github.com/Aarchie-05/SmartComp/blob/master/SmartComp%20Project%20Report.pdf)
2. [Prensentation](https://github.com/Aarchie-05/SmartComp/blob/master/SmartComp.pptx)


   
   


