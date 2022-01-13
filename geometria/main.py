import geometria as g
import emoji
n = "Mario"
s = "Carvalho"
nc = n +" "+ s
opcao = int(input("Selecione uma figura:\n" + emoji.emojize('1.Círculo :red_circle:') + "\n"+emoji.emojize('2.Quadrado :red_square:')+"\nOpção: "))
if opcao == 1:
    raio = float(input("Digite o raio: "))
    area = g.area_circulo(raio)
    print(f"O círculo de raio {raio} tem área: {area}")
elif opcao == 2:
    lado = float(input("Digite o lado: "))
    area = g.area_quadrado(lado)
    print(f"O quadrado de lado {lado} tem área: {area}")
else:
    print("Opção inválida!")
