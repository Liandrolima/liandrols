n = float(input('Qual a sua velocidade?  '))
if n >=0 and n <=60:
	print('velocidade permitida')
if n >= 60.01 and n <= 80:
	x = n - 60.01
	m = x * 5
	print(f'velocidade não permitida vc excedeu em {x:.2f}km/h a velocidade permitida multa de R${m:.2f}')
if n >= 80.01 and n <= 100:
	x = n - 80.01
	m = x * 5
	print(f'velocidade não permitida vc excedeu em {x:.2f}km/h a velocidade permitida multa de R${m:.2f}')
if n >= 100.01 and n <= 200:
	x = n - 100.01
	m = x * 5
	print(f'velocidade não permitida vc excedeu em {x:.2f}km/h a velocidade permitida multa de R${m:.2f}')
if n > 201:
		print('vc esta acima de 200 km/h pare o carro vc é doido')
