import json
import pip._vendor.requests as requests
import Post
from Profesor import *
from Usuario import *
from Estudiante import  *

def init(usuarios, posts):
  get_users(usuarios)
  get_posts(posts)


def get_users(usuarios):
  res = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json")
  res = json.loads(res.text)

  for usuario in res:
    dni = usuario["id"]
    nombre = usuario["firstName"]
    apellido = usuario["lastName"]
    correo = usuario["email"]
    username = usuario["username"]
    kind = usuario["type"]
    seguidores = usuario["following"]

    if kind == 'professor':
          departamento = usuario["department"]
          user = Profesor(dni, nombre, apellido, correo, username, "profesor", seguidores, departamento)
          usuarios.append(user)
          
    elif kind == 'student':
        carrera = usuario["major"]
        user = Estudiante(dni, nombre, apellido, correo, username, "estudiante", seguidores, carrera)
        usuarios.append(user)
  
def get_posts(posts):
   res = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/posts.json")
   res = json.loads(res.text)

   for post in res:
      usuario = post["publisher"]
      kind = post["type"]
      descripcion = post["caption"]
      fecha = post["date"]
      tags = post["tags"]

      post = Post.Post(usuario, kind, descripcion, fecha, tags)
      posts.append(post)