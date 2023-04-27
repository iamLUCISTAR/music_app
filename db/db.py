import sqlite3

db_con = sqlite3.connect("music.sqlite")

cursor = db_con.cursor()

genre_query = """create table genre
                 (genre_id integer primary key autoincrement,
                  genre_name varchar)"""

artist_query = """create table artist
                  (artist_id integer primary key autoincrement,
                   artist_name varchar)"""

album_query = """create table album
                 (album_id integer primary key autoincrement,
                  album_name varchar,
                  artist_id integer,
                  constraint artist_id_fk foreign key (artist_id) references artist(artist_id))"""

query = """ create table user 
            (user_id integer primary key autoincrement,
             user_name varchar,
             email_id varchar,
             password varchar,
             )"""

query2 = """ create table song
             (song_id integer primary key autoincrement,
              song_name varchar,
              artist_id int,
              album_id int,
              genre_id int,
              constraint artist_id_fk foreign key (artist_id) references artist(artist_id),
              constraint album_id_fk foreign key (album_id) references album(album_id),
              constraint genre_id_fk foreign key (genre_id) references genre(genre_id))"""

query3 = """create table playlist
            (playlist_id integer primary key autoincrement,
             playlist_name varchar,
             user_id integer,
             constraint user_id_fk
             foreign key (user_id)
             references user(user_id))
            """
query4 = """create table playlist_song
            (playlist_song_id integer primary key autoincrement,
             song_id integer,
             playlist_id integer,
             constraint song_id_fk foreign key (song_id) references song(song_id),
             constraint playlist_id_fk foreign key (playlist_id) references playlist(playlist_id))
            """

query5 = """create table song_rating
            (rating_id integer primary key autoincrement,
             song_id integer,
             user_id integer,
             rating integer,
             constraint song_id_fk foreign key (song_id) references song(song_id),
             constraint user_id_fk foreign key (user_id) references user(user_id))        
         """

query6 = """create table recommendation
            (recommendation_id integer primary key autoincrement,
             entity varchar,
             entity_id integer,
             by_user_id integer,
             to_user_id integer,
             constraint from_user_fk foreign key (by_user_id) references user(user_id),
             constraint to_user_fk foreign key (to_user_id) references user(user_id))"""


# cursor.execute(genre_query)
# cursor.execute(artist_query)
# cursor.execute(album_query)
# cursor.execute(query)
# cursor.execute(query2)
# cursor.execute(query3)
# cursor.execute(query4)
# cursor.execute(query5)
cursor.execute(query6)