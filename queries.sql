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

create table if not exists loans (
    loan_id int unsigned primary key auto_increment,
    date_due date not null,
    date_returned date not null,
    copy_id int unsigned not null,
    foreign key (copy_id) references copies (copy_id),
    member_id int unsigned not null,
    foreign key (member_id) references members (member_id)

)engine=InnoDB;