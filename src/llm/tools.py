from dotenv import load_dotenv
from langchain_core.tools import tool
from woocommerce import API
import os


load_dotenv(override=True)

wc_api = API(
    url=os.getenv("wc_url"),
    consumer_key=os.getenv("consumer_key"),
    consumer_secret=os.getenv("consumer_secret"),
    wp_api=True,
    version="wc/v3",
)


@tool
def get_all_products(wcapi=wc_api) -> list:
    """get a list of all the products within the woocommerce store"""

    all_products = wcapi.get("products").json()
    products = []
    for prod in all_products:
        new_prod = {
            "id": prod["id"],
            "name": prod["name"],
            "price": prod["price"],
            "stock_quantity": prod["stock_quantity"],
            "permalink": prod["permalink"],
            "short_description": prod["short_description"],
            "tags": prod["tags"],
            "stock_status": prod["stock_status"],

        }
        products.append(new_prod)
    return products

@tool
def get_product_by_id(product_id: int, wcapi=wc_api) -> dict:
    """get a product by its id"""    
    product = wcapi.get(f"products/{product_id}").json()
    return product

@tool
def get_orders(wcapi=wc_api) -> list:
    """get a list of all the orders within the woocommerce store"""
    orders = wcapi.get("orders").json()
    return orders

@tool
def get_order_by_id(order_id: int, wcapi=wc_api) -> dict:
    """get an order by its id"""
    order = wcapi.get(f"orders/{order_id}").json()
    return order


woocommerce_tools = [
    get_all_products,
    get_product_by_id,
    get_orders,
    get_order_by_id,
]


if __name__ == "__main__":
    print(get_orders())