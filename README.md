Authors: Rikellme Ellis, Dujuan Anderson, Daniel Marks 

Date Created: April 12, 2026
Course: ITT103

 Github URL to code:

# Best Buy Retail POS System

 A terminal-based Point of Sale (POS) system for managing products, shopping carts, checkout, and receipts.

### Overview
Best Buy Retail POS System is a Python application that simulates a basic retail checkout workflow. It lets a cashier view inventory, add/remove items from a cart, apply discounts and tax, process payments, print receipts, and restock items.

The program was built to demonstrate inventory management, and simple file I/O for a retail environment. All interaction happens in the terminal with menu-driven prompts.

Tech Stuff:
- Language: Python 3.8+
 Cross-platform terminal (Windows, macOS, Linux)

Features
- View available products with price and stock levels
- Add items to cart with quantity validation and stock updates
- Remove items from cart and return stock automatically
- View cart with live subtotal, discount, tax, and total calculations
- Checkout flow with payment input and change calculation
- Auto-generated text receipts saved to `/receipts` folder
- Cancel order and restore all items to inventory
- Restock products to update inventory counts
- Screen clearing for cleaner terminal UI


**2. Requirements**
No external packages needed. Requires Python 3.8 or newer.


### Usage

**Run the program**
Firstly, you will need Python or IDLE to run the code. IYou canw download Python from https://python.org

Or just download `pos_system.py` directly into a folder.

 No dependencies needed**
This program only uses Python’s built-in libraries. No `pip install` required.

### How to Run the Program

**Step 1: Open your terminal**
- Windows: Open Command Prompt or PowerShell
- macOS/Linux: Open Terminal

**Step 2: Navigate to the project folder**

Replace `path/to/` with where you saved the file.

**Step 3: Run the script**

**Step 4: Use the main menu**

You’ll see this menu:

===== Best Buy Retail POS SYSTEM =====

View Products

Start Order

Remove Item

View Cart

Checkout

Cancel Order

Restock Item

Exit

Choose (1-8):

Type a number 1-8 and press Enter to navigate.

**Step 5: Exit the program**
Select option `8` from the main menu, or press `Ctrl + C` to force quit.

### Assumptions
The program assumes the following to run correctly:
- User inputs product names matching the exact spelling and case shown in the product list. Input is converted to `.title()` so `rice` becomes `Rice`.
- All prices are in JMD and displayed with `$` symbol, but no currency conversion is performed.
- Tax rate is fixed at 10% and discount is 5% applied only when subtotal exceeds $5000.
- The user has write permissions in the current directory to create the `receipts/` folder.
- Terminal supports `cls` on Windows or `clear` on Unix systems for screen clearing.
- Only one shopping cart is active at a time. No multi-user or concurrent sessions.
- Payment is cash-based. No card processing or change validation beyond numeric input.

### Limitations
Current known limitations:
- **Data persistence**: Product list and stock reset every time the program restarts. No database or file save for inventory.
- **Product management**: Cannot add new products or change prices from the UI. Must edit code directly.
- **No input validation for names**: Typos in product names cause "Product not found" with no fuzzy matching.
- **Single currency**: All values assume JMD. No configuration for other currencies or tax rates.
- **No user accounts**: No login, roles, or sales history tracking.
- **Discount threshold**: $5000 minimum for discount is unrealistic for small retail and not configurable without code changes.
- **No unit tests**: Edge cases like negative payment, zero stock, or corrupted receipts folder are not formally tested.
- **Terminal only**: No GUI or web interface.

