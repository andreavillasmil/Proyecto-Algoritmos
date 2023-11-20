from Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, dni, nombre, apellido, correo, username, kind, seguidores, carrera):
        super().__init__(dni, nombre, apellido, correo, username, kind, seguidores)
        self.carrera = carrera
        self.amonestaciones = 0
        self.likes = []
        self.comentarios = []
        self.solicitudes = []


    def show(self):
        return f'''
            ID: {self.dni}
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Correo: {self.correo}
            Username: {self.username}
            Type: {self.kind}
            Carrera: {self.carrera}
            Seguidores: {self.seguidores}
            Posts: {self.posts}
            '''
    
