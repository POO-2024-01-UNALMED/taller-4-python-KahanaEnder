from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes = None):
        if asignaturas is None:
            asignaturas = []
        if estudiantes is None:
            estudiantes = []
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista= None):
        if lista is None:
            lista = []
        lista.append(alumno)
        for elementos in lista:
            self.listadoAlumnos.append(elementos)
    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo


    # def __str__(self):
    #     pass

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
