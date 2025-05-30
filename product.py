

def show_product_list(products):
    print("📦 Product List:")
    for product in products:
        print(f"{product['id']}. {product['name']} - ${product['price']} | Stock: {product['stock']}")
