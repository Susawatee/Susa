import mysql.connector

def conDB():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="longtest"
        )
        return mydb
class Con:
    def gethard_ware4():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware4 "
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data


    def inserthard_ware4(name, hw_name):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hard_ware4 (name, hw_name, status, value) VALUES ('{}', '{}', 'OFF', '0')".format(
            name, hw_name
        )
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID

    def gethard_ware4_ID(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware4 WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def updatehard_ware4(ID, value):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hard_ware4 SET value = '{}' WHERE id = {}".format(value, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

    def deletehard_ware4():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hard_ware4 WHERE id = 4"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

    def selecthard_ware4(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware4 WHERE ID = '{}'".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return True