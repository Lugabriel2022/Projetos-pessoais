from datetime import date

data = date.today(); datastr = data.strftime('%d-%m-%y').replace('-', '')
senha = datastr[::-1]
while True:
    senhas = str(input('Digite sua senha: '))
    if senhas == senha:
        break
    else:
        print('Senha incorreta, dica data-1')
print('Bem vindo de volta')