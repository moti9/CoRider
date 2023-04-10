# Flask CRUD API


## Prerequisites 
***
- Python 3.x
- Git

## Clone the repository
***

<p> Clone the repository using the following command:</p>

```bash
$ git clone https://github.com/moti9/CoRider
```


## Create a virtual environment
***
- It is recommended to use a virtual environment to keep the project dependencies separate from other Python projects on your machine. 
- To create a virtual environment, follow these steps:

1. Navigate to the project directory:  
```bash
$ cd <project-name>
```
2. Create a virtual environment:
```bash
$ python3 -m venv <name-env>
or
$ virtualenv <name-env>
```
3. Activate the virtual environment:

    - On macOS/Linux:  `$ source venv/bin/activate`

    - On Windows: `$ venv\Scripts\activate.bat`
    <br/>
    `$ .\<name-env>\Scripts\activate`

## Install dependencies
***
Once you have activated the virtual environment, install the project dependencies using the following command:
```bash
$ pip install -r requirements.txt
```
This will install all the required packages listed in the requirements.txt file.

## Run the project
***
After you have installed the dependencies, you can run the project using the following command:
```bash
$ python app.py 
```

***
### Make sure that you have already installed mongoDB and completed the setup
```bash
# Connect to the database

client = MongoClient('mongodb://localhost:27017')
db = client['corider']
collection = db['users']
```
***