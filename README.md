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

## General Setup

#### All files are Python Scripts

* The first line of files contains shebang `#!/usr/bin/env python3`
* Code use the `pycodestyle` style (version 2.5)

This project contains tasks for learning to create backend api service for social media with FastAPI.

## API Layout

+ [x]  **app**<br/> The app folder contains router folder and a Python scripts that sets up a basic API app with the following files:
  + The routers contains 'auth.py', 'post.py', 'user.py', and 'vote.py' python files which contains the api's different endpoints.
    + [auth.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/routers/auth.py) contains '/login' endpoint. This function accepts user's login credentials from postgres database and depends on the	session maker class to start and drop database table. If the input user does not exist or has wrong credentials, HTTP exception is raised. Otherwise, access token is generated to enable user login.
    + [post.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/routers/post.py) contains different user interations endpoints: 'create_post' - '/', 'get_post' - '/', 'get_one_post' - '/{id}', 'delete_post' - '/{id}', and 'update_post' - '/{id}' all with the '/posts' prefix defined in the APIRouter instance. All endpoints depends on 'oauth2.get_current_user' function to limit any user to be authenticted before making any CRUD operations. The 'get_posts' endpoint which retrieves all posts of a specific user contains default query parameter for flexible user experience.   
    + [user.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/routers/user.py) contains different user interations endpoints: 'create_user' - '/' and 'get_user' - '/' with 'users' prefix defined in the APIRouter instance. The 'create_user' endpoint accepts UserCreate response model from schemas for creating default attributes and stores in the database. 
    + [vote.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/routers/vote.py) Contains '/vote' endpoint to enable users like or dislike a specific post. The endpoint takes two positional arguments: 'vote' and 'current_user'. The current_user argument makes sure current user is  authenticted before making any CRUD operations. 
  + [main.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/main.py) Creates an app instance from FastAPI class imported from fastapi module. The app instance has CORSMiddleware configured to accept resources outside of a given domain. The app instance also regisers post.router, user.router, auth.router and vote.router routes. The root function returns home page for the fastapi application with end point '/' that simply outputs "Tena yistilign lehulachum"(Welcome in Amharic Language).
  + [config.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/config.py) The config file contains configuration file for environment variable. The environemnt variables are defined inside Settings class with base model 'BaseSettings' inherited from pydantic module. After defining the class, settings variable is instantiated using the constructed Settings class to be imported inside this folder.
  + [database.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/database.py) The database.py file contains our postgres database configuration URL and engine. The settings variable is used to pass the environment vairables to start our api database. The postgres database is integrated with the app instance by passing the defined 'SQLALCHEMY_DATABASE_URL' to the create engine class from sqlalchemy module. Sqlalchemy is postgres's ORM(obejct relational mapping) to communicate user's CRUD data requests to the fastapi database. Another function get_db manages the database session on each data operation using sessionmaker base class.
  + [models.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/models.py) Contains three classes 'Post', 'User' and 'Vote' all inheriting 'Base' from declarative_base() instance defined in database.py that will generate a new table and mapper when the class are called. All the field attributes for the table columns and their relationship among the tables are defined in each of the classes.
  + [oauth2.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/oauth2.py) Contains three classes: 'create_access_token', 'verify_access_token' and 'get_current_user' to create, verify and retreive a user credentials upon a user signing up, loggiing in and postingrespectively. OAuth2PasswordBearer is a dependency for the oauth2 authorisation with JWT token generated for each user to access the api serivces. The authentication bearer uses the default 'HS256 algorithm' to generate the token. These tokens are passes as arguments to the 'verify_access_token' and 'get_current_user' classes. The 'create_access_token' function accepts user's login data with python dict argument to generate and return token 'encoded_jwt'.
  + [schemas.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/schemas.py) Contains user response model classes to be passed to router's decorator functions inside the router folders. On each user's requests to the api: 'post' 'login' 'signup' 'vote' 'delete' and 'update', the api will respond this response models to the users. A base model is imported from pydantic model to be inherited to the class PostBase. 
  + [utils.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/app/utils.py) Contains a proxy object that makes it easy to use multiple PasswordHash objects at the same time. Instances of this class can be created by calling the constructor with the appropriate keywords, or by using one of the alternate constructors, which can load directly from a string or a local file. The CryptContext class accepts 'bcrypt' schemes that is responsible to hash users password passed to the hash function which will return hashed password.
       
+ [x]  **alembic**<br/> The alembic folder contains versions folder and env.py file that sets up enviroment configuration for the API app:
  + [env.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/alembic/env.py) Contains alembic Config object, which provides
