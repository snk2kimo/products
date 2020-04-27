# 查詢檔案是否存在
import os # 載入 os 模組

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 跳到下一個迴圈
			name, price = line.strip().split(',') # 將line去調換行符號(strip).去掉逗號(split)後存入name, price兩個清單內
			products.append([name, price])
	return products

# 記帳程式專案 - 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱： ')
		if name == 'q':
			break
		price = input('請輸入價格： ')
		products.append([name, price])
	print(products)
	return products

# 印出所有商品跟價格
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

# 主程式function，一般都取名為main
def main(filename):
	if os.path.isfile(filename): # 檢查檔案在不在
		print('Yeah!找到檔案了!')
		products = read_file(filename)
		print(products)
	else:
		print('找不到檔案.....')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main('products.csv')