from Usuario import *
from Profesor import *
from Estudiante import *
from Post import *
import API
import Otherfunctions
from datetime import datetime

#En el main es donde se desarrolla el menu principal de la pagina. Desplegamos el menu principal para que, por teclado
#el usuario indique que gestion desea monitorear, todas las opciones validadas. 
def main():
    usuarios = []
    posts = []

    app = API.init(usuarios, posts)
    ans = 'y'
    while ans == 'y':
        print(f'''BIENVENIDO A METROGRAM
            Un espacio donde puedes interactuar con la comunidad Unimetana
            a través de este espacio virtual.
            1. Gestión de Perfil
            2. Gestión de Multimedia
            3. Gestion de Interacciones
            4. Gestión de Moderación
            5. Estadísticas
            6. Salir''')
        option = int(input('''Ingresa las acciones que desees realizar: '''))
    #Módulo de Gestión de Perfil
    #Aqui desplegamos el menu de gestion de perfil donde, por teclado nuevamente, se pedira la accion que se desea realizar,
    #cada opcion esta validada igualement. Dentro de cada opcion, se encuentra una funcion definida acorde a la opcion que corresponde.
        if option == 1:
            while True:
                print(f'''
                    1. Registrar nuevo usuario
                    2. Buscar perfil
                    3. Cambiar información personal de tu cuenta
                    4. Borrar datos de tu cuenta
                    5. Volver al menu principal''')
                
                action = input(f'''Elige qué función deseas realizar: ''')
                if action == "1":
                    registro_usuario(usuarios)
                elif action == "2":
                    busqueda_usuario(usuarios)
                elif action == "3":
                    cambiar_informacion(usuarios)
                elif action == "4":
                    borrado(usuarios)
                elif action == "5":
                    break
                else:
                    action = input('Por favor ingresa una opción válida: ')
    #Módulo de Gestión de Multimedia
        elif option == 2:
            while True:
                usuario_encontrado = False
                usuario1 = input('Ingrese su username: ')
                for user in usuarios:
                    if user.username.lower() == usuario1.lower():
                        usuario_encontrado = True
                        break
                if not usuario_encontrado:
                    print("El usuario no existe")

                print(f'''
                    1. Registrar nuevo post
                    2. Buscar post
                    3. Volver al menu principal''')
                
                action = input(f'''Elige qué función deseas realizar: ''')
                if action == "1":
                    registro_post(usuarios, posts, usuario1)
                elif action == "2":
                    busqueda_post(usuarios, posts, usuario1)
                elif action == "3":
                    break
                else:
                    action = input('Por favor ingresa una opción válida: ')
    #Módulo de Gestión de Interacciones
        elif option == 3:
            pass
    #Módulo de Gestión Moderación
        elif option == 4:
            pass
    #Módulo de Estadísticas
        elif option == 5:
            pass
    #Cerrar el Programa
        elif option == 6:
            break

#Para registrar un usuario, creamos la funcion "registrar_usuario", pedimos por teclado
#nombre, apellido, correo, username, tipo(profesor o estudiante), si es profesor solicitamos departamento 
# y si es estudiante solicitamos carrera. Validamos todos estos inputs de manera que solo se registre informacion valida y 
#finalmente guardamos los datos como objetos dentro de la clase correspondiente para almacenarlos en una lista y asi
#guardar la informacion. Finalmente, se imprime un mensaje indicando que el resgistro fue realizado con exito.
def registro_usuario(usuarios):
    nombre = input('Ingrese su nombre: ')
    if not nombre.isalpha():
        nombre = input('Por favor ingrese un nombre válido: ')
    apellido = input('Ingrese su apellido: ')
    if not apellido.isalpha():
        apellido = input('Por favor ingrese un apellido válido: ')
    correo = input('Ingrese su correo unimet: ')
    for user in usuarios:
        if correo in usuarios:
            correo = input('El correo que ha colocado, no está disponible, por favor ingrese otro: ')
    username = input('Ingrese el username que quiera utilizar: ')
    for user in usuarios:
        if username in usuarios:
            username = input('El username que ha colocado, no está disponible, por favor ingrese otro: ')
    dni = Otherfunctions.get_dni(username)
    kind = input('¿Es estudiante (e) o profesor (p)?: ').lower()
    while kind != ("e") and kind !=("p"):
        kind = input('¿Es estudiante (e) o profesor (p)?: ').lower()
    
    if kind == 'p':
        kind = "profesor"
        departamento = input('Ingrese su departamento: ')
        seguidores = []
        for user in usuarios:
            if user.kind == "profesor":
                if user.departamento == departamento:
                    seguidores.append(user.dni)
        user = Profesor(dni, nombre, apellido, correo, username, kind, seguidores, departamento)
        usuarios.append(user)
        
    elif kind == 'e':
        kind = "estudiante"
        carrera = input('Ingrese la carrera que cursa: ')
        seguidores = []
        
        for user in usuarios:
            if user.kind == "estudiante":
                if user.carrera == carrera:
                    seguidores.append(user.dni)
        user = Estudiante(dni, nombre, apellido, correo, username, kind, seguidores, carrera)
        usuarios.append(user)
    else:
        kind = input('Por favor ingrese un estatus válido')
    
    print("Usuario creado con exito")


