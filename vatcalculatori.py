VAT_RATE = 0.07
PACKAGING_FEE = 2.0   # ค่าบรรจุภัณฑ์ (บาท)
ADMIN_FEE = 1.5       # ค่าใช้จ่ายในการบริหารและดำเนินงาน (บาท)

# ตารางค่าจัดส่ง: ตัวเลือก -> (ชื่อขนาด, ค่าจัดส่งเป็นบาท)
SHIPPING_RATES = {
    "1": ("เล็ก", 40),
    "2": ("กลาง", 80),
    "3": ("ใหญ่", 150),
}

# รับข้อมูล (Input)
price = float(input("กรอกราคาสินค้า (บาท): "))

print("\nเลือกขนาดสินค้า:")
for key, (name, fee) in SHIPPING_RATES.items():
    print(f"  {key}. {name} (ค่าจัดส่ง {fee:,.2f} บาท)")

size_choice = input("เลือกขนาด (1-3): ").strip()
while size_choice not in SHIPPING_RATES:
    size_choice = input("กรุณาเลือก 1, 2 หรือ 3: ").strip()

size_name, shipping = SHIPPING_RATES[size_choice]

# ประมวลผล (Process)
vat = price * VAT_RATE
total = price + vat + shipping + PACKAGING_FEE + ADMIN_FEE

# แสดงผล (Output)
print("\n===== สรุปรายการชำระเงิน =====")
print(f"ราคาสินค้า: {price:,.2f} บาท")
print(f"ภาษีมูลค่าเพิ่ม 7%: {vat:,.2f} บาท")
print(f"ค่าจัดส่ง (ขนาด{size_name}): {shipping:,.2f} บาท")
print(f"ค่าบรรจุภัณฑ์: {PACKAGING_FEE:,.2f} บาท")
print(f"ค่าใช้จ่ายในการบริหารและดำเนินงาน: {ADMIN_FEE:,.2f} บาท")
print(f"ยอดรวมสุทธิ: {total:,.2f} บาท")
