
# Project Description


# Setup Instructions

- Setup Postgres locally by running the bash script

    `. ./setup_postgres_using_docker.sh SUPERUSERPASSWORD`

Note that if you rerun the script and need to change the password you need to rm the postgres directory on the host machine. 
Otherwise when you create a new container using the old mount it will use the old password. The script will also create the deafult db.

- Connect to your local Postgres and create the student users and grant it permission to create dbs

         create user student with password 'student';
         grant all privileges on database "studentdb" to student;
         alter user student createdb;

- Create and activate a new Python3 virtualenv

        virtualenv -p python3 p1-data-modeling-with-postgres
        source p1-data-modeling-with-postgres/bin/activate
- Install the necessary packages
        
        pip install -r requirements.txt
- Run the `create_tables` script

        python create_tables.py

- Verify by running the `test.ipynb` notebook that tables were created successfully