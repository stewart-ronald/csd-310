import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}
# initialize ref function
def show_films(mycursor, title):

    mycursor.execute("SELECT film_name as 'Film Name', film_director as Director, genre_name as Genre, studio_name as "
                     "'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON "
                     "film.studio_id=studio.studio_id")
    films = mycursor.fetchall()
    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2],
                                                                                         film[3]))


def insert_film(mycursor):
    # insert Black Phone, 2021, 102, Scott Derrickson, 2, 1 into film in movies
    mycursor.execute("INSERT INTO movies.film (film_name, film_releaseDate, film_runtime, film_director, studio_id, "
                     "genre_id) VALUES ('Black Phone', '2021', 102, 'Scott Derrickson', 2, 1)")

    show_films(mycursor, "DISPLAYING FILMS AFTER INSERT")


def update_film(mycursor):
    # change 'Alien' genre to 'Horror'
    mycursor.execute("UPDATE film set genre_id=1 where film_name='Alien'")
    show_films(mycursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")


def delete_film(mycursor):
    # delete Gladitor
    mycursor.execute("DELETE from film WHERE film_name='Gladiator'")
    show_films(mycursor, "DISPLAYING FILMS AFTER DELETE")

try:
    db = mysql.connector.connect(**config)
    mycursor = db.cursor()
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press [Enter] to continue...")
    show_films(mycursor, "DISPLAYING FILMS")
    insert_film(mycursor)
    update_film(mycursor)
    delete_film(mycursor)
    db.commit()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    db.close()

show_films(cursor, "--DISPLAYING FILMS AFTER INSERT--")

update_film = "UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'"

cursor.execute(update_film)

show_films(cursor, "--DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror--")

delete_film = "DELETE FROM film WHERE film_name = 'Gladiator'"

cursor.execute(delete_film)

show_films(cursor, "--DISPLAYING FILMS AFTER DELETE--")

db.close()
