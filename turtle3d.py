from vpython import *


def initialize_scene():
    """
    Inicialitza la escena per a que la tortuga pugui dibuixar
    :return: No retorna res
    """
    scene.height = scene.width = 1000
    scene.autocenter = True


class Turtle3D:

    def __init__(self):
        """
        Funció que inicialitza una instancia tortuga

        angleV: angle vertical de la tortuga

        angleH: angle horitzontal de la tortuga

        position: posició actual de la tortuga

        pinta: Permet saber si hem de pintar o no

        color_t: Defineix el color de la tortuga
        """
        self.angleV = 0.0
        self.angleH = 0.0
        self.position = vector(0, 0, 0)
        self.pinta = True
        self.color_t = vector(1, 0, 0)
        initialize_scene()

    def displacement_vector(self, dist: float):
        """
        Aquesta funció ens permet calcular el vector que ens hem de desplaçar per poder calcular la nova posisió de la
        tortuga
        :param dist: la distancia que ens hem de moure
        :return: retornem el vector que conté el desplaçament que hem de aplicar a la posició actual per anar fins la
        nova posició
        """
        x = dist * cos(radians(self.angleH)) * cos(radians(self.angleV))
        y = dist * sin(radians(self.angleV))
        z = dist * sin(radians(self.angleH)) * cos(radians(self.angleV))
        return vector(x, y, z)

    def draw_cylinder(self, desp: vector):
        """
        Aquesta funció s'encarrega de pintar un cilindre començant des de la posició actual fins a un desplaçament
        representat per el vector disp
        :param desp: vector que representa el desplaçament que hem de pintar des de la posició actual
        :return: No retornem res.
        """
        cylinder(pos=self.position, axis=desp, radius=0.1, color=self.color_t)

    def draw_sphere(self):
        """
        Aquesta funció s'encarrega de pintar una esfera de radi 0.1 en la posició actual de la tortuga
        :return: Hem dibuixat una esfera en la posició actual de radi 0.1 amb el color actual de la tortuga
        """
        sphere(pos=self.position, radius=0.1, color=self.color_t)

    def color(self, r: float, g: float, b: float):
        """
        Aquesta funció ens permet asignar-li un nou color a la tortuga
        :param r: Componenet vermella del nou color
        :param g: Component verd del nou color
        :param b: Componenet blau del nou color
        :return: No retornem res.
        """
        self.color_t = vector(r, g, b)

    def hide(self):
        """
        Aquesta operació permet deshabilitar la funció de pintar de la tortuga. És a dir, fa que la tortuga segueixi
        desplaçant-se, però, ara no pinta per on pasa.
        :return: No retornem res.
        """
        self.pinta = False

    def show(self):
        """
        Aquesta operació ens permet habilitar la funcionalitat de pintar de la tortuga.
        :return: No retornem res.
        """
        self.pinta = True

    def home(self):
        """
        Aquesta funció ens permet recolocar la tortuga en el punt de inici.
        :return: No retornem res.
        """
        self.position = vector(0, 0, 0)

    def forward(self, dist: float):
        """
        Aquesta funció ens permet desplaçar la tortuga cap endavant una distancia definida per el parametre dist. A més
        de desplaçar, si la tortuga té habilitat de pintar, pintem el desplaçament. En cas contrari, només ens desplaçem.
        :param dist: Distancia a recorrer per la tortuga.
        :return: No retornem res.
        """
        disp = self.displacement_vector(dist)
        if self.pinta:
            self.draw_sphere()
            self.draw_cylinder(disp)
            self.position += disp
            self.draw_sphere()
        else:
            self.position += disp

    def backward(self, dist):
        """
        Aquesta funció ens permet desplaçar la tortuga cap enrere una distancia definida per el parametre dist. A més
        de desplaçar, si la tortuga té habilitat de pintar, pintem el desplaçament. En cas contrari, només ens desplaçem.
        :param dist: Distancia a recorrer per la tortuga.
        :return: No retornem res.
        """
        disp = self.displacement_vector(-dist)
        if self.pinta:
            self.draw_sphere()
            self.draw_cylinder(disp)
            self.position += disp
            self.draw_sphere()
        else:
            self.position += disp

    def left(self, desp):
        """
        Aquesta operació ens permet girar la tortuga cap a la esquerra un angle definit per desp(graus)
        :param desp: Angle en graus que hem de girar a la esquerra
        :return: No retornem res.
        """
        self.angleH += desp
        self.angleH = self.angleH % 360

    def right(self, desp):
        """
        Aquesta operació ens permet girar la tortuga cap a la dreta, un angle definit per desp(graus)
        :param desp: Angle en graus que hem de girar a la esquerra
        :return: No retornem res.
        """
        self.angleH -= desp
        self.angleH = self.angleH % 360

    def up(self, desp):
        """
        Aquesta operació ens permet elevar la direcció de la tortuga un angle definit per desp(graus)
        :param desp: Angle en graus que hem de elevar la direcció de la tortuga
        :return: No retornem res.
        """
        self.angleV += desp
        self.angleV = self.angleV % 360

    def down(self, desp):
        """
        Aquesta operació ens permet baixar la direcció de la tortuga un angle definit per desp(graus)
        :param desp: Angle en graus que hem de baixar la direcció de la tortuga
        :return: No retornem res.
        """
        self.angleV -= desp
        self.angleV = self.angleV % 360
