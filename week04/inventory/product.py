class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self._category = "เครื่องเขียน"
        self.__price = 1.0
        
        # TODO 1: ตรวจ stock ให้เป็นจำนวนเต็ม >= 0 (และไม่ใช่ bool)
        if isinstance(stock, bool) or not isinstance(stock, int) or stock < 0:
            raise ValueError("Stock ต้องเป็นจำนวนเต็มที่มากกว่าหรือเท่ากับ 0")
        self.__stock = stock
        
        # กำหนดผ่าน setter ของ price เพื่อให้ผ่านการตรวจสอบกฎ
        self.price = price

    @property
    def price(self):
        # TODO 2: คืนค่าราคาภายใน
        return self.__price

    @price.setter
    def price(self, value):
        # TODO 3: ไม่รับราคาที่ไม่ใช่ตัวเลข (int, float) หรือ <= 0 หรือเป็น bool
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("ราคาต้องเป็นตัวเลขที่มากกว่า 0")
        self.__price = float(value)

    @property
    def stock(self):
        # TODO 4: คืนค่าสต็อกภายใน (Read-only ไม่มี setter)
        return self.__stock

    @property
    def is_low_stock(self):
        # TODO 5: คืนค่า True เมื่อ stock <= 3 (ไม่มี setter)
        return self.__stock <= 3

    def sell(self, qty):
        # TODO 6: รับเฉพาะ int > 0 (ไม่รับ bool) และขายจาก __stock
        if isinstance(qty, bool) or not isinstance(qty, int) or qty <= 0:
            return False
        if qty > self.__stock:
            return False
        self.__stock -= qty
        return True

    def restock(self, qty):
        # TODO 7: รับเฉพาะ int > 0 (ไม่รับ bool) และเพิ่ม __stock
        if isinstance(qty, bool) or not isinstance(qty, int) or qty <= 0:
            return False
        self.__stock += qty
        return True

    def stock_value(self):
        return self.price * self.stock

    def show_info(self):
        status = " (สินค้าใกล้หมด!)" if self.is_low_stock else ""
        return (f"{self.name}: {self.price:.2f} บาท / "
                f"คงเหลือ {self.stock} ชิ้น{status}")