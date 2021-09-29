alter table player_bios
add column position text;

update player_bios set position = 'PF' where id in (select player from new_table where position = 'PF');
update player_bios set position = 'PG' where id in (select player from new_table where position = 'PG');
update player_bios set position = 'C' where id in (select player from new_table where position = 'C');
update player_bios set position = 'SG/SF' where id in (select player from new_table where position = 'SG/SF');

select firstname, lastname, position from player_bios;
