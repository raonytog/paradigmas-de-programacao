class Ponto():
    def __init__(self, x, y):
        self.__x = y
        self.__y = x

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def distancia_entre_pontos(self, ponto):
        return ( (ponto.get_y() - self.get_y())**2 +  (ponto.get_x() - self.get_x())**2 )**(0.5)
    
def main():
    p1 = Ponto(1, 2)
    p2 = Ponto(1, 3)

    print(p1.distancia_entre_pontos(p2))
    
if __name__ == "__main__":
    main()