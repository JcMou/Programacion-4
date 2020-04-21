import time
import pypyodbc
from pymongo import MongoClient

def TiempoTranscurrido(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Tiempo = {0}:{1}:{2}".format(int(hours),int(mins),sec))
  
def InsertarSQL():
  Inicio = time.time()
  Connection = "DRIVER={SQL Server};SERVER=DESKTOP-62CJJS5\SQLEXPRESS;DATABASE=Evalueacion;UID=sa;PWD=123456"
  con2 = pypyodbc.connect(Connection)    
  myCursor = con2.cursor()
  for i in range(1000000):
  	myCursor.execute("insert into Pruebas(Nombre,Apellido,Cedula) values('Nombre"+str(i+1)+"','Apellido"+str(i+1)+"','"+str(i+1)+"')") 
  	myCursor.commit()    
  
  con2.close()
  Fin = time.time()
  Tiempo = Fin - Inicio
  TiempoTranscurrido(Tiempo)
  
def LeerSQL(Number):
  Inicio = time.time()
  Connection = "DRIVER={SQL Server};SERVER=DESKTOP-62CJJS5\SQLEXPRESS;DATABASE=Evalueacion;UID=sa;PWD=123456"
  con2 = pypyodbc.connect(Connection)    
  myCursor = con2.cursor()
  myCursor.execute("SELECT TOP "+str(Number)+" * from Pruebas")
  data = myCursor.fetchall()    
  con2.close()
  #print(data)
  Fin = time.time()
  Tiempo = Fin - Inicio
  TiempoTranscurrido(Tiempo)
  
def InsertarMongo():
  Inicio = time.time()
  client = MongoClient('mongodb://localhost:27017')
  db = client['Pruebas']
  post = db.PruebaInsert  
  for i in range(1000000):  	
    post.insert_one({'Nombre': 'Nombre'+str(i+1),'Apellido': 'Apellido'+str(i+1),'Cedula': str(i+1)})
  Fin = time.time()
  Tiempo = Fin - Inicio
  TiempoTranscurrido(Tiempo)
  
def LeerMongoDB(Number):
  Inicio = time.time()
  client = MongoClient('mongodb://localhost:27017')
  db = client['Pruebas']
  post = db.PruebaInsert    
  docs = post.find()  
  try:
    for i in range(Number):
      docs.next()
      #print (docs.next())	  
  except StopIteration as err:
    print ("StopIteration error:", err, "-- rewinding Cursor object.")
  docs.rewind()
  Fin = time.time()
  Tiempo = Fin - Inicio
  TiempoTranscurrido(Tiempo)
	
#InsertarSQL()
#LeerSQL(1000000)
#InsertarMongo()
#LeerMongoDB(1000000)
