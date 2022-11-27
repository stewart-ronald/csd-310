import mysql.connector

mydb = mysql.connector.connect(
    user='movies_user',
    password='popcorn',
    host='127.0.0.1',
    database='movies',
    raise_on_warnings=True
)
mycursor = mydb.cursor()

# displaying all studio fields
mycursor.execute("SELECT * FROM studio")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
# displaying all genre fields
mycursor.execute("SELECT * FROM genre")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# displaying films less than 2 hours
mycursor.execute("SELECT film_name FROM film WHERE film_runtime < 120")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# displaying film names and directors grouped by director
mycursor.execute("SELECT film_name, film_director FROM film GROUP BY film_director, film_name")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
