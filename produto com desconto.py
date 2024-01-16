produto = float(input('digite o preço'))
desconto = produto * 0.05
pagar = produto - desconto

print(f'o valor normal do produto é R${produto:.2f} mas com desconto de 5% vocé ganha R${desconto:.2f} e pagará apenas R${pagar:.2f}')

produto = float(input('digite o preço'))

if produto < 199.99:
	print('sem desconto')

elif produto >=200 and produto <=300:
	desconto = produto * 15/100
	pagar = produto - desconto

	print(f'o valor normal do produto é:  R${produto:.2f} mas com desconto de 15% vocé ganha:  R${desconto:.2f} de desconto e pagará apenas:  R${pagar:.2f}')
	
elif produto >=301 and produto <=2000:
	desconto = produto * 10/100
	pagar = produto - desconto
	print(f'o valor normal do produto é:  R${produto:.2f} mas com desconto de 10% vocé ganha:  R${desconto:.2f} de desconto e pagará apenas:  R${pagar:.2f}')
	
elif produto >=2001 and produto <=5000:
	desconto = produto * 5/100
	pagar = produto - desconto
	print(f'o valor normal do produto é:  R${produto:.2f} mas com desconto de 5% vocé ganha:  R${desconto:.2f} de desconto e pagará apenas:  R${pagar:.2f}')
else:
	print('Chamar Gerente')
