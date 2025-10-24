class Estado:
    def __init__(self, vocabulario: list):
        self.__transicoes = [None]*len(vocabulario)
        self.__vocabulario = vocabulario.copy()

    def proximo_estado(self, letra: str):
        if letra in self.__vocabulario: return self.__transicoes[letra]
        else: raise ValueError()

    def cadastrar_transicao(self, letra: str, proximo_estado):
        self.__transicoes[letra] = proximo_estado

class Automato:
    def __init__(self, num_estados, estado_inicial, vocabulario, estados_aceitos, matriz_transicao):
        self.__estado_inicial = estado_inicial
        self.__vocabulario = vocabulario
        self.__estados_aceitos = estados_aceitos
        self.__matriz_transicao = matriz_transicao
        self.__estado = estado_inicial

        self.__estados = [None]*num_estados
        for i in range(num_estados):
            self.__estados[i] = Estado(vocabulario)


        for i in range(num_estados):
            for j in range(len(vocabulario)):
                a = self.__estados[matriz_transicao[i][j]]
                self.__estados[i].cadastrar_transicao(vocabulario[j], a)

        self.__estado = self.__estados[estado_inicial]
        self.__estados_aceitos = [0]*len(estados_aceitos)
        for i in range(len(estados_aceitos)):
            self.__estados_aceitos[i] = self.__estados[estados_aceitos[i]]

    def __aceito_ou_nao(self):
        return self.__estado in self.__estados_aceitos
    
    def processa_string(self, string):
        for letra in string:
            self.__estado = self.__estado.proximo_estado(letra)
            return self.__aceito_ou_nao()

def main():
    vocabulario = ["a", "b"]
    num_estados = 4
    estado_incial = 0
    matriz_transicoes = [
        [1, 0],
        [1, 2],
        [1, 3],
        [1, 0]
    ]
    estados_aceitos = [3]
    automato = Automato(num_estados, estado_incial, vocabulario, estados_aceitos, matriz_transicoes)
    automato.processa_string("abb")

if __name__ == '__main__':
    main()
