class Stack:
    def __init__(self):
        self.stack = []
# ฟังก์ชันสำหรับเพิ่มข้อมูลใน Stack
    def push(self, item):
        self.stack.append(item)
# ฟังก์ชันสำหรับดูข้อมูลบนสุด
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
# ฟังก์ชันสำหรับลบข้อมูลบนสุด
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
# ฟังก์ชันตรวจสอบว่า Stack ว่างหรือไม่
    def is_empty(self):
        return len(self.stack) == 0
# ฟังก์ชันแสดงข้อมูลใน Stack
    def display(self):
        if not self.is_empty():
            return self.stack
        return "Stack is empty"
# ทดสอบโปรแกรม
stack = Stack()
# 1. ทดสอบการ push ข้อมูล 5 ตัว
stack.push(50)
stack.push(69)
stack.push(78)
stack.push(85)
stack.push(100)
print("หลังจาก Push 5 ตัว:", stack.display())
# 2. แสดงข้อมูลบนสุดโดยใช้ peek
print("ข้อมูลบนสุด:", stack.peek())
# 3. ทดสอบ pop ข้อมูลออก 3 ตัว
stack.pop()
stack.pop()
stack.pop()
print("หลังจาก Pop 3 ตัว:", stack.display())
# 4. แสดงข้อมูลที่เหลือใน Stack
print("ข้อมูลใน Stack ที่เหลือ:", stack.display())

