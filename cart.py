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

