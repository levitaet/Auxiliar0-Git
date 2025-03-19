class Usuario:
    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"[X] {tarea.obtenerNombre()}" )
            else:
                print(f"[ ] {tarea.obtenerNombre()}" )

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
