import ibm_db_dbi as dbi
from ibm_db_dbi import SQL_ATTR_DBC_SYS_NAMING, SQL_TRUE
from ibm_db_dbi import SQL_ATTR_TXN_ISOLATION, SQL_TXN_NO_COMMIT
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

options = {
    SQL_ATTR_TXN_ISOLATION: SQL_TXN_NO_COMMIT,
    SQL_ATTR_DBC_SYS_NAMING: SQL_TRUE,
    }
conn = dbi.connect()
conn.set_option(options) 	

cur = conn.cursor()

sql = "INSERT INTO PGFILES.SUPPLIES (supply_brand, supply_type) values(?, ?)"
cur.execute(sql, ("Goodies", "Gummi"))

conn.close()

conn = dbi.connect()
conn.set_option(options) 
cur = conn.cursor()



query = "select * from pgfiles/supplies"
cur.execute(query)

for row in cur:
    print(row[2])

if __name__ == "__main__":
    app.secret_key = 'cutcokey'
    app.config[ 'SESSION_TYPE' ] = 'filesystem'
    app.run(debug=False,host='0.0.0.0',port=9103)