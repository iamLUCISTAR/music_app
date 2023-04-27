
# REST API's - Music App

This application provided the backend services of a music application like searching song, creating playlists, recommending songs to the user and much more. This application was developed using FLASK framework.

## Run Locally

Clone the project

```bash
  https://github.com/iamLUCISTAR/music_app.git
```

Open a terminal and go to the project directory

```bash
  cd music_app
```

Create a virtual environment and activate it and install the required packages using the below commands

```bash
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

Start the development server by running the routes.py file in the src directory, the server starts by default in port 5001. You change the configuration in the routes.py file.

```bash
  python src/routes.py
```
Now the backend services of the music app is ready to accept http requests.

## DB setup
1. The application has database setup using sqlite package.
music_app/db/music.sqlite - This file acts as database for the application and already has data set up for static tables like

- artist
- album
- genre
- song

2. The db/db.py file acts as a initial datamodel file to the tables of the application.
3. db/songs.sql file has the initial data for the static tables.






## Schema design
- Below is the schema design for the music application.

![Screenshot 2023-04-27 at 8 32 20 PM](https://user-images.githubusercontent.com/130143790/234905325-d35a66b8-4286-4474-a752-238e0d540cef.png)

## List of API's
The yaml file can be found in the design/api_docs.yml directory which has the api design documentation. It can be visualised using swagger.io editor.
```bash
  https://editor.swagger.io/
```
![Screenshot 2023-04-27 at 8 44 08 PM](https://user-images.githubusercontent.com/130143790/234907502-a5f604b5-0398-49e3-8c4b-3e2b114617a7.png)
- API for user service
![Screenshot 2023-04-27 at 8 45 37 PM](https://user-images.githubusercontent.com/130143790/234908379-dddbcea9-9e9e-4afb-bf0f-3e2ea3d39c0a.png)
- API for song service
![Screenshot 2023-04-27 at 8 46 17 PM](https://user-images.githubusercontent.com/130143790/234908512-5e12276a-a37c-42c3-b1af-dfe36a49070d.png)
- API for playlist service
![Screenshot 2023-04-27 at 8 46 39 PM](https://user-images.githubusercontent.com/130143790/234908581-36e86b8d-a763-49aa-9bc6-9c4f5b1db2d4.png)
- API for recommendation service
![Screenshot 2023-04-27 at 8 47 11 PM](https://user-images.githubusercontent.com/130143790/234908642-350be864-cde6-4c14-9421-83ced70e303f.png)

## Use cases covered by the api's

1. User - service
- Users can create an account by adding their username, email_id and password, system does not allow same user to create another account using the same email_id.
- Once an user creates an account they can login and logout of the system.
- Session tracking to keep track of user session while he his logged in.

2. Song - service
- Songs are classifed according to the genre, artist and albums.
- User can search any song based on genre, artist, album and title.
- User can rate any song in a scale of 1 to 5.
- Each song has its rating rated by every user by taking the average rating.

3. Playlist - service
- User can create his own playlist with a list of songs or also without songs and add songs later.
- User can add or remove songs from his playlist

4.  Recomendation - service
- User can recommend a particular song/album/artist/genre to the other users using the service.
- System will recommend songs to the user by monitoring the songs in the playlist and user's listening style.
- System will also create playlist on its own based on artist/genre and suggests it to the user.
## Authors

- [@sharathb](https://iamlucistar.github.io/my-personal-website/)

