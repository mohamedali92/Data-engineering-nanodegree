# Data Modeling with Cassandra
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.
They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

The goal of the project is to model data using Apache Cassandra and complete an ETL pipeline using Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Docker
- Python3
- virtualenv package

### Installing

- Create and activate a new Python3 virtualenv. This allows us to use local isolated python interpreter without polluting the global interpreter with many packages.

        virtualenv -p python3 p2-data-modeling-with-apache-cassandra
        source p2-data-modeling-with-apache-cassandra/bin/activate
- Install the necessary packages. These packages are used in the various python scripts below and in the jupyter notebooks.
        
        pip install -r requirements.txt

- Setup a local cassandra docker container using the provided script, this is to create an isolated environment for the project without polluting the host system

        . ./setup_cassandra_using_docker.sh
        
   or 
   
        . ./setup_cassandra_using_docker.sh DEFAULTPASSWORD
        
- Use the provided `cassandra-secrets-template.yaml` and update the username and password to provide the authentication details to access the local cassandra instance. 
 Then rename the file by removing the `-template` since thats the name the jupyter notebook is using:

        mv cassandra-secrets-template.yaml  cassandra-secrets.yaml

- Run the Project_1B_Project_Template notebook to process the raw data, model it and insert & query it using Cassandra