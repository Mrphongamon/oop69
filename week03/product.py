
class Product:
    category = "เครื่องเขียน"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_info(self):
        return (f"{self.name}: {self.price:.2f} บาท / "
                f"คงเหลือ {self.stock} ชิ้น")

    # 1. ขายสินค้า
    def sell(self, qty):
        if qty <= 0 or qty > self.stock:
            return False
        self.stock -= qty
        return True

    # 2. รับสินค้าเข้า
    def restock(self, qty):
        if qty <= 0:
            return False
        self.stock += qty
        return True

    # 3. คำนวณมูลค่าสินค้าคงเหลือ
    def stock_value(self):
        return self.price * self.stock
