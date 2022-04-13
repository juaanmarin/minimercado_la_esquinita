from flask import Flask, render_template, request

app= Flask(__name__)

titulos=("Documento","Nombre","Telefono","saldo")
informacion=[]

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/registrar")
def registrar_cliente():
  return render_template('registrar_cliente.html')

@app.route("/validar", methods=['POST'])
def valida():
  documento=""
  nombre=""
  telefono=""
  saldo=""

  if request.method=='POST':
    documento=request.form['documento']
    for i in range (len(informacion)):
      pocicion=informacion[i]
      verificar=documento in pocicion
      if verificar==False:
        print("no se actualiza")
      elif(verificar==True):
        for j in range (len(pocicion)):
          print(pocicion[j])
          documento=pocicion[0]
          nombre=pocicion[1]
          telefono=pocicion[2]
          saldo=pocicion[3]
  datos=[documento,nombre,telefono,saldo]

  return render_template('actualizar.html', data=datos)


@app.route("/actualizar", methods=['GET','POST'])
def actualizar():
  documento=""
  nombreNuevo=""
  nuevoTel=""
  nuevoSaldo=""
  print()
  if request.method=='POST':
    documento=request.form['actualiza']
    nombreNuevo=request.form['nombreN']
    nuevoTel=request.form['telNuevo']
    nuevoSaldo=request.form['saldoN']
    for i in range (len(informacion)):
      pocicion=informacion[i]
      verificar=documento in pocicion[0]
      if verificar==False:
        print("no se encontro")
      elif(verificar==True):
        print("actualizar")
        if (nombreNuevo==""):
          nombreNuevo=pocicion[1]
        elif (nombreNuevo!="") :
          pocicion.remove(pocicion[1])
          pocicion.insert(1, nombreNuevo)
        if(nuevoTel==""):
          nuevoTel=pocicion[2]
        elif (nuevoTel!=""):
          pocicion.remove(pocicion[2])
          pocicion.insert(2, nuevoTel)

        s=int(pocicion[3])
        
        if(nuevoSaldo==""):
          nuevoSaldo=int(pocicion[3])
        elif(nuevoSaldo!=""):
          ns=int(nuevoSaldo)
          if (s>=0):
            desc=s-ns
          elif(s<0):
            desc=s+ns
          
          pocicion[3]=desc
          
  dato=nombreNuevo
  print(documento)
  print(nombreNuevo)
   
  return render_template('actualizar.html', lista=dato)


@app.route("/datos")
def datos():
  return render_template("datos.html",titulos_tabla=titulos,data=informacion)


@app.route("/agregar_persona", methods=["POST"])
def agregar_persona():
  if (request.method=="POST"):
    documento=request.form["documento"]
    Nombre=request.form["Nombre"]
    Telefono=request.form["Telefono"]
    Saldo=request.form["Saldo"]

   
    listainfo=[documento,Nombre,Telefono,Saldo]
    informacion.append(listainfo)

    print("***************************************")

  return render_template("registrar_cliente.html",data=informacion)

if (__name__ == "__main__"):
  app.run(debug=True,port=8000)




