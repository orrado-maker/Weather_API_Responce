import open_ui
import mysql.connector


def save_data():


    db = mysql.connector.connect(
        id=open_ui.submitted_data["ID"],
        Latti=open_ui.submitted_data["Latitude 1"],
        Longitude=open_ui.submitted_data["Longitude 1"],
        Temp= 22 #placeholder for temp data from api request#
        database="userPrefDB"
    )

    cursor = db.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    values = ("John", "Highway 21")

    cursor.execute(sql, values)
    db.commit()

    print(cursor.rowcount, "record inserted.")
