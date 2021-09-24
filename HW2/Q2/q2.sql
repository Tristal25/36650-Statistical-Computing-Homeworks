Drop table rdata;

Create table rdata (
id Serial Primary Key, 
a varchar(5) unique not NULL, 
b varchar(5) unique not NULL, 
moment date default '2021-01-01', 
x numeric(5, 2) check (x > 0)
);
