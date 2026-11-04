from week04.inventory.product import Product

print("=== สรุปผลการทดสอบกฎธุรกิจ T1–T9 ===")

# T1: สมุด ราคา 35 สต็อก 10; sell(2)
p = Product("สมุด", 35.0, 10)
res_t1 = p.sell(2)
print(f"T1 -> sell(2): {res_t1}, stock = {p.stock}")

# T2: ต่อจาก T1: sell(99)
res_t2 = p.sell(99)
print(f"T2 -> sell(99): {res_t2}, stock = {p.stock}")

# T3: ต่อจาก T2: restock(5)
res_t3 = p.restock(5)
print(f"T3 -> restock(5): {res_t3}, stock = {p.stock}")

# T4: ต่อจาก T3: price=40
p.price = 40
print(f"T4 -> price=40: price = {p.price:.0f}, value = {p.stock_value():.0f}")

# T5: ต่อจาก T4: price=-10
print("T5 -> price=-10: ", end="")
try:
    p.price = -10
except ValueError as e:
    print(f"ValueError ({e}); price ยัง = {p.price:.0f}")

# T6: กำหนด p.stock = -5
print("T6 -> p.stock = -5: ", end="")
try:
    p.stock = -5
except AttributeError:
    print(f"AttributeError; stock คงเดิม = {p.stock}")

# T7: ต่อจาก T4: sell(True), restock(2.5), sell(0)
res_sell_bool = p.sell(True)
res_restock_float = p.restock(2.5)
res_sell_zero = p.sell(0)
print(f"T7 -> sell(True): {res_sell_bool}, restock(2.5): {res_restock_float}, sell(0): {res_sell_zero}; stock ยัง = {p.stock}")

# T8: สร้างสินค้าใหม่ stock=3; ดู is_low_stock แล้ว restock(2)
p_new = Product("ปากกา", 10.0, 3)
low_before = p_new.is_low_stock
p_new.restock(2)
low_after = p_new.is_low_stock
print(f"T8 -> is_low_stock ก่อน restock: {low_before} / หลัง restock: {low_after}; stock = {p_new.stock}")

# T9: มี Product สองตัว; ขายจากตัวแรก 1 ชิ้น
p_a = Product("ยางลบ", 5.0, 10)
p_b = Product("ดินสอ", 5.0, 10)
p_a.sell(1)
print(f"T9 -> p_a.stock = {p_a.stock}, p_b.stock = {p_b.stock} (สต็อกตัวแรกเปลี่ยน สต็อกอีกตัวไม่เปลี่ยน)")