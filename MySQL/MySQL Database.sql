CREATE DATABASE testDB; -- cerate database databasename

SHOW DATABASES; -- using this query we can show all the databases

DROP DATABASE testDB; -- sung this query we can delete the database schema

USE testDB; -- using this query we can use the database according to our preference

CREATE TABLE Persons (      -- this query we can used to create the blank table
    PersonID int PRIMARY KEY NOT NULL,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

SELECT * FROM Persons;  -- we can select all the columns and data from the table

CREATE TABLE TestTable AS  -- we can create another table from existing table
SELECT PersonID, FirstName, LastName
FROM Persons; 

SELECT * FROM TestTable;

DROP TABLE TestTable; -- we can drop the exisiting table from the database

TRUNCATE TABLE TestTable; -- this query delete all the content of the table, but not the table itself

ALTER TABLE TestTable  -- we can add the column name using this query
ADD City varchar(255); 

ALTER TABLE TestTable -- we can delete the column name using this query
DROP COLUMN City;

ALTER TABLE TestTable -- we can change the datatype of the column using this query
MODIFY COLUMN City INT;

ALTER TABLE Persons -- we can add the column name using this query
ADD DateOfBirth date; -- here date is the datatype

ALTER TABLE Persons
MODIFY COLUMN DateOfBirth year;  /* The "DateOfBirth" column is now of 
type year and is going to hold a year in a two- or four-digit format. */

















