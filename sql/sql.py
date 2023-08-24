
import mysql.connector

#Connect to the database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Peanutbutter24!',
    database='family'
)

#Create a cursor
cursor = db.cursor()

#Execute the query to retrieve all columns and rows from the table
cursor.execute("SELECT * FROM people")

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

#Close the cursor and connection
cursor.close()
db.close()
