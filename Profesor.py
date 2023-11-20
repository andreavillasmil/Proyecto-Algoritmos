from Usuario import Usuario

class Profesor(Usuario):
    def __init__(self, dni, nombre, apellido, correo, username, kind, seguidores, departamento):
        super().__init__(dni, nombre, apellido, correo, username, kind, seguidores)
        self.departamento = departamento
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
            Departamento: {self.departamento}
            Seguidores: {self.seguidores}
            Posts: {self.posts}
            '''
    
