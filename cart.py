def add_cart(cart):
    product_id = int(input("Qo'shmoqchi bo'lgan product idsimi kiriting: "))
    cart.append(product_id)
    print("Mahsulot savatchangizga muvaffaqiyatli qoshildi.")

def show_cart(cart, products):
    if len(cart) == 0:
        print("Sizning davatchangiz bosh")
    else:
        print("📦 Sizning savatchangiz:")
        for product in products:
            if product['id'] in cart:
                print(f"{product['id']}. {product['name']} - ${product['price']} | Stock: {product['stock']}")
                
def remove_product(cart,products):
    product_id=int(input('olib tashlamoqchi bo'lgan mahsulot ID sini kiriting:'))
    if product-id in cart:
       cart.remove(product-id)
       print(f'ID{product_id} olib tashlandi.')
    else:
       print('bu mahsulot savatda yo'q.')
def show_check(cart,products):
    total=o
    print("------Check menusi---------")
    for product_id in cart:
        for product in products:
            if product['id]==product_id:
               print(f'-{product['name']}-${product['price']}')
               total+=product['price]
               print('---umumiy narx-----------')
               print(total)
    
    
    


