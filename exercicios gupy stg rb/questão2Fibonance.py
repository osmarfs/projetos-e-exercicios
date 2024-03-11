"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""


fib = [1,1]
i = 0
num = int(input("Entre com um número: "))

while num > len(fib):
	fib.append(fib[i] + fib[i+1])
	i+=1

if num not in fib:
	print (f"O numero {num} não pertence a sequencia Fibonacci {fib}")
else:
	print(f"O numero {num} pertence a sequencia Fibonacci {fib}")