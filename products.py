products = [] # 建立專案清單
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])
print(products)

print(products[2][0])
print(products[2][1])