
from week03.product import Product

# สร้างรายการสินค้า
products = [
    Product("สมุด", 25.0, 10),
    Product("ปากกา", 12.0, 20),
    Product("ยางลบ", 8.0, 15),
]


# เลือกสินค้าจากหมายเลข
def choose_product():
    for i, p in enumerate(products, start=1):
        print(i, p.show_info())

    raw = input("หมายเลขสินค้า: ").strip()

    # ตรวจสอบว่าเป็นตัวเลขจำนวนเต็ม
    if not raw.isascii() or not raw.isdigit():
        return None

    index = int(raw) - 1

    # ตรวจสอบว่าหมายเลขอยู่ในช่วงสินค้า
    if index < 0 or index >= len(products):
        return None

    return products[index]


# เมนูหลัก
while True:
    print("\n===== ระบบจัดการสินค้า =====")
    print("1 = แสดงสินค้า")
    print("2 = ขายสินค้า")
    print("3 = รับสินค้าเข้า")
    print("4 = มูลค่ารวม")
    print("0 = ออก")

    menu = input("เลือกเมนู: ").strip()

    if menu == "0":
        print("จบการทำงาน")
        break

    elif menu == "1":
        for i, p in enumerate(products, start=1):
            print(i, p.show_info())

    elif menu == "2":
        p = choose_product()

        if p is None:
            print("ไม่พบสินค้า")
            continue

        raw = input("จำนวนที่ต้องการขาย: ").strip()

        if not raw.isascii() or not raw.isdigit():
            print("กรุณาป้อนจำนวนเต็มบวก")
            continue

        qty = int(raw)

        if qty <= 0:
            print("กรุณาป้อนจำนวนเต็มบวก")
        elif p.sell(qty):
            print("ขายสินค้าสำเร็จ")
            print(p.show_info())
        else:
            print("ขายไม่สำเร็จ: จำนวนสินค้าไม่เพียงพอ")

    elif menu == "3":
        p = choose_product()

        if p is None:
            print("ไม่พบสินค้า")
            continue

        raw = input("จำนวนที่ต้องการรับเข้า: ").strip()

        if not raw.isascii() or not raw.isdigit():
            print("กรุณาป้อนจำนวนเต็มบวก")
            continue

        qty = int(raw)

        if qty <= 0:
            print("กรุณาป้อนจำนวนเต็มบวก")
        elif p.restock(qty):
            print("รับสินค้าเข้าสำเร็จ")
            print(p.show_info())
        else:
            print("รับสินค้าเข้าไม่สำเร็จ")

    elif menu == "4":
        total = sum(p.stock_value() for p in products)
        print(f"มูลค่าสินค้ารวม: {total:.2f} บาท")

    else:
        print("เมนูไม่ถูกต้อง กรุณาเลือกใหม่")
