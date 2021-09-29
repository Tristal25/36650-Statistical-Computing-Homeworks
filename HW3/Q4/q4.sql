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