#Para realizarla busqueda de un usuario, definimos la funcion "busqueda_usuario". Se despliega un menu para que, por teclado,
#se ingrese si se desea buscar el usuario por username, departamento o carrera. Cada opcion esta validada de manera que
#si la opcion ingresada es incorrecta, el programa devolvera que no se ha podido econtrar el usuario. Por otro lado, si se busca
#un usuaruio por su username, el programa imprime toda la infromacion de dicho usuario. Si se busca un usuario por departamento
#o carrera, imprime un despliegue de todos los usuarios que pertenezcan a dicho departamento o carrera.
def busqueda_usuario(usuarios):
    while True:
        print(f'''
        1. Buscar por Username
        2. Buscar por Departamento
        3. Buscar por Carrera
        4. Volver al menu principal''')

        action = input(f'''Elige qué función deseas realizar: ''')

        if action == "1":
            username = input(f'Ingresa un username: ')
            resultado = False
            for user in usuarios:
                if (user.username).lower() == username.lower():
                    print(user.show())
                    resultado = True
                    break
            if resultado == False:
                print("No se encontró el usuario")

        elif action == "2":
            departamento = input(f'Ingresa un departamento: ')
            resultado = False
            for user in usuarios:
                if user.kind == "profesor":
                    if user.departamento.lower() == departamento.lower():
                        print(user.show())
                        resultado = True
                        break
            if resultado == False:
                print("No se encontró el usuario")

        elif action == "3":
            carrera = input(f'Ingresa un carrera: ')
            resultado = False
            for user in usuarios:
                if user.kind == "estudiante":
                    if user.carrera.lower() == carrera.lower():
                        print(user.show())
                        resultado = True
                        break
            if resultado == False:
                print("No se encontró el usuario")

        elif action == "4":
            break

        else:
            action = input('Por favor ingresa una opción válida')


#Para cambiar la informacion creamos la variable pedimos por teclado que se ingrese el username del usuario al que se desea
#cambiar informacion, una vez se verifica que el usuario existe, borramos la información que se desea cambiar. Preguntamos
#por teclado qué dato se desea cambiar y a qué se desea cambiar, para finalmente agregarlo a la lista e indicar que el cambio 
#se realizó con éxito
def cambiar_informacion(usuarios):
    while True:
        user_cambio=""
        username = input(f'Ingresa el username para el cambio de informacion: ')

        resultado = False
        for user in usuarios:
            if (user.username).lower() == username.lower():
                print(user.show())
                user_cambio = user
                usuarios.remove(user)
                resultado = True

        if resultado == False:
            print("No se encontró el usuario")
        else:
            print(f'''
            1. Nombre
            2. Apellido
            3. username
            4. email
            5. Departamento o Carrera
            6. Volver al menu principal''')

            action = input(f'''Elige qué dato deseas cambiar: ''')

            if action == "1":
                Nombre = input('Ingresa tu nuevo Nombre: ')
                user_cambio.nombre = Nombre
            elif action == "2":
                Apellido = input('Ingresa tu nuevo Apellido: ')
                user_cambio.apellido = Apellido
            elif action == "3":
                username = input('Ingresa tu nuevo username: ')
                user_cambio.username = username
            elif action == "4":
                email = input('Ingresa tu nuevo email: ')
                user_cambio.email = email
            elif action == "5":
                departa_carre = input('Ingresa tu nuevo Departamento/Carrera: ')
                if user_cambio == "profesor":
                    user_cambio.departamento = departa_carre
                else: 
                    user_cambio.carrera = departa_carre
            elif action == "6":
                break
            else:
                action = input('Por favor ingresa una opción válida: ')

            usuarios.append(user_cambio)
            print("Actualizado con exito")
            break


