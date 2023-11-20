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
                    4. Borrar tu cuenta
                    5. Volver al menu principal''')
                
                action = input(f'''Elige qué función deseas realizar: ''')
                if action == "1":
                    registro_usuario(usuarios)
                    break
                elif action == "2":
                    busqueda_usuario(usuarios)
                    break
                elif action == "3":
                    cambiar_informacion(usuarios)
                    break
                elif action == "4":
                    borrado(usuarios)
                    break
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
                    break

                print(f'''
                    1. Registrar nuevo post
                    2. Buscar post
                    3. Volver al menu principal''')
                
                action = input(f'''Elige qué función deseas realizar: ''')
                if action == "1":
                    registro_post(usuarios, posts, usuario1)
                    break
                elif action == "2":
                    busqueda_post(usuarios, posts, usuario1)
                    break
                elif action == "3":
                    break
                else:
                    action = input('Por favor ingresa una opción válida: ')

    #Módulo de Gestión de Interacciones
        elif option == 3:
            while True:
                usuario_encontrado = False
                usuario1 = input('Ingrese su username: ')
                for user in usuarios:
                    if user.username.lower() == usuario1.lower():
                        usuario1 = user.dni
                        usuario_encontrado = True
                        break
                if not usuario_encontrado:
                    print("El usuario no existe")
                    break
                print(f'''
                1. Seguir a un usuario
                2. Dejar de seguir a un usuario
                3. Eliminar comentario
                4. Revisar solicitudes
                5. Volver al menu principal
                ''')
                action = input('Elige que accion deseas realizar: ')
                if action == '1':
                    seguir_usuario(usuario1, usuarios)
                    break
                elif action == '2':
                    dejar_seguir_usuario(usuario1, usuarios)
                    break
                elif action == '3':
                    eliminar_comentario(usuario1, usuarios, posts)
                    break
                elif action == '4':
                    revisar_solicitudes(usuario1, usuarios)
                elif action == '5':
                    break
                else:
                    print('Elige una opcion valida')


    #Módulo de Gestión Moderación
        elif option == 4:
            while True:
                kind = input('Es usted estudiante(e), profesor(p) o administrador(a): ')
                if kind == 'a':
                    print('Bienvenido al módulo de gestión de moderación')
                    print(f'''
                    1. Eliminar un post
                    2. Eliminar un comentario
                    3. Eliminar un usuario
                    4. Volver al menú principal
                    ''')
                    action = input(f'''Elige qué acción deseas realizar: ''')
                    if action == '1':
                        eliminar_post(usuarios, posts)
                        break
                    elif action == '2':
                        eliminar_comentario(usuarios, posts)
                        break
                    elif action == '3':
                        eliminar_usuario(usuarios)
                        break
                    elif action == '4':
                        break
                    else:
                        print('Por favor elija una opción válida: ')

                elif kind == 'p':
                    print('Como usted es profesor, no puede realizar funciones de administrador')
                    print('Sin embargo, puede notificar al personal administrativo en caso de ver actividad ofensiva')
                elif kind == 'e':
                    print('Los estudiantes no pueden realizar funciones de administrador')
                    break
                else:
                    print('Por favor escoja una opción válida')
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

#Esta funcion la ocuparemos para verificar si un usuario A sigue a un usuario B para poder ver sus posts.
def ver_posts(usuarios, usuario, usuario1):
    for user in usuarios:
                if (user.username).lower() == usuario.lower():
                    if usuario1 in user.seguidores:
                        continue
                    else:
                            print(f'No puedes ver los posts de {usuario1}, ya que no lo sigues')
                            break
                    
#Esta funcion la ocuparemos para identificar un post en específico.
def identify_posts(usuarios, posts):
    usuario = input('Ingrese el usuario que publicó el post: ')
    usuario_encontrado = False
    for user in usuarios:
        if (user.username).lower() == usuario.lower():
            usuario = user.dni
            usuario_encontrado = True
            break
    if not usuario_encontrado:
        print("No se encontró el usuario")
    descripcion = input('Ingrese la descripción del post del usuario que desea visualizar: ')
    for post in posts:
        if usuario == post.usuario:
            if descripcion.lower() == post.descripcion.lower():
                print(post.show())
                return post and usuario
    print("No se encontró el post")


#Para registrar un post, pedimos por teclado los datos requeridos: usuario (primero se pide el username, que luego se convertira al
#id del mismo), tipo de post, descripcion, la fecha se asigna de acuerdo al momento que se publique, y los hashtags que se vayan
#a utilizar. Finalmente, agregamos el post a la lista de posts y tambien al dato 'post' perteniencte al usuario que le corresponde,
#y se emite un mensaje de que el post ha sido registrado de manera existosa. 
def registro_post(usuarios, posts, usuario1):
    tags = []
    resultado = False
    for user in usuarios:
        if (user.username).lower() == usuario1.lower():
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
#Además se incluye la función 'identify_post' donde se pregunta al usuario si desea ver un post en particular; luego se pregunta si 
#se quiere dejar un like y/o comentar. En caso afirmativo para ambos, se agregan las interacciones a los likes y comentarios del post.
#Por otro lado, si se busca por hashtag, se pide que ingrese por teclado el nombre del hashtag; si se cumple la condicion 
#'ver _posts' entonces se muestra el listado de posts con ese hashtag que pertenezcan a las personas que siga el usuario que
#navegaluego se pregunta si se quiere dejar un like y/o comentar. En caso afirmativo para ambos, se agregan las 
#interacciones a los likes y comentarios del post.De lo contrario se indica que posts no se pueden visualizar.
def busqueda_post(usuarios, posts, usuario1):
    while True:

        print(f'''' 
              1. Buscar post por username 
              2. Buscar post por hashtag 
              3. Volver al menú principal ''')
        action = input(f'''Elige qué función deseas realizar: ''')

        if action == "1":
            resultado = False
            usuario = input(f'Ingresa un username: ')
            for user in usuarios:
                if (user.username).lower() == usuario.lower():
                    ver_posts(usuarios, usuario, usuario1)
                    resultado = True
                    break
                if not resultado:
                    print("No existe el usuario")
                    break
            resultado = False
            for user in usuarios:
                if (user.username).lower() == usuario.lower():
                    usuario = user.dni
                    for post in posts:
                        if post.usuario == usuario:
                            print(post.show())
                            seguir = input('¿Desea abrir alguna publicación en específico? Si(s) o No(n): ')
                            if seguir == 's':
                                identify_posts(usuarios, posts)
                                dar_like = input('¿Desea dar un like a esta publicación? Si(s) o No(n): ')
                                if dar_like == 's':
                                    post.dar_like(usuario)
                                elif dar_like == 'n':
                                    continue
                                else:
                                    print('Por favor elige una opción válida')
                                    break
                                comentar = input('¿Quieres dejar un comentario en esta publicación? Si(s) o No(n): ')
                                if comentar == 's':
                                    comentario = input('Escribe el comentario que desees dejar: ')
                                    post.comentar(usuario, comentario)
                                    resultado = True
                                    break
                                elif comentar == 'n':
                                    resultado = True
                                    break
                                else:
                                    print('Por favor elige una opción válida')
                                    break


                            elif seguir == 'n':
                                break
                            else:
                                    print('Por favor elige una opción válida')
                                    break

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
                        seguir = input('¿Desea abrir alguna publicación en específico? Si(s) o No(n): ')
                        if seguir == 's':
                            identify_posts(usuarios, posts)
                            dar_like = input('¿Desea dar un like a esta publicación? Si(s) o No(n): ')
                            if dar_like == 's':
                                post.dar_like(usuario)
                            elif dar_like == 'n':
                                continue
                            else:
                                print('Por favor elige una opción válida')
                                break
                            comentar = input('¿Quieres dejar un comentario en esta publicación? Si(s) o No(n): ')
                            if comentar == 's':
                                comentario = input('Escribe el comentario que desees dejar: ')
                                post.comentar(usuario, comentario)
                                resultado = True
                                break
                            elif comentar == 'n':
                                resultado = True
                                break
                            else:
                                print('Por favor elige una opción válida')
                                break
                        elif seguir == 'n':
                            break
                        else:
                                print('Por favor elige una opción válida')
                                break

            if not resultado:
                print("No se encontró el hashtag")

        elif action == "3":
            break
        else:
            action = input('Por favor ingresa una opción válida')

#Para eliminar un post, ejecutamos la funcion 'identify_post' que permite buscar el post exacto que buscamos eliminar. Una vez
#identificado, se pide por teclado una reafirmacion de si se quiere eliminar el post porque es ofensivo; en caso afirmativo, se 
#elimina el post y se da un mensaje para certificar, y dependiendo del tipo de usuario, se acredita una amonestacion al mismo. 
#En caso contrario, simplemente sale al menu principal nuevamente. Y en caso de que los datos no coincidan, se indica que 
#el post no pudo eliminarse.
def eliminar_post(usuarios, posts):
    post = identify_posts(usuarios, posts)
    if post:
        while True:
            opcion = input('¿Seguro que desea eliminar este post? ¿Realmente es ofensivo? Si(s) o No(n): ')
            if opcion.lower() == 's':
                posts.remove(post)
                print('Post eliminado con éxito')
                for usuario in usuarios:
                    if isinstance(usuario, Profesor) and usuario.dni == post.usuario:
                        usuario.amonestaciones += 1
                        break
                    elif isinstance(usuario, Estudiante) and usuario.dni == post.usuario:
                        usuario.amonestaciones += 1
                        break
            elif opcion.lower() == 'n':
                break
            else:
                print('Por favor ingrese una opción válida')
    else:
        print('No se puede eliminar el post porque no se encontró el usuario o el post')


#Para eliminar un comentario, llamamos nuevamente la funcion 'identify_post' dentro de la variable post para que no se pierdan
#los datos del post. Una vez identificado, se pide por teclado el username de la persona y el comentario textual que realizo. Luego
#se busca en el post ya identificado, algun comentario que coincida con los datos ingresados, si existe, se elimina y se le acredita
#una amonestacion al usuario que lo haya comentado. En caso contrario, se indica que el comentario no se encontro.
def eliminar_comentario(usuarios, posts):
    post = identify_posts(usuarios, posts)
    if post:
        usuario = input('Ingresa el username de la persona que comentó: ')
        user_encontrado = False
        for user in usuarios:
            if user.username.lower() == usuario.lower():
                print(user.show())
                user_encontrado = True
                usuario_dni = user.dni
                break
        if not user_encontrado:
            print("No se encontró el usuario")
        comentario = input('Ingresa el comentario que deseas eliminar: ')
        comentario_eliminado = False
        for p in posts:
            if p == post:
                for c in p.comentarios:
                    if usuario_dni == c[0] and comentario.lower() in c[1].lower():
                        p.comentarios.remove(c)
                        comentario_eliminado = True
                        break
                if comentario_eliminado:
                    print('Comentario eliminado con éxito')
                    for usuario in usuarios:
                        if isinstance(usuario, Profesor) and usuario.dni == post.usuario:
                            usuario.amonestaciones += 1
                            break
                        elif isinstance(usuario, Estudiante) and usuario.dni == post.usuario:
                            usuario.amonestaciones += 1
                            break
        if not comentario_eliminado:
            print('No se encontró el comentario')
    else:
        print('No se puede eliminar el comentario porque no se encontró el usuario o el post')

#Para eliminar un usuario, se pide por teclado que se indique el username de dicho usuario. Luego, verificando si es profesor o
#estudiante, se verifica el nmero de amonestaciones que tenga. Si tiene 3 o mas amonestaciones, se elimina el usuario automaticamente.
#En caso contrario, se indica que el usuario tiene menos de 3 amonestaciones y no se elimina.
def eliminar_usuario(usuarios):
    usuario = input('Ingrese el username del usuario que desea eliminar: ')
    for user in usuarios:
        if user.username.lower() == usuario.lower():
            if isinstance(usuario, Profesor):
                if usuario.amonestaciones >= 3:
                    usuarios.remove(usuario)
                    print('Usuario eliminado con exito')
                    break
                else:
                    print('El usuario tiene menos de tres amonestaciones')
            elif isinstance(usuario, Estudiante):
                if usuario.amonestaciones >= 3:
                    usuarios.remove(usuario)
                    print('Usuario eliminado con exito')
                    break
                else:
                    print('El usuario tiene menos de tres amonestaciones')

#Para seguir un usuario, tomamos la variable usuario1 ya dada por el menu. Comparamos si el id del usuario1 esta dentro de los
#seguidores del usuario, en caso afirmativo, se indica que ya sigue a ese usuario y vuelve al menu principal. En caso contrario
#se agrega el dni del usuario1 a las solicitudes del usuario y se indica que usuario1 esta dentro de las solicitudes de usuario.
def seguir_usuario(usuario1, usuarios):
    usuario = input('Ingrese el username del usuario que desea seguir: ')
    usuario_encontrado = False
    for user in usuarios:
        if user.username.lower() == usuario.lower():
            usuario1 = user.dni
            usuario_encontrado = True
            if usuario1 in user.seguidores:
                print('Ya sigues a este usuario')
                break
            else:
                user.solicitudes.append(usuario1)
                print(f'Estás en las solicitudes de seguimiento de {user.username}, debe aceptarte para poder seguirlo')
            break
    if not usuario_encontrado:
        print("El usuario no existe")
    
#Para dejar de seguir un usuario, tomamos la variable usuario1 ya dada por el menu. Comparamos si el id de usuario1 esta dentro de
#la lista de seguidores de usuario, en caso afirmativo, se elimina a usuario1 de la lista de seguidores de usuario. En caso contrario,
#se indica que usuario1 no sigue a usuario.
def dejar_seguir_usuario(usuario1, usuarios):
    usuario = input('Ingrese el username del usuario que desea dejar de seguir: ')
    usuario_encontrado = False
    for user in usuarios:
        if user.username.lower() == usuario.lower():
            usuario1 = user.dni
            usuario_encontrado = True
            if usuario1 in user.seguidores:
                user.seguidores.remove(usuario1)
                print('Dejaste de seguir a este usuario')
            else:
                print('No sigues a este usuario')
            break
    if not usuario_encontrado:
        print("El usuario no existe")

#Para revisar solicitudes, tomamos la variable usuario1 ya dad por el menu. Imprimimos las solicitudes que hayan para usuario1.
#Preguntamos por teclado si se desea aceptar alguna solicitud, en caso afirmativo, se pide por teclado que se ingrese el id de 
#la solicitud que se quiere aceptar, se verifica que el id no este en seguidores y se agrega a la lista de seguidores. 
# En caso contrario se indica que ya se sigue a ese usuario.
def revisar_solicitudes(usuario1, usuarios):
   while True:
    print(usuario1.solicitudes)
    opcion = input('Deseas aceptar alguna solicitud?: Si(s) o No(n): ')
    if opcion == 's':
        usuario = input('Ingresa el id de la solicitud que desees aceptar: ')
        usuario_encontrado = False
        for user in usuarios:
            if user.username.lower() == usuario.lower():
                usuario_encontrado = True
                if usuario1 not in user.seguidores:
                    user.seguidores.append(usuario1)
                    print(f'Ahora sigues a {user.username}')
                else:
                    print('Ya sigues a este usuario')
                break
            if not usuario_encontrado:
                print("El usuario no existe")
    elif opcion == 'n':
        break
    else:
       print('Ingrese una opcion valida')


main()
