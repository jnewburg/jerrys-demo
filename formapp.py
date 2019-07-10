import ibm_db_dbi as dbi
from ibm_db_dbi import SQL_ATTR_DBC_SYS_NAMING, SQL_TRUE
from ibm_db_dbi import SQL_ATTR_TXN_ISOLATION, SQL_TXN_NO_COMMIT
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

options = {
    SQL_ATTR_TXN_ISOLATION: SQL_TXN_NO_COMMIT,
    SQL_ATTR_DBC_SYS_NAMING: SQL_TRUE,
    }
#conn = dbi.connect()
#conn.set_option(options) 	

#cur = conn.cursor()

#query = "select * from pgfiles/supplies"
#cur.execute(query)

#for row in cur:
#    print(row[2])

@app.route ( '/login' , methods =[ 'GET' , 'POST' ])
def login():
    if request.method == 'POST' :
        username = request.form[ 'username' ]
        password = request.form[ 'password' ]
        session ['user'] = username
        return redirect( "/" )
    else :
        return render_template( 'login.html' )

@app.route ( '/logout' )
def logout():
    session.pop('user', None)
    session.clear()
    return redirect( '/login' )

@app.route("/")
def formAddSupply():
    if not 'user' in session:
        return redirect( "/login" )
    else:
        return render_template('formAddSupply.html')
        
@app.route('/addSupply',methods=['POST'])
def add_supply():
    errors = {}
    # read the posted values from the UI
    supply_name = request.form['supply_name']
    supply_brand = request.form['supply_brand']
    supply_date = request.form['supply_date']
    #return 'Name: ' + supply_name + ' Brand: ' + supply_brand
    if supply_name == '':
        errors['supply_name'] = 'Please enter a value for supply name'
    if supply_brand	== '':
        errors['supply_brand'] = 'Please enter a value for brand'
    if not errors:
        return 'Name: ' + supply_name + ' Brand: ' + supply_brand
        conn = dbi.connect()
        conn.set_option(options) 	

        cur = conn.cursor()

        sql = "INSERT INTO PGFILES.SUPPLIES (supply_brand, supply_type) values(?, ?)"
        cur.execute(sql, (supply_name, supply_name))
    else:
        return render_template('formAddSupply.html', errors=errors)

if __name__ == "__main__":
    app.secret_key = 'cutcokey'
    app.config[ 'SESSION_TYPE' ] = 'filesystem'
    app.run(debug=False,host='0.0.0.0',port=9103)