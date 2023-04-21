# Webstack-Portfolio_Project

`Back-end` `FASTAPI`

#### Concepts

_For this project, look at these concepts:_

## Resources

**Read or watch:**

* [FASTAPI Documentation](https://fastapi.tiangolo.com)
* [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
* [YOUTUBE Tutorial](https://www.youtube.com/watch?v=0sOvCWFmrtA&ab_channel=freeCodeCamp.org)
* [Using FastAPI to Build Python Web APIs](https://realpython.com/fastapi-python-web-apis/)
* [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
* [containerize your application](https://docs.docker.com/get-started/)

## General Requirement & Setup

#### All files are Python Scripts

* The first line of files is exactly shebang `#!/usr/bin/env python3`
* Code use the `pycodestyle` style (version 2.5)
* All modules have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions (inside and outside a class) have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

This project contains tasks for learning to create backend api service for social media with FastAPI.

## API Layout

+ [x]  **app**<br/>[app](app folder) contains router folder and a Python scripts that sets up a basic API app with the following files:
  + [routers](routers) contains 'auth.py', 'post.py', 'user.py', and 'vote.py' python files which contains the api's different endpoints.
    + [auth.py](auth.py) contains '/login' endpoint. This function accepts user's login credentials from postgres database and depends on the		 		session maker class to start and drop database table. If the input user does not exist or has wrong credentials, HTT			      P exception is raised. Otherwise, access token is generated to enable user login.
  + [main.py](main.py) Creates an app instance from FastAPI class imported from fastapi module. The app instance has CORSMiddleware configured to accept resources outside of a given domain. The app instance also regisers post.router, user.router, auth.router and vote.router routes. The root function returns home page for the fastapi application with end point '/' that simply outputs "Tena yistilign lehulachum"(Welcome in Amharic Language).
  + [config.py](config.py) The config file contains configuration file for environment variable. The environemnt variables are defined inside Settings class with base model 'BaseSettings' inherited from pydantic module. After defining the class, settings variable is instantiated using the constructed Settings class to be imported inside this folder.
  + [database.py](database.py) The database.py file contains our postgres database configuration URL and engine. The settings variable is used to pass the environment vairables to start our api database. The postgres database is integrated with the app instance by passing the defined 'SQLALCHEMY_DATABASE_URL' to the create engine class from sqlalchemy module. Sqlalchemy is postgres's ORM(obejct relational mapping) to communicate user's CRUD data requests to the fastapi database. Another function get_db manages the database session on each data operation using sessionmaker base class.
  + [models.py](models.py) Contains three classes 'Post', 'User' and 'Vote' all inheriting 'Base' from declarative_base() instance defined in database.py that will generate a new table and mapper when the class are called. All the field attributes for the table columns and their relationship among the tables are defined in each of the classes.
  + [oauth2.py](oauth2.py) Contains three classes: 'create_access_token', 'verify_access_token' and 'get_current_user' to create, verify and retreive a user credentials upon a user signing up, loggiing in and postingrespectively. OAuth2PasswordBearer is a dependency for the oauth2 authorisation with JWT token generated for each user to access the api serivces. The authentication bearer uses the default 'HS256 algorithm' to generate the token. These tokens are passes as arguments to the 'verify_access_token' and 'get_current_user' classes. The 'create_access_token' function accepts user's login data with python dict argument to generate and return token 'encoded_jwt'.
  + [schemas.py](schemas.py) Contains user response model classes to be passed to router's decorator functions inside the router folders. On each user's requests to the api: 'post' 'login' 'signup' 'vote' 'delete' and 'update', the api will respond this response models to the users. A base model is imported from pydantic model to be inherited to the class PostBase. 
  + [utils.py](utils.py) Contains a proxy object that makes it easy to use multiple PasswordHash objects at the same time. Instances of this class can be created by calling the constructor with the appropriate keywords, or by using one of the alternate constructors, which can load directly from a string or a local file. The CryptContext class accepts 'bcrypt' schemes that is responsible to hash users password passed to the hash function which will return hashed password.
       
+ [x] 5. **Mock logging in**
  + Copy [4-app.py](4-app.py) into [5-app.py](5-app.py) and [templates/4-index.html](templates/4-index.html) into [templates/5-index.html](templates/5-index.html).
  + Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table into [5-app.py](5-app.py).
    ```python
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    ```
  + This will mock a database user table. Logging in will be mocked by passing `login_as` URL query parameter containing the user ID to log in as.
  + Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.
  + Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.
  

+ [x] 6. **Use user locale**
  + Copy [5-app.py](5-app.py) into [6-app.py](6-app.py) and [templates/5-index.html](templates/5-index.html) into [templates/6-index.html](templates/6-index.html).
  + Change your `get_locale` function to use a user’s preferred locale if it is supported.
  + The order of priority should be:
    1. Locale from URL parameters.
    2. Locale from user settings.
    3. Locale from request header.
    4. Default locale.
  + Test by logging in as different users.<br/>
    ![Hello World! in French with a logged in message](assets/task_6_1.png)
