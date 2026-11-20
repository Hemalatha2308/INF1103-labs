import csv

from product_factory import ProductFactory


def load_products(path, inventory, supplier):
    loaded_count = 0

    try:
        file = open(path, newline="")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row

            for row_number, row in enumerate(reader, start=2):

                # Skip empty rows
                if not row:
                    continue

                try:
                    product = ProductFactory.create(
                        product_type=row[0],
                        product_id=row[1],
                        name=row[2],
                        price=float(row[3]),
                        stock_quantity=int(row[4]),
                        supplier=supplier
                    )

                    inventory.add_product(product)
                    loaded_count += 1

                except ValueError as error:
                    print(f"Invalid row {row_number}: {error}")

        print(f"{loaded_count} products loaded.")

    finally:
        print("Load attempt finished.")