class ItemToPurchase:

    def __init__(self):
        self.item_name="None"
        self.item_price=0.00
        self.item_quantity = 0

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.total_cost():.2f}")

    def total_cost(self):
        return self.item_price*self.item_quantity
    
    


def prompt_for_item(num):
    print(f"Item {num}")
    item = ItemToPurchase()
    item.item_name = input("Enter the item name:\n")
    item.item_price = float(input("Enter the item price:\n"))
    item.item_quantity = int(input("Enter the item quantity:\n"))

    return item


def main():
    item1 = prompt_for_item(1)
    item2 = prompt_for_item(2)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"\nTotal: ${item1.total_cost()+item2.total_cost():.2f}")

if __name__ == "__main__":
    main()

