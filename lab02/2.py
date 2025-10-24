class Ponto2D():
    def __init__(self, x, y):
        self.__x = y
        self.__y = x

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def distancia_entre_pontos(self, ponto):
        return (ponto.get_y() - self.get_y())**2 +  (ponto.get_x() - self.get_x())**2
    
class Ponto3D(Ponto2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    def get_z(self):
        return self.__z
    
    def distancia_entre_pontos(self, ponto):
        return super().distancia_entre_pontos(ponto) + (ponto.get_z() - self.get_z())**2
    
def main():
    p1 = Ponto3D(1, 2, 1)
    p2 = Ponto3D(1, 3, 2)

    print( (p1.distancia_entre_pontos(p2))**(0.5) )
    
if __name__ == "__main__":
    main()