access to the values within the .init file in use. The run_migrations_offline function configures the context with just a URL and not an Engine, though an Engine is acceptable here as well. By skipping the Engine creation, we don't even need a DBAPI to be available. Calls to context.execute() here emit the given string to the script output. The run_migrations_online function creates an Engine and associate a connection with the context.
  + [versions](https://github.com/twinnerhenock/Webstack-Portfolio_Project/tree/main/alembic/versions) This folder will contain every database new updates with separate files and 'alembic head' command followed by the respective version number allows easy databse updates and version control. 
   
+ [x]  **tests**<br/> The tests folder contains pytest testing modules for the parts of the fast api. Pytest is a testing framework based on python. It is mainly used to write API test cases. The folder contains pytest modules for testing post, user, vote and database classes.
  + [x] **Installation**<br/>
  + Install the pytest:
    ```powershell
    pip3 install pytest
    ```
    Confirm the installation using the following command to display the help section of pytest.
    ```
    pytest -h
    ```
  + [conftest.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/tests/conftest.py) Different fixtures are defined in this file to make them accessible across multiple test files. Test fixture 'session' is defined to bind database engine on every test as shown below. With the same token, test fixtures 'client', 'test_user', 'test_user2' and 'token' are defined and passed as arguments in other test modules for simplicity.
    ```powershell
    @pytest.fixture()
    def session():
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    ```
    
   + [test_posts.py](https://github.com/twinnerhenock/Webstack-Portfolio_Project/blob/main/tests/test_posts.py) Contains test functions to assert user's created, deleted, updated and retrieved posts. The py test parametrize decorator can be used pass in multiple assertion arguments as mock test as shown below. Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using the following marker −
     ```powershell
     @pytest.mark.parametrize
     ```
     Executed by running the following command −
     ```
     Pytest -k test_posts -v
     ```
     The test_create_post function is asserted for HTTP request status code, post attributes 'title', 'content', 'published' and 'owner_id'.

     ```powershell
     @pytest.mark.parametrize("title, content, published", [
         ("awesome new title", "awesome new content", True),
         ("favorite pizza", "i love pepperoni", False),
         ("tallest skyscrapers", "wahoo", True),
         ])
     def test_create_post(authorized_client, test_user, test_posts, title, content, published):
         res = authorized_client.post(
         "/posts/", json={"title": title, "content": content, "published": published})

         created_post = schemas.Post(**res.json())
         assert res.status_code == 201
         assert created_post.title == title
         assert created_post.content == content
         assert created_post.published == published
         assert created_post.owner_id == test_user['id']
     ```
  

+ [x] **docker-compose.yml**
  A a container is a sandboxed process on your machine that is isolated from all other processes on the host machine. That isolation leverages kernel namespaces and cgroups, features that have been in Linux for a long time. Docker has worked to make these capabilities approachable and easy to use. When running a container, it uses an isolated filesystem. This custom filesystem is provided by a container image. Since the image contains the container’s filesystem, it must contain everything needed to run an application - all dependencies, configurations, scripts, binaries, etc. The image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata as shown below.
+ [x] **Installing Docker on Ubuntu**<br/>
+ Uninstall the tech preview or beta version of Docker Desktop for Linux. Run:
  ```powershell
  sudo apt remove docker-desktop
  ```
  Recommended approach to install Docker Desktop on Ubuntu:
  ```powershell
  sudo apt-get update
  sudo apt-get install ./docker-desktop-<version>-<arch>.deb
  docker compose version
  ```
  To start Docker Desktop:
  ```powershell
  systemctl --user start docker-desktop
  ```
+ The image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata as shown     below.
  ```powershell
     version: "3"
     services: 
         api:
            image: twinnerhenock/fastapi
            depends_on:
                - db
            ports:
                - 5000:8000  
            volumes:
                - ./:/usr/src/app
            
            environment:
                DATABASE_HOSTNAME: ${DATABASE_HOSTNAME}
                DATABASE_PORT: ${DATABASE_PORT}
                DATABASE_PASSWORD: ${DATABASE_PASSWORD}
                DATABASE_NAME: ${DATABASE_NAME}
                DATABASE_USERNAME: ${DATABASE_USERNAME}
                SECRET_KEY: ${SECRET_KEY}
                ALGORITHM: ${ALGORITHM}
                ACCESS_TOKEN_EXPIRE_MINUTES: ${ACCESS_TOKEN_EXPIRE_MINUTES}  
         db:   
           image: twinnerhenock/fastapi
           environment:
             POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
             POSTGRES_DB: ${POSTGRES_DB}
  ```

+ [x] **Author**<br/>
   + Henock Yared
   

        
