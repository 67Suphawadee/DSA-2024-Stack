### 2.โปรแกรมแปลงเลขฐาน
### จงเขียนโปรแกรมแปลงเลขฐาน 10 ให้เป็นฐาน 2 และ ฐาน 16 โดยใช้ Stack และทดสอบเรียกใช้งานโดยรับตัวเลขฐาน 10 มาจากผู้ใช้งาน

class Stack:
    def __init__(self):
        self.stack = []
# เพิ่มข้อมูลใน Stack
    def push(self, item):
        self.stack.append(item)
 # ลบข้อมูลบนสุดจาก Stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
 # ตรวจสอบว่า Stack ว่างหรือไม่
    def is_empty(self):
        return len(self.stack) == 0
# แสดงข้อมูลใน Stack
    def display(self):
        return self.stack
# ฟังก์ชันแปลงเลขฐาน
def convert_base(number, base):
    stack = Stack()
    digits = "0123456789ABCDEF"
# ตรวจสอบกรณีเลข 0
    if number == 0:
        return "0"
# คำนวณการแปลงเลขฐาน
    while number > 0:
        remainder = number % base
        stack.push(digits[remainder])
        number //= base
# สร้างผลลัพธ์จาก Stack
    result = ""
    while not stack.is_empty():
        result += stack.pop()

    return result
# รับตัวเลขฐาน 10 จากผู้ใช้งาน
decimal_number = int(input("กรุณาใส่ตัวเลขฐาน 10: "))
# แปลงเป็นฐาน 2
binary_result = convert_base(decimal_number, 2)
# แปลงเป็นฐาน 16
hex_result = convert_base(decimal_number, 16)
# แสดงผลลัพธ์
print(f"ตัวเลข {decimal_number} ในฐาน 2 คือ: {binary_result}")
print(f"ตัวเลข {decimal_number} ในฐาน 16 คือ: {hex_result}")
