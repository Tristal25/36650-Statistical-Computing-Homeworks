Select * from more_player_stats;
Select * from player_bios;
Select * from player_stats;

# Q2

Select count(distinct college) as colleges from player_bios;

# Q3

drop table teams;
drop type DivisionType;
drop type ConferenceType;

Create type DivisionType as ENUM ('Atlantic', 'Central', 'Southeast', 'Northwest', 'Pacific', 'Southwest');
Create type ConferenceType as ENUM ('Eastern', 'Western');

Create table teams (
	id char(3) primary key, 
	location text, 
	name text, 
	division DivisionType, 
	conference ConferenceType
);


Insert into teams VALUES
('BOS', 'Boston', 'Celtics', 'Atlantic', 'Eastern'),
('BKN', 'Brooklyn', 'Nets', 'Atlantic', 'Eastern'),
('NYK', 'New York', 'Knicks', 'Atlantic', 'Eastern'),
('PHI', 'Philadelphia', '76ers', 'Atlantic', 'Eastern'),
('TOR', 'Toronto', 'Raptors', 'Atlantic', 'Eastern'),
('CHI', 'Chicago', 'Bulls', 'Central', 'Eastern'),
('CLE', 'Cleveland', 'Cavaliers', 'Central', 'Eastern'),
('DET', 'Detroit', 'Pistons', 'Central', 'Eastern'),
('IND', 'Indiana', 'Pacers', 'Central', 'Eastern'),
('MIL', 'Milwaukee', 'Bucks', 'Central', 'Eastern'),
('ATL', 'Atlanta', 'Hawks', 'Southeast', 'Eastern'),
('CHA', 'Charlotte', 'Bobcats', 'Southeast', 'Eastern'),
('MIA', 'Miami', 'Heat', 'Southeast', 'Eastern'),
('ORL', 'Orlando', 'Magic', 'Southeast', 'Eastern'),
('WAS', 'Washington', 'Wizards', 'Southeast','Eastern'),
('DEN', 'Denver', 'Nuggets', 'Northwest', 'Western'),
('MIN', 'Minnesota', 'Timberwolves', 'Northwest', 'Western'),
('OKC', 'Oklahoma City', 'Thunder', 'Northwest', 'Western'),
('POR', 'Portland', 'Trail Blazers', 'Northwest', 'Western'),
('UTA', 'Utah', 'Jazz', 'Northwest', 'Western'),
('GSW', 'Golden State', 'Warriors', 'Pacific', 'Western'),
('LAC', 'Los Angeles', 'Clippers', 'Pacific', 'Western'),
('LAL', 'Los Angeles', 'Lakers', 'Pacific', 'Western'),
('PHX', 'Phoenix', 'Suns', 'Pacific', 'Western'),
('SAC', 'Sacramento', 'Kings', 'Pacific', 'Western'),
('DAL', 'Dallas', 'Mavericks', 'Southwest', 'Western'),
('HOU', 'Houston', 'Rockets', 'Southwest', 'Western'),
('MEM', 'Memphis', 'Grizzlies', 'Southwest', 'Western'),
('NOP', 'New Orleans', 'Hornets', 'Southwest', 'Western'),
('SAS', 'San Antonio', 'Spurs', 'Southwest', 'Western');


# Q4

drop table new_table;

## Alternative

create table new_table (
	player integer references more_player_stats (id), 
	prl numeric, 
	position text
);

Insert into new_table (prl, position)
(select (per - 67 * va/(gp * minutes)) as prl, 
 case when (per - 67 * va/(gp * minutes)) >= 11.3 then 'PF'
 	when (per - 67 * va/(gp * minutes)) >= 10.8 then 'PG'
 	when (per - 67 * va/(gp * minutes)) >= 10.6 then 'C'
 	else 'SG/SF' end as position from more_player_stats);

## Answer

create table new_table (
	player integer references more_player_stats, 
	prl numeric, 
	position text
);

Insert into new_table (player, prl)
(select id, (per - 67 * va/(gp * minutes)) as prl 
from more_player_stats);

update new_table set position = 'PF' where prl >= 11.3;
update new_table set position = 'PG' where prl >= 10.8 and prl < 11.3;
update new_table set position = 'C' where prl >= 10.6 and prl < 10.8;
update new_table set position = 'SG/SF' where prl < 10.6 and prl >= 0;


Select * from new_table;

# Q5

alter table player_bios
add column position text;

update player_bios set position = 'PF' where id in (select player from new_table where position = 'PF');
update player_bios set position = 'PG' where id in (select player from new_table where position = 'PG');
update player_bios set position = 'C' where id in (select player from new_table where position = 'C');
update player_bios set position = 'SG/SF' where id in (select player from new_table where position = 'SG/SF');

select firstname, lastname, position from player_bios;

# Q6

alter table player_bios
add column inches numeric;

update player_bios
set inches = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

alter table player_bios
drop column height;

alter table player_bios
rename column inches to height;

select firstname, lastname, height from player_bios;







