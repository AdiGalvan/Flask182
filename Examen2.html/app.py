from flask import Flask, render_template,request, redirect,url_for,flash# render_template es la biblioteca/funcion que genera la vista para que se pueda ver
from flask_mysqldb import MySQL

app= Flask(__name__) #declaracion o inicializacion del servidor flask, se declara una variable app 


app.config['MYSQL_HOST']= "localhost" 
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""  
app.config['MYSQL_DB']= "DB_Floreria" 

app.secret_key='mysecretkey'

mysql= MySQL(app)


@app.route('/')
def ingresar():
   curSelect= mysql.connection.cursor()
   curSelect.execute('select * from tbflores')
   consulta= curSelect.fetchall() 

   return render_template('ingresar.html' )



@app.route('/registrar',methods=['POST'])
def registrar():
    if request.method == 'POST':
        Vnombre= request.form['txtNombre']
        Vcantidad= request.form['txtCantidad']
        Vprecio= request.form['txtPrecio']
        CS= mysql.connection.cursor()
        CS.execute('insert into tbflores(nombre,cantidad,precio) values (%s,%s,%s)',(Vnombre,Vcantidad, Vprecio))
        mysql.connection.commit()

    flash('Datos agregados correctamente')
    return redirect(url_for('ingresar'))



@app.route('/editar/<id>')
def editar(id): 
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas where id= %s ',(id,))
    consultaId= curEditar.fetchone()
    return render_template('EditarEliminar.html', fruta= consultaId)
    

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
      Vnombre= request.form['txtNombre']
      Vcantidad= request.form['txtCantidad']
      Vprecio= request.form['txtPrecio']

    cursorCon= mysql.connection.cursor()
    cursorCon.execute('update tbflores set nombre=%s, cantidad= %s, precio=%s where id= %s',(Vflor,Vcantidad,Vprecio,id))
    mysql.connection.commit()

    flash('Los datos se actualizaron en la BD')
    return redirect(url_for('consultas'))
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)