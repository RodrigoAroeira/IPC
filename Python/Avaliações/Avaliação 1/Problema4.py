def mdc(n, m): # Definindo a função mdc, que recebe dois parâmetros
    nums = [n, m] # Criando uma lista com os dois parâmetros
    nums.sort() # Ordenando a lista
    divs = [] # Criando uma lista vazia para armazenar os divisores
    for i in range(1, max(nums)): # Criando um loop que varia de 1 ao maior número da lista nums
        if n % i == 0 and m % i == 0: # Verificando se o número da lista nums é divisível por i
            divs.append(i) # Adicionando o i à lista divs
    return max(divs) # Retornando o maior número da lista divs

n = int(input("Digite o primeiro número: ")) # Recebendo o primeiro número
m = int(input("Digite o segundo número: ")) # Recebendo o segundo número
print("mdc:", mdc(n, m)) # Chamando a função mdc e imprimindo o resultado