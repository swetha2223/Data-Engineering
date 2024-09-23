# question 1. Parent -- payment class --- GetPayment method ---pass
# 2. Gpay(payment)--- Get payment --- speaking google payment gate way
# 3.Phonepay(payment)--- Get payment --- speaking phone payment gate way
# 4.Amazonpay(payment)--- Get payment --- speaking amazon payment gate way
#  with reference of  inheritanceEx1


class Payment:
    def __init__(self, name):
        self.name = name

    def GetPayment(self):
        pass

class Gpay(Payment):
    def GetPayment(self):
        return "Speaking Google Payment Gateway"

class Phonepay(Payment):
    def GetPayment(self):
        return "Speaking Phone  Payment Gateway"

class Amazonpay(Payment):
    def GetPayment(self):
        return "Speaking Amazon Payment Gateway"

gpay = Gpay("1")
phonepay = Phonepay("2")
amazonpay = Amazonpay("3")


print(f"{gpay.name} says: {gpay.GetPayment()}")
print(f"{phonepay.name} says: {phonepay.GetPayment()}")
print(f"{amazonpay.name} says: {amazonpay.GetPayment()}")




