class Product:
    # เพิ่ม Class Attribute ตรงนี้ตามโจทย์งานที่ 4
    category = "เครื่องเขียน"
    pass

p1 = Product()
p2 = Product()

p1.name = "สมุด"
p1.price = 25.0
p2.name = "ปากกา"
p2.price = 12.0

print(f"{p1.name}: {p1.price:.2f} บาท")
print(f"{p2.name}: {p2.price:.2f} บาท")

# ส่วนทดสอบการแก้ไขค่า (งานที่ 3)
p1.price = 30.0
print("ราคา p1 หลังแก้:", p1.price)
print("ราคา p2 หลังแก้:", p2.price)

# เพิ่มส่วนทดสอบอ่านค่า category (งานที่ 4)
print("จากชื่อ Class:", Product.category)
print("จาก p1:", p1.category)
print("จาก p2:", p2.category)