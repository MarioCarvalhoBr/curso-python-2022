import time
tempo_incial = int(time.time())

time.sleep(3) # Sleep for 3 seconds
idade = 18
if idade >= 18:
  print("Maior de idade")
  print("Bem-vind@!")
  
if idade <	18:
  print("Menor de idade")
  print("Proibido a entrada!")

print('FIM')
tempo_final = int(time.time())
tempo_exec = tempo_final - tempo_incial
print('tempo_incial: ', tempo_incial)
print('tempo_final: ', tempo_final)
print('tempo_exec: ', tempo_exec)

