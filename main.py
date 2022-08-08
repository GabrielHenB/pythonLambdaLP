lista = [1, -2, 4, -3, -4, -5, 2, 100, -30, 0, 0];
lista2 = [0 , 0 , 1, 0, 0]

def verifica(li):
  positivos = 0;
  negativos = 0;
  zeros = 0;
  for i in filter(lambda n: n>0, li): positivos += 1;
  for i in filter(lambda n: n<0, li): negativos += 1;
  for i in filter(lambda n: n==0, li): zeros += 1;
  positivos = (positivos * 100) / len(li);
  negativos = (negativos * 100) / len(li);
  zeros = (zeros * 100) / len(li);

  print("Positivos: {0} %".format(positivos));
  print("Negativos: {0} %".format(negativos));
  print("Zeros: {0} %".format(zeros));

print("VERIFICANDO LISTA 1:");
verifica(lista);
print("VERIFICANDO LISTA 2: ");
verifica(lista2);