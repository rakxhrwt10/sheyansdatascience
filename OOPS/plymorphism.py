# Parent class
class Payment:
    def pay(self, amount):
        print("Processing payment...")


# Child class 1 (UPI)
class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI ✅")


# Child class 2 (Card)
class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card 💳")


# Child class 3 (Net Banking)
class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking 🏦")


# Function (common interface)
def make_payment(payment_method, amount):
    payment_method.pay(amount)


# Objects
p1 = UPI()
p2 = Card()
p3 = NetBanking()

# Same function, different behavior
make_payment(p1, 1000)
make_payment(p2, 2000)
make_payment(p3, 3000)