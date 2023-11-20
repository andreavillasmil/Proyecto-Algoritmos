class Usuario():
    def __init__(self, dni, nombre, apellido, correo, username, kind, seguidores):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.username = username
        self.kind = kind
        self.posts = []
        self.seguidores = seguidores
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
        Seguidores: {self.seguidores}
        Posts: {self.posts}
        '''
