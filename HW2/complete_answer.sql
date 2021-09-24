# Q1
Create table rdata (
id Serial Primary Key, 
a varchar(5), 
b varchar(5), 
moment date, 
x numeric(5, 2)
);

# Q2

drop table rdata;

Create table rdata (
id Serial Primary Key, 
a varchar(5) unique not NULL, 
b varchar(5) unique not NULL, 
moment date default '2021-01-01', 
x numeric(5, 2) check (x > 0)
);

# Q4

Insert into rdata (a, b, x) values
('abcde', 'fghij', 111.11), 
('klmno', 'pqrst', 222.22), 
('uvwxy', 'z', 333.33);

select * from rdata;

#Q5

Insert into rdata (a, b, x) values
('a', 'b', -111.11);

Insert into rdata (a, b, x) values
('a', 'b', 111.11);

# Q6

Update rdata
set moment = '2020-03-15'
where id = 1 or id = 2;

# Q7

alter table rdata
add column y boolean default false;

# Q8

delete from rdata
where id = 1 or id = 2;

# Q9

alter table rdata 
rename column moment to date;









