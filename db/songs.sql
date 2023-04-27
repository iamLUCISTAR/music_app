--static tables admin access only

insert into genre (genre_name) values ('pop');
insert into genre (genre_name) values ('melody');
insert into genre (genre_name) values ('rap');
insert into genre (genre_name) values ('jazz');
insert into genre (genre_name) values ('rock');

insert into artist (artist_name) values ('yuvan shankar raja');
insert into artist (artist_name) values ('harris jayaraj');
insert into artist (artist_name) values ('ar rahman');
insert into artist (artist_name) values ('gv prakash');
insert into artist (artist_name) values ('santhosh narayanan');
insert into artist (artist_name) values ('justin bieber');
insert into artist (artist_name) values ('selena gomez');
insert into artist (artist_name) values ('katty perry');
insert into artist (artist_name) values ('maroon 5');
insert into artist (artist_name) values ('the weeknd');

insert into album (album_name, artist_id) values ('vallavan', 1)
insert into album (album_name, artist_id) values ('sarvam', 1)
insert into album (album_name, artist_id) values ('love today', 1)
insert into album (album_name, artist_id) values ('goa', 1)
insert into album (album_name, artist_id) values ('mankatha', 1)
insert into album (album_name, artist_id) values ('varanam aayiram', 2)
insert into album (album_name, artist_id) values ('anniyan', 2)
insert into album (album_name, artist_id) values ('lesa lesa', 2)
insert into album (album_name, artist_id) values ('nanban', 2)
insert into album (album_name, artist_id) values ('kadhal desam', 3)
insert into album (album_name, artist_id) values ('vtv', 3)
insert into album (album_name, artist_id) values ('bombay', 3)
insert into album (album_name, artist_id) values ('jeans', 3)
insert into album (album_name, artist_id) values ('bigil', 3)
insert into album (album_name, artist_id) values ('bachelor', 4)
insert into album (album_name, artist_id) values ('madarasapatinam', 4)
insert into album (album_name, artist_id) values ('aadukalam', 4)
insert into album (album_name, artist_id) values ('soorarai potru', 4)
insert into album (album_name, artist_id) values ('asuran', 4)
insert into album (album_name, artist_id) values ('kakakapo', 4)
insert into album (album_name, artist_id) values ('pizza', 4)
insert into album (album_name, artist_id) values ('karnan', 4)
insert into album (album_name, artist_id) values ('madras', 4)
insert into album (album_name, artist_id) values ('irudhi sutru', 4)


--yuvan
insert into song (song_name,artist_id,album_id,genre_id) values ('loose penne',1,1,1);
insert into song (song_name,artist_id,album_id,genre_id) values ('siragugal',1,2,2);
insert into song (song_name,artist_id,album_id,genre_id) values ('mamakutty',1,3,3);
insert into song (song_name,artist_id,album_id,genre_id) values ('idhu varai',1,4,4);
insert into song (song_name,artist_id,album_id,genre_id) values ('mankatha theme',1,5,5);
--harris
insert into song (song_name,artist_id,album_id,genre_id) values ('yethi',2,6,1);
insert into song (song_name,artist_id,album_id,genre_id) values ('mundhinam',2,6,2);
insert into song (song_name,artist_id,album_id,genre_id) values ('kadhal yaanai',2,7,3);
insert into song (song_name,artist_id,album_id,genre_id) values ('love pannu',2,8,4);
insert into song (song_name,artist_id,album_id,genre_id) values ('all is well',2,9,5);
--ar
insert into song (song_name,artist_id,album_id,genre_id) values ('mustafa',3,10,1);
insert into song (song_name,artist_id,album_id,genre_id) values ('manipaya',3,11,2);
insert into song (song_name,artist_id,album_id,genre_id) values ('humma',3,12,3);
insert into song (song_name,artist_id,album_id,genre_id) values ('columbus',3,13,4);
insert into song (song_name,artist_id,album_id,genre_id) values ('verithanam',3,14,5);
--gvp
insert into song (song_name,artist_id,album_id,genre_id) values ('adiye',4,15,1);
insert into song (song_name,artist_id,album_id,genre_id) values ('pookal pookum',4,16,2);
insert into song (song_name,artist_id,album_id,genre_id) values ('porkalam',4,17,3);
insert into song (song_name,artist_id,album_id,genre_id) values ('veiyon silli',4,18,4);
insert into song (song_name,artist_id,album_id,genre_id) values ('asura',4,19,5);
--sana
insert into song (song_name,artist_id,album_id,genre_id) values ('akkam pakkam paar',5,20,1);
insert into song (song_name,artist_id,album_id,genre_id) values ('mogathirai',5,21,2);
insert into song (song_name,artist_id,album_id,genre_id) values ('kandha vara solunga',5,22,3);
insert into song (song_name,artist_id,album_id,genre_id) values ('aagayam theepidicha',5,23,4);
insert into song (song_name,artist_id,album_id,genre_id) values ('hey sandakaara',5,24,5);
--justin
insert into song (song_name,artist_id,album_id,genre_id) values ('baby',6,null,1);
insert into song (song_name,artist_id,album_id,genre_id) values ('let me love you',6,null,2);
--selena
insert into song (song_name,artist_id,album_id,genre_id) values ('fetish',7,null,1);
insert into song (song_name,artist_id,album_id,genre_id) values ('a year without rain',7,null,2);
--katty
insert into song (song_name,artist_id,album_id,genre_id) values ('roar',8,null,1);
insert into song (song_name,artist_id,album_id,genre_id) values ('love me like you do',8,null,2);
--maroon
insert into song (song_name,artist_id,album_id,genre_id) values ('girls like you',9,null,3);
insert into song (song_name,artist_id,album_id,genre_id) values ('memories',9,null,4);
--weeknd
insert into song (song_name,artist_id,album_id,genre_id) values ('starboy',10,null,4);
insert into song (song_name,artist_id,album_id,genre_id) values ('heartless',10,null,1);
