import mysql.connector

def conDB():
        mydb = mysql.connector.connect(
            host="localhost",
            user="longtest",
            password="171145",
            database="longtest"
        )
        return mydb

class Con:
    def gethard_ware(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware WHERE ID = '{}'".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data


    def inserthard_ware(name,hw_name):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hard_ware (name,hw_name,status,value) VALUES('{}','{}','ON','10')".format(name,hw_name)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID

    def updatehard_ware(ID, status):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hard_ware SET status = '{}' WHERE id = {}".format(status, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True


    def deletehard_ware():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hard_ware WHERE id = 4"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

    def selecthard_ware(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware WHERE ID = '{}'".format(ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

