import math
import operator

def criarArquivo(nome_arquivo): # Cria Lista de Arquivo
    arquivo = open(nome_arquivo, "r")
    lista = arquivo.readlines()
    arquivo.close()
    
    return lista

def calcularDistanciaEuclidiana(sepala, petala):
    distancia = 0
    for x in range(4):
        distancia += pow((float(sepala[x]) - float(petala[x])), 2)
        
    return math.sqrt(distancia)


def gravarArquivo(lista, nome_arquivo):
    arquivo = open(nome_arquivo,"w")
    for x in lista:
        arquivo.write(x+"\n")
    arquivo.close()

        
def getRotuloEscolhido(rotulos):
    if(len(rotulos)== 1):
        return rotulos[0][0]
    else:
        
        rotulo_escolhido = rotulos[0][0]
        for x in range(1, len(rotulos)):
            if(rotulos.count(rotulos[x][0]) > rotulos.count(rotulo_escolhido)):
                rotulo_escolhido = rotulos[x][0]
                
        return rotulo_escolhido


def getVizinhos(teste_treinamento, conjunto_treinamento, k):
    mais_proximos = []
    for x in conjunto_treinamento: # Acessando cada flor do conjunto de treinamento
        dist = calcularDistanciaEuclidiana(teste_treinamento, x.split(",")) # Utilizando o calcula distância euclidiana da lista de teste.
        mais_proximos.append([x.split(",")[4][:-1], dist])
    mais_proximos.sort(key = operator.itemgetter(1)) #vai ordernar pelo indice 1 de cada sublista;
    
    return mais_proximos[:k] # rodar até antes do limite de k;

def criarArquivoResultado(conjunto_treinamento, lista_teste_treinamento, k):
    resultado = []

    for x in lista_teste_treinamento:
        teste_treinamento = x.split(",")
        rotulos_teste_treinamento = getVizinhos(teste_treinamento, conjunto_treinamento,k)
        rotulo_escolhido = getRotuloEscolhido(rotulos_teste_treinamento)
        resultado.append(rotulo_escolhido)
        
    return resultado
        
def calcularPorcentagem(resultado, rotulosTeste):
    quant_acertos = 0
    
    for x in range(len(resultado)):
        if(resultado[x] + "\n" == rotulosTeste[x]):
            quant_acertos +=1
    porcentagem = (100*quant_acertos)//len(resultado)
    
    return porcentagem


def main():

    k = int(input("Digite o valor que deseja para k: "))
    conjunto_treinamento = criarArquivo("treinamento.txt")
    lista_teste_treinamento = criarArquivo("teste.txt")
    lista_rotulos_teste = criarArquivo("rotulosteste.txt")
    lista_resultado = criarArquivoResultado(conjunto_treinamento, lista_teste_treinamento, k)
    gravarArquivo(lista_resultado, "resultado.txt")
    porcentagem = calcularPorcentagem(lista_resultado, lista_rotulos_teste)

    print ("Obteve como percentual de: ", porcentagem, "% de acertos!")
    
main()
    
    
