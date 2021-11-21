# Preenchimento de Vetor III

# Leia um valor X. Coloque este valor na primeira posição de um vetor N[100].
# Em cada posição subsequente de N (1 até 99), coloque a metade do valor
# armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor N.

# •	Entrada

# A entrada contém um valor de dupla precisão com 4 casas decimais.

# •	Saída

# Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor
# e Y é o valor armazenado naquela posição. Cada valor do vetor deve ser
# apresentado com 4 casas decimais.


x = float(input())
for i in range(0, 100):
	# .format é um método de strings e ele que faz aparecer a variável no lugar dos {}. 
	# As {} são substituídas pelos argumentos fornecidos ao método na ordem em que aparecem.
	# end = '' na declaração print ("\ t", end = '') Essa é a função para imprimir todos os valores em uma lista aninhada
    print("N[{}] = ".format(i), end='')
    print('{0:.4f}'.format(x))
    x /= 2
