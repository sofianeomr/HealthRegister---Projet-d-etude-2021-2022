import mysql.connector

class SQLConnection :
    """ Fournit un accès à la BD """
    mydb = None

    @classmethod
    def getSQLConnection(cls):
        if cls.mydb != None:
            return cls.mydb
        try:
            cls.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="health_register"
            )
        except Exception as ex:
            print(ex)
        return cls.mydb