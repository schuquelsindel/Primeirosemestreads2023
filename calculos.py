valor1 = float(input("Dê um valor:"))
valor2 = float(input("Dê mais um valor:"))

if(valor2 > 0 ):
      resp1 = valor1 // valor2
      resp2 = valor1 % valor2
      resp3 = valor1 ** valor2
      print ("resposta 1:",(resp1))
      print ("resposta 2:",(resp2))
      print ("resposta 3: ", (resp3))

if(valor2 == 0):
      resp3 = 1
      print ("resposta 1: não há divisão por 0")
      print ("resposta 2: não há resto se não há divisão")
      print ("resposta 3:" , (resp3))
