#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
#sempre será a soma dos 2 valores anteriores 
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
#escreva um programa na linguagem que desejar onde, informado um número, 
#ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o
#número informado pertence ou não a sequência.
#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de
# sua preferência ou pode ser previamente definido no código;

def pertence_fibonacci(numero):
    a, b = 0, 1
    
    while a < numero:
        a, b = b, a + b
    
    return a == numero

numero = int(input("informar número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence a sequencia")
else:
    print(f"O número {numero} não pertence a sequência")


#informado os primeiros números como a=0 e b=1, em seguida com while
#para que faça a soma dos dois últimos números da sequencia, até que a
#seja >= ao número informado no input. 
