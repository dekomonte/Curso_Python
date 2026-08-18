# Horários para tomar remédio - script mais tosco e menos robusto possível
from datetime import date

# ["nome do remedio", primeiro horario, intervalo]
remedios = [
    ["Ibuprofeno", 8, 8],
    ["Dipirona", 8, 6],
    ["Ondansetrona", 8, 8],
    ["Buscopan", 8, 12]
]

#Data no padrão BR
data = date.today()
data = data.strftime("%d/%m/%Y")

# print(f"===== Medicamentos =====")
print(f"===== Medicamentos - {data} =====")
for remedio in remedios:
    print("->",remedio[0])
    hora = remedio[1]
    intervalo = remedio[2]
    while hora < 24:
        print(f"{hora}:00")
        hora = hora+intervalo
    if hora == 24:
        print(f"00:00")
    #print("\n")
