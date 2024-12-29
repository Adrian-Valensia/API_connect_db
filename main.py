from fastapi import FastAPI, HTTPException, status
#Para crear las clases del cuerpo de nuestro metodos
from pydantic import BaseModel
#No puedes importar psycopg2 sin instalar POSTGREsql 
#Te pedira los archivos DLL
import psycopg2
#Para poder insertar datos tipo fecha
from datetime import date, time, datetime
#Manda a traer los recursos de controllers
from controllers.movies_controllers import Movie, db_params

#Nombre de nuestra app
app = FastAPI()

#Creamos el conector con psycopg2
conn = psycopg2.connect(**db_params)

#DEFINIMOS NUESTRO CRUD

@app.get('/my_movies')
def read_movies(): 
    cur = conn.cursor()   
    cur.execute('SELECT * FROM my_movies')
    rows = cur.fetchall()
    cur.close()
    return {'my_movies':rows}

@app.post('/my_movies')
def create_movie(item: Movie):
    cur = conn.cursor()
    cur.execute('INSERT INTO my_movies (autor, Descripcion, Fecha_Estreno) VALUES (%s, %s, %s)', (item.autor, item.Descripcion, item.Fecha_Estreno))
    conn.commit()
    cur.close()
    return {'message': 'Movie created successfully'}

@app.put('/my_movies/{movie_id}')
def update_item(movie_id: int, item: Movie):
    cur = conn.cursor()
    cur.execute('UPDATE my_movies SET autor = %s, Descripcion = %s, Fecha_Estreno = %s WHERE id = %s', (item.autor, item.Descripcion, item.Fecha_Estreno, movie_id)) 
    conn.commit()
    cur.close()
    return {'message': 'Movie updated successfully'}

@app.delete('/my_movies/{movie_id}')
def delete_item(movie_id: int):
    cur = conn.cursor()
    cur.execute('DELETE FROM items WHERE id = %s', (movie_id,))
    conn.commit()
    cur.close()
    return {'message': 'Movie deleted successfully'}