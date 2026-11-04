from week04.inventory.product import Product

def main():
    # สร้างสินค้าเริ่มต้น
    products = [
        Product("สมุด", 25.0, 10),
        Product("ปากกา", 12.0, 2), # สต็อกน้อยกว่าหรือเท่ากับ 3 จะแสดงสถานะเตือน
        Product("ยางลบ", 8.0, 15),
    ]

    while True:
        print("\n--- ระบบจัดการสินค้า ---")
        for i, p in enumerate(products):
            print(f"{i + 1}. {p.show_info()}")
        
        print("\n[1] ขายสินค้า  [2] รับสินค้าเข้า  [3] ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1-3): ")

        if choice == "1":
            idx = int(input("เลือก Index สินค้า (1-3): ")) - 1
            qty = int(input("จำนวนที่ต้องการขาย: "))
            if products[idx].sell(qty):
                print("-> ขายสำเร็จ!")
            else:
                print("-> ขายไม่สำเร็จ (จำนวนไม่ถูกต้องหรือสินค้าไม่พอ)")
                
        elif choice == "2":
            idx = int(input("เลือก Index สินค้า (1-3): ")) - 1
            qty = int(input("จำนวนที่ต้องการรับเข้า: "))
            if products[idx].restock(qty):
                print("-> รับสินค้าเข้าสำเร็จ!")
            else:
                print("-> รับสินค้าเข้าไม่สำเร็จ (จำนวนต้องมากกว่า 0)")
                
        elif choice == "3":
            print("ออกจากระบบ...")
            break
        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง")

if __name__ == "__main__":
    main()