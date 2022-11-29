import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    print("\n--DISPLAYING Studio RECORDS--\n")

    cursor = db.cursor()

    # The first query is to select all the fields for the studio table
    cursor.execute("SELECT studio_id, studio_name FROM movies.studio")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID:    {studio[0]}");
        print(f"Studio Name:  {studio[1]}\n");

    # The second query is to select all the fields for the genre table
    cursor.execute("SELECT genre_id, genre_name FROM movies.genre")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Genre ID:    {studio[0]}");
        print(f"Genre Name:  {studio[1]}\n");

    # The third query is to select the movie names for those movies that have a run time of less than two hours.
    cursor.execute("SELECT film_id, film_name FROM movies.film WHERE film_runtime <120")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Film ID:    {studio[0]}");
        print(f"Film Name:  {studio[1]}\n");

    # The fourth query is to get a list of film names, and directors grouped by director.
    cursor.execute("SELECT film_id, film_name, film_director FROM movies.film")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Film ID:        {studio[0]}");
        print(f"Film Name:      {studio[1]}");
        print(f"Film Director:  {studio[2]}\n");

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
