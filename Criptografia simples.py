alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
mensagemcripto = []

pal = str(input('Insira a palavra a ser criptografada: ')).lower()
pal = pal.replace(' ', '')
mensagem = list(pal)

for c in mensagem:
    l = alfabeto.index(c)
    l += 1
    mensagemcripto.append(str(l))

resultado = ''.join(mensagemcripto)
resultado = resultado.replace(' ', '')

print(resultado)
