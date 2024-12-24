### 3: การคำนวณ Postfix Expression
### จงเขียนฟังก์ชันสำหรับคำนวณผลลัพธ์ของนิพจน์ในรูปแบบ Postfix และทดสอบเรียกใช้งานโดยให้ผู้ใช้ป้อน Postfix Expression

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
# ฟังก์ชันคำนวณผลลัพธ์ Postfix Expression
def evaluate_postfix(expression):
    stack = Stack()
    # วนซ้ำแต่ละตัวในนิพจน์
    for char in expression.split():
        if char.isdigit():  # ถ้าเป็นตัวเลข
            stack.push(int(char))
        else:  # ถ้าเป็นโอเปอเรเตอร์
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2)
            elif char == '^':
                stack.push(operand1 ** operand2)

    return stack.pop()
# รับนิพจน์ Postfix จากผู้ใช้งาน
postfix_expression = input("กรุณาป้อนนิพจน์ Postfix (คั่นด้วยช่องว่าง): ")
# คำนวณผลลัพธ์
result = evaluate_postfix(postfix_expression)
# แสดงผลลัพธ์
print(f"ผลลัพธ์ของนิพจน์ Postfix '{postfix_expression}' คือ: {result}")
