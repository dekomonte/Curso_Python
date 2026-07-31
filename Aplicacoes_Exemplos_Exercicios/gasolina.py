# Gasto para rodar y km com uma moto que faz aproximadamente 40 km/l em Brasília

km_com_um_litro = 40
preco_medio_um_litro = 6.45
km_quero_descobrir = 6.6

resposta = (preco_medio_um_litro*km_quero_descobrir)/km_com_um_litro

print(f"Seu veículo faz os {km_quero_descobrir:.2f} km com R$ {resposta:.2f}")

# Versao - interacao com usuario
km_com_um_litro = float(input("Consumo do Veiculo (km/L):"))
preco_medio_um_litro = float(input("Preço Medio Gasolina (R$):"))
km_quero_descobrir = float(input("Distancia (km):"))

resposta = (preco_medio_um_litro*km_quero_descobrir)/km_com_um_litro

print(f"Seu veículo faz os {km_quero_descobrir:.2f} km com R$ {resposta:.2f}")
