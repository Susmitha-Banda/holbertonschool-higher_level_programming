# holbertonschool-higher_level_programming

My SQL

### SQL Server
Any of these will be needed to start SQL server.
1) Using docker image.
2) Using VS code plugin.

#### In our case, we will go with Option 1 i.e docker image

#

### How to Run any application using docker image?

1) `docker pull <imagename>`  -->  `docker pull mysql`
2) check if the image is pulled --> `docker images`
3) Run the image to start the container -> `docker run <imageTag>`

``` 
docker run  -e MYSQL_ROOT_PASSWORD=pwd -d -p 3306:3306 mysql
```


#

### SQL Client
It's a workspace to write the queries.
1) DBeaver (supports all databases)
2) SQL developer (mostly used for Oracle DB)
3) SQL Server Management Studio ( mostly used for Microsoft SQL)
4) Shell Terminal.

#### In our case, we will use DBeaver as it's mostly widely used.

#

### Issue faced

``` 
Modify DBeaver Connection Settings
Open DBeaver.

Edit your MySQL connection:

Navigate to the Database Navigator.
Right-click your MySQL connection and select Edit Connection.
Adjust the connection settings:

Click on the Driver Properties tab.

Add a new property:

Property Name: allowPublicKeyRetrieval
Value: true
```