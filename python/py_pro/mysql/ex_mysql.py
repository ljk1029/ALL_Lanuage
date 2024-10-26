from typing import Tuple
import mysql.connector
import requests



def print_list(l:list):
    for e in l:
        print(e)


class CloudDBOptions:
    posturl = "https://xxx"
    geturl = "https://xxx"

    headers = {
        'appId': 'zTest',
        'appSecret': '123345',
        'Content-Type': 'application/json',
        'Cookie': 'SESSION=f5f94db6-5f76-4493-9a42-a96080a8968e; lix=200; name=xli; sidebarStatus=1'
    }
    
    def post(self, title:str, payload:str):
        response = requests.request("POST", CloudDBOptions.posturl, headers=CloudDBOptions.headers, data=payload)
        print(title+str(response.text))

    
    def get(self, condition:str=""):
        response = requests.request("GET", CloudDBOptions.geturl+condition, headers=CloudDBOptions.headers)
        return response.text



class MySQLOptions:
    def __init__(self, host:str="127.0.0.1", user:str="user1", passwd:str="user1", db:str="mydb") -> None:
        self.dbconn = mysql.connector.connect(host=host, user=user, passwd=passwd, db=db)

    def __del__(self):
        self.dbconn.close()

    def _exec_sql(self, sql:str):
        cursor = self.dbconn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def create_table(self, table:str, columns:dict):
        descstr = ", ".join([f"{column} {datatype}" for column, datatype in columns.items()])
        sql = "create table {} ({})".format(table, descstr)
        print(f"create_table: {sql}")
        print_list(self._exec_sql(sql))
    
    def describe(self, table:str):
        sql = f"desc {table}"
        print(f"describe: {sql}")
        return self._exec_sql(sql)

    def query(self, table:str, fields:list, condition:str = ""):
        key_str = ", ".join(fields)
        sql = "select {} from {} {}".format(key_str, table, f"where {condition}" if condition != "" else "")
        print(f"query statement: {sql}")
        return self._exec_sql(sql)

    def insert(self, table:str, data:Tuple[dict, list]):
        if type(data) is list:
            columns = ", ".join(data[0].keys())
            values = ", ".join(["({})".format(", ".join(d.values())) for d in data])
        elif type(data) is dict:
            columns = ", ".join(data.keys())
            values = "({})".format(", ".join(data.values()))
        sql = "insert into {} ({}) values {}".format(table, columns, values)
        if type(data) is list and len(data) > 100:
            print(f"insert data length: {len(data)}")
        else:
            print(f"insert statement({len(data)}): {sql}")
        print_list(self._exec_sql(sql))
        # 删除和增加操作之后必须执行commit才能生效
        self.dbconn.commit()