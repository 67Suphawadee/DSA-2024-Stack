### 1.โปรแกรมกลับลำดับตัวอักษร
### จงเขียนโปรแกรมกลับลำดับตัวอักษรในข้อความโดยใช้ Stack (รับข้อความมาจากผู้ใช้งาน)
class Stack:
    def __init__(self):
        self.stack = []
# ฟังก์ชันสำหรับเพิ่มข้อมูลใน Stack
    def push(self, item):
        self.stack.append(item)
# ฟังก์ชันสำหรับลบข้อมูลบนสุดของ Stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
# ฟังก์ชันตรวจสอบว่า Stack ว่างหรือไม่
    def is_empty(self):
        return len(self.stack) == 0
# ฟังก์ชันสำหรับกลับลำดับตัวอักษร
def reverse_string(input_string):
    stack = Stack()
 # ดันตัวอักษรแต่ละตัวลงใน Stack
    for char in input_string:
        stack.push(char)
# ดึงตัวอักษรออกจาก Stack และสร้างข้อความใหม่
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string
# รับข้อความจากผู้ใช้งาน
user_input = input("กรุณาใส่ข้อความที่ต้องการกลับลำดับ: ")
# เรียกใช้งานฟังก์ชันกลับลำดับตัวอักษร
result = reverse_string(user_input)
# แสดงผลลัพธ์
print("ข้อความหลังจากกลับลำดับ:", result)
