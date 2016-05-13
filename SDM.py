import distance
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image 

def exibeimagem(arr):
    img = Image.fromarray(arr)
    img = img.convert('L')
    plt.imshow(img, interpolation='nearest')
    plt.show() 
    
def primeiracamada(matriz,palavra,raio):
    # faz a leitura da palavra, compara com a matriz de enderecos e retorna as linhas que estão próximas
    matrizretorno = [] 
    for linha in range(len(matriz)):
        dif = distance.hamming(matriz[linha],palavra)        
        if dif <= raio :
            matrizretorno.append(matriz[linha])           
            
    return (matrizretorno)

def segundacamada(matriz, palavra):    
    # para operação de leitura - acrescenta o valor da locação
    col = len(matriz[0])
    lin = len(matriz)
    
    memoria = np.zeros((lin,col)) # cria a memória que será utilizada

    operacao = 'w'
    # fase de armazenamento
    if operacao == 'w': 
        for linha in range(len(matriz)):            
            for coluna in range(len(matriz[0])):
                valor2 = matriz[linha][coluna]
                valor1 = memoria[linha][coluna]
                memoria[linha,coluna] = valor1 + valor2
            
       # return (memoria)
        print ('------------- ENDEREÇOS ATIVADOS --------------- \n')
        print (memoria)
        print ('\n ------------- ENDEREÇOS ATIVADOS --------------- \n ')

    # fase de leitura
    
    operacao = 'r'
    if operacao == 'r':
        #cria o vetor de saida
        v = np.zeros((1,col))
        o = np.zeros((1,col))

        for linha in range(len(memoria)):
            for coluna in range(len(memoria[linha])):
                if memoria[linha][coluna] == 1:
                    valor1 = v[0][coluna]
                    v[0][coluna] = valor1 + 1

                if memoria[linha][coluna] == 0:
                    valor1 = v[0][coluna]
                    v[0][coluna] = valor1 - 1

         # obtem o resultado da SDM
        print ('\n ------------- VETOR SOMADOR --------------- \n ')
        print (v)
        print ('\n ------------- VETOR SOMADOR --------------- \n ')
        for coluna in range(col):
            if v[0,coluna] >= 0:
                o[0][coluna] = 1
            if v[0][coluna] < 0:
                o[0][coluna] = 0

            
        return o



   
def main():
    
    
    matrizenderecos = np.array([[0,0,0,1,
                                 1,1,0,0,
                                 1,1,0,0,
                                 1,1,0,0],
                                
                                   
                                [1,1,0,0,
                                 1,1,0,0,
                                 1,1,0,0,
                                 1,1,0,0],

                                [1,1,0,1,
                                 1,1,0,0,
                                 1,1,0,1,
                                 0,1,0,0],

                                [1,1,1,1,
                                 1,0,0,0,
                                 1,1,0,0,
                                 0,1,0,0],

                                [0,1,0,0,
                                 0,1,0,0,
                                 1,1,0,0,
                                 1,1,0,0],
                                   
                                [1,1,1,0,
                                 1,1,1,0,
                                 1,0,0,0,
                                 1,0,0,0],

                                [0,1,0,1,
                                 1,1,0,0,
                                 0,1,0,1,
                                 1,1,1,0],

                                [1,0,0,0,
                                 1,1,0,0,
                                 1,1,0,0,
                                 1,1,0,1],

                                [1,0,0,0,
                                 1,1,0,0,
                                 1,1,1,0,
                                 0,0,0,0],

                                [1,0,0,0,
                                 1,0,0,1,
                                 1,1,1,0,
                                 0,1,0,0],

                                [1,1,1,0,
                                 1,1,0,1,
                                 1,1,1,0,
                                 1,1,0,0],

                                [1,0,0,1,
                                 0,1,1,0,
                                 1,1,0,0,
                                 1,1,0,1],

                                [1,1,0,0,
                                 1,0,0,0,
                                 0,1,1,0,
                                 1,1,0,0],

                                [1,0,1,0,
                                 0,1,1,0,
                                 1,1,0,1,
                                 0,1,1,0],                                  

                                [0,1,1,0,
                                 1,0,0,0,
                                 0,1,0,0,
                                 1,1,1,0]])                          
             
    print ('\n ------------- VETOR DE ENTRADA --------------- \n ')    
    palavra =np.array([1,1,1,1,
                       1,1,0,0,
                       0,1,0,0,
                       1,1,1,0])
   
    arr = palavra.reshape(4,4)    
    print (arr)
    exibeimagem(arr)
    print ('\n ------------- VETOR DE ENTRADA --------------- \n ')


# ============== SDM  ==================== SDM ========================

    #primeira camada, onde é carregado o valor de endereços
    matrizmemoria = primeiracamada(matrizenderecos,palavra,5)
    
    #segunda camada, parte onde é gravado na memória o conteúdo dos endereços ativados e contabilizados
    retorno = segundacamada(matrizmemoria, palavra)

# ============== SDM  ==================== SDM ========================    

    
    print ('\n ------------- VETOR DE SAÍDA --------------- \n ')
    arr = retorno.reshape(4,4)
    print (arr)
    exibeimagem(arr)    
    print ('\n ------------- VETOR DE SAÍDA --------------- \n ')




    

if __name__ == '__main__':
    main()
