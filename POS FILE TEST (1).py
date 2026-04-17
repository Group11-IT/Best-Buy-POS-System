import os
from datetime import datetime
from pathlib import Path

class POSSystem:
    def __init__(self):
        self.storename = "Best Buy Retail"
        self.tax_rate = 0.10
        self.discount_rate = 0.05
        self.discount_cost = 5000
        # Updated product list
        self.products_list = {
            "Rice": {"cost": 250, "stock": 80},
            "Milk": {"cost": 180, "stock": 50},
            "Bread": {"cost": 120, "stock": 40},
            "Eggs": {"cost": 300, "stock": 60},
            "Sugar": {"cost": 200, "stock": 90},
            "Flour": {"cost": 220, "stock": 70},
            "Cooking Oil": {"cost": 500, "stock": 45},
            "Soap": {"cost": 150, "stock": 30},
            "Toothpaste": {"cost": 350, "stock": 25},
            "Shampoo": {"cost": 600, "stock": 20},
            "Bottled Water": {"cost": 100, "stock": 120},
            "Soda": {"cost": 150, "stock": 85}
        }

        self.shopping_cart = {}

    # screen refresh
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Display the products
    def display_products(self):
        self.clear_screen()
        print(f"\nAvailable products at {self.storename}:")
        print("-" * 45)
        for item, details in self.products_list.items():
            print(f"{item:<20} Price: ${details['cost']:<6} | Stock: {details['stock']}")
        print("-" * 45)

    # Start order
    def add_to_cart(self):
        while True:
            self.clear_screen()
            print("\n===== ADD TO CART =====")
            self.display_products()

            item = input("\nEnter product name (or 'back' to return): ").strip().title()

            if item.lower() == 'back':
                break

            if item not in self.products_list:
                print("Product not found in system.")
                input("Press Enter to continue...")
                continue

            try:
                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    print("Quantity must be positive.")
                    input("Press Enter to continue...")
                    continue
            except ValueError:
                print("Invalid quantity.")
                input("Press Enter to continue...")
                continue

            if qty > self.products_list[item]["stock"]:
                print(f"Only {self.products_list[item]['stock']} left in stock.")
                input("Press Enter to continue...")
                continue

            self.shopping_cart[item] = self.shopping_cart.get(item, 0) + qty
            self.products_list[item]["stock"] -= qty
            print(f"\n✓ {qty} {item}(s) added to cart.")

            # after adding item
            while True:
                print("\nWhat next?")
                print("1. Add another item")
                print("2. Delete an item")
                print("3. View cart")
                print("4. Checkout")
                print("5. Cancel order")
                print("6. Back to main menu")

                choice = input("Choose (1-6): ").strip()

                if choice == '1':
                    break
                elif choice == '2':
                    self.remove_from_cart()
                    input("\nPress Enter to continue...")
                elif choice == '3':
                    self.view_cart()
                    input("\nPress Enter to continue...")
                elif choice == '4':
                    self.checkout()
                    return
                elif choice == '5':
                    self.cancel_order()
                    return
                elif choice == '6':
                    return
                else:
                    print("Invalid choice.")
                    input("Press Enter to continue...")

    # Cancel the current order
    def cancel_order(self):
        self.clear_screen()
        if not self.shopping_cart:
            print("\nCart is already empty.")
            return

        self.view_cart()
        confirm = input("\nCancel order and return all items to stock? (yes/no): ").lower()
        if confirm == 'yes':
            for item, qty in self.shopping_cart.items():
                self.products_list[item]["stock"] += qty
            self.shopping_cart.clear()
            print("Order canceled. All items returned to stock.")
        else:
            print("Cancel aborted.")

    # Remove item from cart
    def remove_from_cart(self):
        while True:
            self.clear_screen()
            print("\n===== REMOVE FROM CART =====")

            if not self.shopping_cart:
                print("Cart is empty. Nothing to remove.")
                input("\nPress Enter to return to main menu...")
                return

            self.view_cart()

            item = input("\nEnter product name to remove (or 'back' to return): ").strip().title()

            if item.lower() == 'back':
                break

            if item not in self.shopping_cart:
                print("Item not in cart.")
                input("Press Enter to continue...")
                continue

            try:
                qty = int(input(f"Enter quantity to remove (Max {self.shopping_cart[item]}): "))
                if qty <= 0:
                    print("Invalid quantity.")
                    input("Press Enter to continue...")
                    continue
            except ValueError:
                print("Invalid input.")
                input("Press Enter to continue...")
                continue

            if qty > self.shopping_cart[item]:
                print("You don't have that many in cart.")
                input("Press Enter to continue...")
                continue

            self.shopping_cart[item] -= qty
            self.products_list[item]["stock"] += qty

            if self.shopping_cart[item] == 0:
                del self.shopping_cart[item]

            print(f"\n✓ {qty} {item}(s) removed from cart.")

            if not self.shopping_cart:
                print("Cart is now empty.")
                input("\nPress Enter to return to main menu...")
                return

            # after removing item
            while True:
                print("\nWhat next?")
                print("1. Remove another item")
                print("2. Add an item")
                print("3. View cart")
                print("4. Checkout")
                print("5. Cancel order")
                print("6. Back to main menu")

                choice = input("Choose (1-6): ").strip()

                if choice == '1':
                    break
                elif choice == '2':
                    self.add_to_cart()
                    return
                elif choice == '3':
                    self.view_cart()
                    input("\nPress Enter to continue...")
                elif choice == '4':
                    self.checkout()
                    return
                elif choice == '5':
                    self.cancel_order()
                    return
                elif choice == '6':
                    return
                else:
                    print("Invalid choice.")
                    input("Press Enter to continue...")

    # Show current order
    def view_cart(self):
        self.clear_screen()
        if not self.shopping_cart:
            print("\nCart is empty.")
            return

        print("\n----- SHOPPING CART -----")

        # Calculate total costs
        subtotal, discount, tax, total = self.calculate_totals()

        # Show line items
        for item, qty in self.shopping_cart.items():
            price = self.products_list[item]["cost"]
            line_total = price * qty
            print(f"{item:<20} x{qty} = ${line_total:.2f}")

        print("-" * 30)
        print(f"Subtotal: ${subtotal:.2f}")

        # Only show discount line if discount is available
        if discount > 0:
            print(f"Discount ({self.discount_rate*100:.0f}%): -${discount:.2f}")
        else:
            # Show why no discount yet
            remaining = self.discount_cost - subtotal
            if remaining > 0:
                print(f"Discount: $0.00 (${remaining:.2f} away from {self.discount_rate*100:.0f}% off)")

        print(f"Tax ({self.tax_rate*100:.0f}%): ${tax:.2f}")
        print("-" * 30)
        print(f"Estimated Total: ${total:.2f}")

    # Calculate items totals cost
    def calculate_totals(self):
        subtotal = sum(self.products_list[item]["cost"] * qty for item, qty in self.shopping_cart.items())
        discount = subtotal * self.discount_rate if subtotal >= self.discount_cost else 0
        tax = (subtotal - discount) * self.tax_rate
        total = subtotal - discount + tax
        return subtotal, discount, tax, total

    # generate the receipt
    def generate_receipt(self, subtotal, discount, tax, total, payment, change):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n====== {self.storename} ===")
        print("======= RECEIPT ===========")
        print(f"Date: {now}")
        print("-" * 30)

        for item, qty in self.shopping_cart.items():
            price = self.products_list[item]["cost"]
            print(f"{item:<20} x{qty} = ${price * qty:.2f}")

        print("-" * 30)
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount: -${discount:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        print(f"Paid: ${payment:.2f}")
        print(f"Change: ${change:.2f}")
        print("Thank you for shopping")
        print("=======================\n")

    # Store receipt in a folder - WITH PERMISSION HANDLING
    def save_receipt_to_file(self, subtotal, discount, tax, total, payment, change):
        filename = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        # Try multiple locations until one works
        possible_dirs = [
            Path("receipts"), # Local receipts folder
            Path.home() / "POS_Receipts", # User's home folder
            Path.cwd() # Current directory as last resort
        ]

        filepath = None
        for folder in possible_dirs:
            try:
                folder.mkdir(exist_ok=True)
                test_path = folder / filename
                # Test if we can write here
                with open(test_path, 'w') as f:
                    pass
                filepath = test_path
                break
            except (PermissionError, OSError):
                continue

        if filepath is None:
            print("\n⚠ Could not save receipt: No write permission in any location.")
            print(" Receipt was still displayed above.")
            return

        try:
            with open(filepath, 'w') as f:
                f.write(f"========== {self.storename} ==========\n")
                f.write("============== RECEIPT ==============\n")
                f.write("\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("-" * 30 + "\n")

                for item, qty in self.shopping_cart.items():
                    price = self.products_list[item]["cost"]
                    f.write(f"{item:<20}x{qty} = ${price * qty:.2f}\n")

                f.write("-" * 30 + "\n")
                f.write(f"Subtotal: ${subtotal:.2f}\n")
                f.write(f"Discount: -${discount:.2f}\n")
                f.write(f"Tax: ${tax:.2f}\n")
                f.write(f"Total: ${total:.2f}\n")
                f.write(f"Paid: ${payment:.2f}\n")
                f.write(f"Change: ${change:.2f}\n")
                f.write("\n")
                f.write(" Thank you for shopping\n")
                f.write("\n")
                f.write("======================================\n")

            print(f"\n✓ Receipt saved to {filepath}")
        except Exception as e:
            print(f"\n⚠ Could not save receipt: {e}")
            print(" Receipt was still displayed above.")

    # Checkout
    def checkout(self):
        self.clear_screen()
        if not self.shopping_cart:
            print("Cart is empty.")
            return

        subtotal, discount, tax, total = self.calculate_totals()

        print("\n----- CHECKOUT -----")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount: -${discount:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")

        while True:
            try:
                payment = float(input("Enter payment: $"))
                if payment < total:
                    print("Not enough money.")
                else:
                    change = payment - total
                    self.generate_receipt(subtotal, discount, tax, total, payment, change)
                    self.save_receipt_to_file(subtotal, discount, tax, total, payment, change)
                    self.shopping_cart.clear()
                    break
            except ValueError:
                print("Invalid input. Enter a number.")

    def restock_item(self, item_name: str = None, qty: int = None):
        self.clear_screen()
        if item_name is None or qty is None:
            self.display_products()
            item_name = input("\nEnter product name to restock: ").strip().title()
            try:
                qty = int(input("Enter quantity to add: "))
            except ValueError:
                print("Invalid quantity. Must be a number.")
                return False

        item = item_name.strip().title()

        if item not in self.products_list:
            print(f"Error: '{item}' not found in product list.")
            return False

        if qty <= 0:
            print("Error: Restock quantity must be positive.")
            return False

        self.products_list[item]["stock"] += qty
        print(f"Restocked {qty} {item}(s). New stock: {self.products_list[item]['stock']}")
        return True

    # Main menu of the system
    def main_menu(self):
        while True:
            self.clear_screen()
            print(f"\n===== {self.storename} POS SYSTEM =====")
            print("1. View Products")
            print("2. Start Order")
            print("3. Remove Item")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Cancel Order")
            print("7. Restock Item")
            print("8. Exit")
            choice = input("Choose (1-8): ")

            if choice == '1':
                self.display_products()
            elif choice == '2':
                self.add_to_cart()
            elif choice == '3':
                self.remove_from_cart()
            elif choice == '4':
                self.view_cart()
            elif choice == '5':
                self.checkout()
            elif choice == '6':
                self.cancel_order()
            elif choice == '7':
                self.restock_item()
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again")

            input("\nPress Enter to continue...")

# Run system
if __name__ == "__main__":
    try:
        pos = POSSystem()
        pos.main_menu()
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        input("Press Enter to exit...")
