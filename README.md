# start Airflow
Get inside the projects folder and run 
`echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env`
then
`docker-compose up --build`

by default the weberver will start at 
`http://0.0.0.0:8080`

the default admin credentials are:
`user : airflow
password : airflow`


# cleanup
use `ctrl+c` to stop the server.
To stop and delete containers, delete volumes with database data and download images, run:
`docker-compose down --volumes --rmi all` 