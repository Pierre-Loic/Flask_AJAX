# Flask_AJAX
## Basic example of a Flask application with AJAX
This is a basic example to understand how you can use Flask with AJAX with the framework Jquery. The example is divided in 6 small steps in order to understand how data are sent from the front-end to the back-end and from the back-end to the front-end.
## Technologies used :
* Python with Flask
* HTML with Jinja2
* Javascript with Jquery
* Wikipedia API
## Steps of the example :
* STEP 1 (run.py)
The user opens the home page
* STEP 2 (main.html)
The user fills the input box with a word
* STEP 3 (main.html)
An AJAX request is sent to the url /test_ajax/
* STEP 4 (run.py)
Data are collected from the request and sent to an API
* STEP 5 (run.py)
API Data are sent back to the template
* STEP 6 (main.html)
div#reponse is updated with API data 