#Para borrar un usuario, pedimos por teclado el nombre del usuario que se desea liminar, una vez verificado que el usuario existe
#mostramos los datos del mismo y se pregunta si realmente se desea al eliminar ese usuario. Si la respuesta es sí, se procede
#a eliminar el usuario de la lista de usuarios por completo.
def borrado(usuarios):
    username = input(f'Ingresa el username para el cambio de informacion: ')

    for user in usuarios:
        if (user.username).lower() == username.lower():
            print(user.show())
            action = input("Realmente deseas eliminar a este usuario Si(s) o No(n)").lower()
            if action == 's':
                usuarios.remove(user)
                print("Borrado exitoso")
            elif action == 'n':
                continue


#Para registrar un post, pedimos por teclado los datos requeridos: usuario (primero se pide el username, que luego se convertira al
#id del mismo), tipo de post, descripcion, la fecha se asigna de acuerdo al momento que se publique, y los hashtags que se vayan
#a utilizar. Finalmente, agregamos el post a la lista de posts y tambien al dato 'post' perteniencte al usuario que le corresponde,
#y se emite un mensaje de que el post ha sido registrado de manera existosa. 
def registro_post(usuarios, posts, usuario1):
    tags = []
    usuario1 = usuario
    resultado = False
    for user in usuarios:
        if (user.username).lower() == usuario.lower():
                print(user.show())
                usuario = user.dni
                resultado = True
        if resultado == False:
            print("No se encontró el usuario")

    kind = input('Ingress el tipo de post que desea publicar: foto(f) o video(v): ')
    while True:
        if kind == 'f':
            kind = 'foto'
            break
        elif kind == 'v':
            kind = 'video'
            break
        else:
            kind = input('Por favor ingrese un tipo de post válido: ')

    descripcion = input('Ingrese la descripción de su publicación: ')
    fecha = str(datetime.now())
    num = int(input('¿Cuántos hashtags desea agregar? Escriba un número: '))
    for i in range (1, (num + 1)):
        tag = input('Ingresa tu hashtag: ')
        tags.append(tag)
    
    post = Post(usuario, kind, descripcion, fecha, tags)
    posts.append(post)
    for user in usuarios:
        if user.dni == usuario:
            user.posts.append(post)

    print('Post registrado con éxito')


#Para realizar la busqueda de un post, primero pedimos por teclado el username de la persona que esta navegando la red.
#Una vez confirmada su identidad, se le pregunta por teclado su desea buscar un post por username de la persona, o por hashtag.
#Si desea buscarlo por el username, se pide que ingrese por teclado el username de la persona que busca, si se cumple la condicion 
# de 'ver_posts', se mostrara la lista de posts del usuario ingresado, de lo contrario, se indica que no puede ser visualizado.
#Por otro lado, si se busca por hashtag, se pide que ingrese por teclado el nombre del hashtag; si se cumple la condicion 
#'ver _posts' entonces se muestra el listado de posts con ese hashtag que pertenezcan a las personas que siga el usuario que
#navega, de lo contrario se indica que posts no se pueden visualizar.
def busqueda_post(usuarios, posts, usuario1):
    while True:

        print(f'''' 
              1. Buscar post por username 
              2. Buscar post por hashtag 
              3. Volver al menú principal ''')
        action = input(f'''Elige qué función deseas realizar: ''')

        if action == "1":
            usuario = input(f'Ingresa un username: ')
            for user in usuarios:
                if (user.username).lower() == usuario.lower():
                    if usuario1 in user.seguidores:
                        continue
                    else:
                        print(f'No puedes ver los posts de {usuario1}, ya que no lo sigues')
                else:
                    print("No existe el usuario")
                    break
            resultado = False
            for user in usuarios:
                if (user.username).lower() == usuario.lower():
                    usuario = user.dni
                    for post in posts:
                        if post.usuario == usuario:
                            print(post.show())
                            resultado = True
                    if resultado == False:
                        print("No se encontró el usuario")


        elif action == "2":
            tag = input(f'Ingresa el hashtag que buscas: ')
            resultado = False
            for post in posts:
                usuario = post.usuario
                for t in post.tags:
                    if tag.lower() in t.lower():
                        print(post.show())
                        resultado = True
            if not resultado:
                print("No se encontró el hashtag")

        elif action == "3":
            break
        else:
            action = input('Por favor ingresa una opción válida')


main()