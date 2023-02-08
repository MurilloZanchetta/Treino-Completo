peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura?'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc< 17:
 print('Você está Muito abaixo do peso')
elif 17<= imc < 18.5:
 print('Você está Abaixo do peso')
elif 18.5<= imc < 25:
 print('PARABÉNS, Você está no seu Peso Normal')
elif 25<= imc < 30:
 print('Você está Acima do peso')
elif 30<= imc < 35:
 print('Você está em Obesidade I')
elif 35<= imc < 40:
 print('Cuidado, Você está em Obesidade II (severa)')
elif imc >= 40:
 print('Você está em Obesidade III (mórbida), Muito preocupante')
