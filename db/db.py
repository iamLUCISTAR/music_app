import sqlite3

db_con = sqlite3.connect("music.sqlite")

cursor = db_con.cursor()

create_genre = """create table genre
                 (genre_id integer primary key autoincrement,
                  genre_name varchar not null
                  )"""

create_artist = """create table artist
                  (artist_id integer primary key autoincrement,
                   artist_name varchar not null)
                   """
artist_index = "create index artist_name_idx on artist (artist_name)"

create_album = """create table album
                 (album_id integer primary key autoincrement,
                  album_name varchar not null,
                  artist_id integer,
                  constraint artist_id_fk foreign key (artist_id) references artist(artist_id))"""
album_index = "create index album_name_idx on album (album_name)"

create_user = """ create table user 
                  (user_id integer primary key autoincrement,
                   user_name varchar,
                   email_id varchar,
                   password varchar,
                   created_datetime datetime
                   )"""
user_index = "create index user_name_idx on user (user_name)"

create_song = """ create table song
                  (song_id integer primary key autoincrement,
                  song_name varchar not null,
                  artist_id int not null,
                  album_id int,
                  genre_id int not null,
                  constraint artist_id_fk foreign key (artist_id) references artist(artist_id),
                  constraint album_id_fk foreign key (album_id) references album(album_id),
                  constraint genre_id_fk foreign key (genre_id) references genre(genre_id))"""
song_index = "create index song_name_idx on song (song_name)"

create_playlist = """create table playlist
                    (playlist_id integer primary key autoincrement,
                     playlist_name varchar not null,
                     user_id integer not null,
                     constraint user_id_fk foreign key (user_id) references user(user_id)
                     )
                   """
playlist_index = "create index playlist_name_idx on playlist (playlist_name)"

create_playlist_song = """create table playlist_song
                         (playlist_song_id integer primary key autoincrement,
                          song_id integer not null,
                          playlist_id integer not null,
                          constraint song_id_fk foreign key (song_id) references song(song_id),
                          constraint playlist_id_fk foreign key (playlist_id) references playlist(playlist_id))
                       """

create_song_rating = """create table song_rating
                        (rating_id integer primary key autoincrement,
                         song_id integer not null,
                         user_id integer not null,
                         rating integer not null,
                         constraint song_id_fk foreign key (song_id) references song(song_id),
                         constraint user_id_fk foreign key (user_id) references user(user_id))        
                     """

create_recommendation = """create table recommendation
                           (recommendation_id integer primary key autoincrement,
                            entity_type varchar not null,
                            entity_id integer not null,
                            by_user_id integer not null,
                            to_user_id integer not null,
                            constraint from_user_fk foreign key (by_user_id) references user(user_id),
                            constraint to_user_fk foreign key (to_user_id) references user(user_id))"""
recommendation_index = "create index entity_idx on recommendation (entity_type)"

cursor.execute(create_genre)
cursor.execute(create_artist)
cursor.execute(create_album)
cursor.execute(create_user)
cursor.execute(create_song)
cursor.execute(create_playlist)
cursor.execute(create_playlist_song)
cursor.execute(create_song_rating)
cursor.execute(create_recommendation)
cursor.execute(artist_index)
cursor.execute(album_index)
cursor.execute(song_index)
cursor.execute(user_index)
cursor.execute(playlist_index)
cursor.execute(recommendation_index)
