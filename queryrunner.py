import os
import mysql.connector
class MYSQLDB:
    def __init__(self,server:str,port:int,username:str,password:str) -> None:
        self.db=mysql.connector.connect(host=server,port=port,username=username,password=password)
        self.cursor=self.db.cursor()
    def getDatabases(self):
        dbs=[]
        self.cursor.execute("Show DATABASES")
        for db in self.cursor:
            dbs.append(db)
        return dbs
    def getLocalErrors(self):
        with open('/var/log/mysql/error.log','r') as f:
            errors=f.readlines()
            return errors
    def getCurrentConnections(self):
        result=[]
        self.cursor.execute('select count(host) from information_schema.processlist')
        for item in self.cursor:
            result.append(item)
        return result

class Query(MYSQLDB):
    def __init__(self,query:str) -> None:
        self.query=query
        self.hsql=hash(query)
        self.result=None
    def run(self):
        self.cursor.execute(self.query)
    
