

raio = float(input("Digite o valor do raio da circunferência:"))
#float para números fracionários/com valores decimais
pi = 3.1415
perimetro = 2*pi*raio
area = pi*raio**2
volume = 4/3 * pi * raio**3
#Dois asteriscos para potências

print(f"Perímetro: {perimetro:.2f}")
print(f"Área: {area:.2f}")
print(f"Volume: {volume:.2f}")
#f antes do texto para botar as variaveis juntos da string
#:.2f para arredondar os valores a apenas duas casas decimais