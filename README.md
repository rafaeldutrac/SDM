# SDM
SDM -Sparse Distributed Memory - Rede Neural sem peso

Memória distribuída esparsa (SDM) é um modelo matemático correlacionado com a memória de longo prazo introduzido por Pentti Kanerva em 1988, enquanto ele estava na NASA Ames Research Center . É uma memória de acesso aleatório (RAM)generalizada. 

Estas palavras(endereços, ou sequência de bits) servem como endereços de dados para a memória. O principal atributo da memória é a sensibilidade à semelhança( no caso, Hamming ), o que significa que uma palavra pode ser lida para trás não só dando o endereço de escrita original, mas também, dando uma perto dele, medida pelo número de bits incompatíveis (isto é, a distância de Hamming entre endereços de memória ).

SDM implementa a transformação do espaço lógico em espaço físico usando armazenamento de dados distribuídos. Um valor que corresponde a um endereço lógico é armazenado em vários endereços físicos. Este modo de armazenamento é robusto e não determinística. A célula de memória não é abordada diretamente. Se os dados de entrada (endereços lógicos) estiverem parcialmente danificados(ruídos), os nós ainda podem obter dados de saída corretos.
