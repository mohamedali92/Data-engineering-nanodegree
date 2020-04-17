
# Project Description
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

# Setup Instructions

- Setup Postgres locally by running the bash script. This leverages Docker to make the setup as reproducible as possible

    `. ./setup_postgres_using_docker.sh SUPERUSERPASSWORD`

Note that if you rerun the script and need to change the password you need to rm the postgres directory on the host machine. 
Otherwise when you create a new container using the old mount it will use the old password. The script will also create the deafult db.

- Connect to your local Postgres and create the student user and grant it permission to create dbs

         create user student with password 'student';
         grant all privileges on database "studentdb" to student;
         alter user student createdb;

- Create and activate a new Python3 virtualenv. This allows us to use local isolated python interpreter without polluting the global interpreter with many packages.

        virtualenv -p python3 p1-data-modeling-with-postgres
        source p1-data-modeling-with-postgres/bin/activate
- Install the necessary packages. These packages are using in the various python scripts below and in the jupyter notebooks.
        
        pip install -r requirements.txt
- Run the `create_tables` script which acts like a database migration to drop/create the database and drop/create the necessary tables

        python create_tables.py

- Verify by running the `test.ipynb` notebook that tables were created successfully, this notebook simply selects 5 records from each table to verify data was added successfully

- Run the `etl.py` script to run the etl and populate the tables. The script will load the raw data into pandas dataframes, filter, remove duplicates and inser the data into postgres tables:

        python etl.py
        
# Schema
This project uses a traditional star schema to represent the data. 
`songplays` are the facts surrounded by various entites that project in depth information about each song play.

![schema](https://github.com/mohamedali92/data-engineering-nanodegree/blob/master/1-data-modeling/p1-data-modeling-with-postgres/star-schema.png)   


### Potential Future additions
- [ ] Build a GraphQl engine on top of the data in postgres using ![Hasura](https://hasura.io/) 
- [ ] Build an analytics dashboard using ![Superset](https://superset.apache.org/) 