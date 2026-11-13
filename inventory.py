from product import Product


class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                print("Product removed successfully.")
                return

        print("Product not found.")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def display_all(self) -> None:
        print("Current Inventory")
        print("----------------------------------------")

        for product in self.__products:
            product.display_information()

        print("----------------------------------------")

    def get_all_products(self) -> list[Product]:
        return self.__products