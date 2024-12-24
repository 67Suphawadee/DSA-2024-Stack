### ส่วนที่ 5: คำนวณ Infix ด้วย Stack
### จงเขียนฟังก์ชันประเมินผลนิพจน์คณิตศาสตร์ที่อยู่ในรูป Infix โดยใช้ Stack และทดสอบการทำงานโดยป้อน infix Expression จากผู้ใช้งาน

# สร้างคลาส Stack สำหรับใช้เก็บข้อมูลใน Stack
class Stack:
    def __init__(self):
        self.stack = []  # ใช้ลิสต์ในการเก็บข้อมูล
# ฟังก์ชันสำหรับเพิ่มข้อมูลใน Stack
    def push(self, item):
        self.stack.append(item)
# ฟังก์ชันสำหรับดึงข้อมูลบนสุดจาก Stack
    def pop(self):
        return self.stack.pop() if self.stack else None  # ถ้า Stack ไม่ว่างให้ดึงข้อมูลออก
# ฟังก์ชันสำหรับดูข้อมูลบนสุดของ Stack โดยไม่ลบออก
    def peek(self):
        return self.stack[-1] if self.stack else None  # ถ้า Stack ไม่ว่างให้ดูข้อมูลบนสุด
# ฟังก์ชันสำหรับตรวจสอบลำดับความสำคัญของโอเปอเรเตอร์
def precedence(op):
    # คืนค่าลำดับความสำคัญของโอเปอเรเตอร์
    return {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}.get(op, 0)  # ถ้าไม่พบโอเปอเรเตอร์คืนค่า 0
# ฟังก์ชันแปลง Infix เป็น Postfix
def infix_to_postfix(expression):
    stack = Stack()  # สร้าง Stack สำหรับเก็บโอเปอเรเตอร์
    result = []  # เก็บผลลัพธ์ที่เป็น Postfix Expression
    for char in expression:
        if char.isdigit():  # ถ้าเป็นตัวเลขให้เพิ่มลงใน Postfix Expression
            result.append(char)
        elif char == '(':  # ถ้าพบวงเล็บเปิด '(' ให้เก็บลงใน Stack
            stack.push(char)
        elif char == ')':  # ถ้าพบวงเล็บปิด ')'
            while stack.peek() != '(':  # ดึงโอเปอเรเตอร์ออกจาก Stack จนกว่าจะเจอ '('
                result.append(stack.pop())
            stack.pop()  # ลบวงเล็บเปิด '(' ออก
        else:  # ถ้าพบโอเปอเรเตอร์
            while stack.peek() and precedence(stack.peek()) >= precedence(char):  # ถ้าโอเปอเรเตอร์ใน Stack มีลำดับความสำคัญสูงกว่า
                result.append(stack.pop())  # ดึงโอเปอเรเตอร์ออกจาก Stack
            stack.push(char)  # เก็บโอเปอเรเตอร์ใหม่ลงใน Stack

    while stack.peek():  # ดึงโอเปอเรเตอร์ที่เหลือใน Stack
        result.append(stack.pop())

    return ''.join(result)  # แปลงลิสต์ผลลัพธ์เป็นสตริงและคืนค่า
# ฟังก์ชันสำหรับคำนวณ Postfix Expression
def evaluate_postfix(expression):
    stack = Stack()  # สร้าง Stack สำหรับเก็บตัวเลข
    for char in expression:
        if char.isdigit():  # ถ้าเป็นตัวเลข
            stack.push(int(char))  # เพิ่มตัวเลขลงใน Stack
        else:  # ถ้าเป็นโอเปอเรเตอร์
            b, a = stack.pop(), stack.pop()  # ดึงตัวเลข 2 ตัวจาก Stack
            # คำนวณผลลัพธ์โดยใช้โอเปอเรเตอร์
            stack.push(eval(f"{a}{char}{b}"))  # ใช้ eval สำหรับคำนวณ

    return stack.pop()  # คืนค่าผลลัพธ์สุดท้ายจาก Stack
# ฟังก์ชันหลักสำหรับคำนวณ Infix Expression
def evaluate_infix(expression):
    postfix = infix_to_postfix(expression)  # แปลง Infix เป็น Postfix
    return evaluate_postfix(postfix)  # คำนวณผลลัพธ์จาก Postfix
# รับนิพจน์ Infix จากผู้ใช้งาน
expression = input("กรุณาป้อนนิพจน์ Infix: ")
result = evaluate_infix(expression)  # คำนวณผลลัพธ์ของ Infix Expression
print(f"ผลลัพธ์: {result}")  # แสดงผลลัพธ์
