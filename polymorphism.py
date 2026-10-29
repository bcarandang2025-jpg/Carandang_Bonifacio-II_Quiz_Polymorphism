class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Processing a credit card payment of ${amount:.2f}")


class DigitalWallet(PaymentMethod):
    def __init__(self):
        # Every digital wallet starts with a remaining balance of 50.00
        self.wallet_balance = 50.00

    def pay(self, amount):
        if amount > self.wallet_balance:
            print(f"Routing failed. Insufficient funds in digital wallet. (Available: ${self.wallet_balance:.2f})")
        else:
            self.wallet_balance -= amount
            print(f"Routing ${amount:.2f} through digital wallet")
            print(f"Digital Wallet Remaining Balance: ${self.wallet_balance:.2f}")


def process_checkout(payment_method, amount):
    payment_method.pay(amount)


# Menu Selection
print("===== PAYMENT GATEWAY =====")
print("1. Credit Card")
print("2. Digital Wallet")

choice = input("Choose your payment method (1 or 2): ")

if choice == "1":
    payment = CreditCard()
    print("\n===== EXECUTING CHECKOUT =====")
    process_checkout(payment, 20.00)

elif choice == "2":
    payment = DigitalWallet()
    print("\n===== EXECUTING CHECKOUT =====")
    # Deducts $20 from the wallet's internal $50 balance
    process_checkout(payment, 20.00) 

else:
    print("Invalid choice. Please select 1 or 2.")
