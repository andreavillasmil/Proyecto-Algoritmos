from datetime import datetime
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
    
    def dar_like(self, usuario):
        if usuario not in self.likes:
            self.likes.append(usuario)
            print(f'{usuario} dio like a la publicación.')
        else:
            self.likes.remove(usuario)


    def comentar(self, usuario, comentario):
        fecha = str(datetime.now())
        self.comentarios.append((usuario, comentario, fecha))
        print(f'{usuario} comentó en la publicación: {comentario}')
