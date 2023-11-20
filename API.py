import json
import pip._vendor.requests as requests
import Post
from Profesor import *
from Usuario import *
from Estudiante import  *

def init(usuarios, posts):
  get_users(usuarios)
  get_posts(posts)
  user_posts(usuarios, posts)


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

   for post_data in res:
      usuario = post_data["publisher"]
      kind = post_data["type"]
      descripcion = post_data["caption"]
      fecha = post_data["date"]
      tags = post_data["tags"]

      new_post = Post.Post(usuario, kind, descripcion, fecha, tags)
      posts.append(new_post)

def user_posts(usuarios, posts):
  for post in posts:
        for user in usuarios:
            if post.usuario == user.dni:
                if isinstance(user, Profesor):
                    user.posts.append(post)
                elif isinstance(user, Estudiante):
                    user.posts.append(post)
