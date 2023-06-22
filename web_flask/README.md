# 0x04. AirBnB clone - Web framework

20180813 - The purpose of this project is to introduce the use of the web framework Flask

### 0-hello_route.py, __init__.py
A script that starts a flask application
Routes:
/: display “Hello HBNB!”

### 1-hbnb_route.py
A script that starts a flask application
Routes:  
/: display “Hello HBNB!”  
/hbnb: display “HBNB”

### 2-c_route.py
A script that starts a flask application  
Routes:  
/: display “Hello HBNB!”  
/hbnb: display “HBNB”  
/c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )

### 3-python_route.py
A script that starts a flask application  
/: display “Hello HBNB!”  
/hbnb: display “HBNB”  
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )  
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )  
The default value of text is “is cool”

### 4-number_route.py
A script that starts a flask application  
/: display “Hello HBNB!”  
/hbnb: display “HBNB”  
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )  
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )  
The default value of text is “is cool”  
/number/<n>: display “n is a number” only if n is an integer

### 5-number_template.py, templates/5-number.html
A script that starts a flask application  
/: display “Hello HBNB!”  
/hbnb: display “HBNB”  
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )  
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )  
The default value of text is “is cool”  
/number/<n>: display “n is a number” only if n is an integer  
/number_template/<n>: display a HTML page only if n is an integer:  
H1 tag: “Number: n” inside the tag BODY

### 6-number_odd_or_even.py, templates/6-number_odd_or_even.html
/: display “Hello HBNB!”  
/hbnb: display “HBNB”  
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )  
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )  
The default value of text is “is cool”  
/number/<n>: display “n is a number” only if n is an integer  
/number_template/<n>: display a HTML page only if n is an integer:  
H1 tag: “Number: n” inside the tag BODY  
/number_odd_or_even/<n>: display a HTML page only if n is an integer:  
H1 tag: “Number: n is even|odd” inside the tag BODY

### models/engine/file_storage.py, models/engine/db_storage.py, models/state.py
update FileStorage to to deserialize JSON file  
update DBStorage with close(self) method that calls remove on private session attribute  
update State with getter method to return list of City objects from storage linked to the current state  

### web_flask/7-states_list.py, web_flask/templates/7-states_list.html
A script that starts a Flask application  
You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)  
After each request you must remove the current SQLAlchemy Session:  
Declare a method to handle @app.teardown_appcontext  
Call in this method storage.close()  
Routes:  
/states_list: display a HTML page: (inside the tag BODY)  
H1 tag: “States”  
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip  
LI tag: description of one State: <state.id>: <B><state.name></B>  
Import this 7-dump to have some data

### web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html
A script that starts a Flask application  
use the public getter method cities  
After each request you must remove the current SQLAlchemy Session:  
Declare a method to handle @app.teardown_appcontext  
Call in this method storage.close()  
Routes:  
/cities_by_states: display a HTML page: (inside the tag BODY)  
H1 tag: “States”  
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip  
LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)  
LI tag: description of one City: <city.id>: <B><city.name></B>  
Import this 7-dump to have some data

### web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/
A script that starts a Flask application  
To load all cities of a State:  
If your storage engine is DBStorage, you must use cities relationship  
Otherwise, use the public getter method cities  
After each request you must remove the current SQLAlchemy Session:  
Declare a method to handle @app.teardown_appcontext  
Call in this method storage.close()  
Routes:  
/hbnb_filters: display a HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static  
Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css from web_static/styles/ to the folder web_flask/static/styles  
Copy files icon.png and logo.png from web_static/images/ to the folder web_flask/static/images  
Update .popover class in 6-filters.css to allow scrolling in the popover and a max height of 300 pixels.  
Use 6-index.html content as source code for the template 10-hbnb_filters.html:  
Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;  
State, City and Amenity objects must be loaded from DBStorage and sorted by name (A->Z)
