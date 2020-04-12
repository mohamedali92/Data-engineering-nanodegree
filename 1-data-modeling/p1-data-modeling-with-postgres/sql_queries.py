# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays
(
    songplay_id serial primary key,
    start_time timestamp references time(start_time),
    user_id varchar(64) references users(user_id),
    level varchar(10),
    song_id varchar(64) references songs(song_id),
    artist_id varchar(64) references artists(artist_id),
    session_id int not null,
    location  varchar(128),
    user_agent varchar(256) not null 
);
""")

user_table_create = ("""
create table if not exists users
(
    user_id    varchar(64) primary key,
    first_name varchar(64) not null ,
    last_name  varchar(64) not null,
    gender     varchar(1),
    level      varchar(10)
);
""")

song_table_create = ("""
create table if not exists songs
(
    song_id   varchar(64) primary key,
    title     varchar(64) not null,
    artist_id varchar(64) references artists(artist_id),
    year      int,
    duration  float4 not null
);
""")

artist_table_create = ("""
create table if not exists artists
(
    artist_id varchar(64) primary key,
    name      varchar(128) not null,
    location  varchar(128),
    latitude  float4,
    longitude float4
);
""")

time_table_create = ("""
create table if not exists time
(
    start_time timestamp primary key,
    hour       int,
    day        int,
    week       int,
    month      int,
    year       int,
    weekday    int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
insert into songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
values (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
insert into users (user_id, first_name, last_name, gender, level) 
values (%s, %s, %s, %s, %s)
on conflict (user_id) do update set level = excluded.level;
""")

song_table_insert = ("""
insert into songs (song_id, title, artist_id, year, duration)
values (%s, %s, %s, %s, %s)
on conflict (song_id) do nothing;
""")

artist_table_insert = ("""
insert into artists (artist_id, name, location, latitude, longitude)
values (%s, %s, %s, %s, %s)
on conflict (artist_id) do nothing;
""")


time_table_insert = ("""
insert into time (start_time, hour, day, week, month, year, weekday)
values (%s, %s, %s, %s, %s, %s, %s)
on conflict (start_time) do nothing;
""")

# FIND SONGS

song_select = ("""
select s.song_id,
       a.artist_id
from songs s
         join artists a on s.artist_id = a.artist_id
where s.title = %s
  and a.name = %s
  and s.duration = %s;
""")

# QUERY LISTS

create_table_queries = (songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create)

create_table_queries = (user_table_create,  artist_table_create, time_table_create, song_table_create, songplay_table_create)
drop_table_queries = (user_table_drop,  artist_table_drop, time_table_drop, song_table_drop, songplay_table_drop)