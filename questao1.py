#1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
#Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#Imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma)

#explicação:
#enquanto K for menor que 13, indicado no índice,
#transforma k em 1, e acrescenta +1 até que a soma seja o índice. 
#Ele somará 1+2+3+4...+13, que dará 91. 
