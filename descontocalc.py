price = float(input("Digite o preço:"))
percent = float(input("Digite o valor de disconto(%):"))
discount = percent / 100
totalprice = price - discount
print("Desconto:" ,percent)
print("Valor com desconto:" ,totalprice)