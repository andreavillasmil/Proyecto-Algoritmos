class Post:

    def __init__(self, usuario, kind, descripcion, fecha, tags):
        self.usuario = usuario
        self.kind = kind
        self.descripcion = descripcion
        self.fecha = fecha
        self.tags = tags
        self.likes = []
        self.comentarios = []

    def show(self):
        return f'''
        Usuario: {self.usuario}
        Tipo: {self.kind}
        Descripción: {self.descripcion}
        Fecha: {self.fecha}
        Hashtags: {self.tags}
        Likes: {self.likes}
        Comentarios: {self.comentarios}
        '''
