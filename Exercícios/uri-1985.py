number_of_products = int(input())

purchase_value = 0

for i in range(number_of_products):
  purchase = input().split(' ')
  
  product_code = purchase[0]
  product_quantity = purchase[1]

  if (product_code == '1001'):
    purchase_value += 1.50 * int(product_quantity)
  elif (product_code == '1002'):
    purchase_value += 2.50 * int(product_quantity)
  elif (product_code == '1003'):
    purchase_value += 3.50 * int(product_quantity)
  elif (product_code == '1004'):
    purchase_value += 4.50 * int(product_quantity)
  elif (product_code == '1005'):
    purchase_value += 5.50 * int(product_quantity)

print('{:.2f}'.format(purchase_value))
