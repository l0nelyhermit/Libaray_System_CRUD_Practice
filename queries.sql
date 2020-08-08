-- /* Login*/
-- mysql -u root

-- /* Show all databases*/
-- show databases;

-- /* to create a new database */
-- create database <database-name>;

-- /* to switch to an exisiting database */
-- use <database-name>;

-- /* to see tables in a database */
-- show tables;

create table if not exists vets (
    vet_id int auto_increment primary key,
    fname varchar(100),
    lname varchar(100)
)engine = innodb;