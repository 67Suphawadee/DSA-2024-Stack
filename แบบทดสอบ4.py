### 4: การตรวจสอบ JSON string
### จงเขียนโปรแกรมตรวจสอบความถูกต้องของ JSON string โดยใช้ Stack และทดสอบเรียกใช้งานโดยให้ผู้ใช้งานป้อน JSON string

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
# ฟังก์ชันตรวจสอบความถูกต้องของ JSON string
def is_valid_json(json_string):
    stack = Stack()
# สัญลักษณ์เปิดและปิดที่ต้องตรวจสอบ
    matching = {"}": "{", "]": "[", '"': '"'}
    in_quote = False  # ตัวแปรตรวจสอบว่าอยู่ในเครื่องหมายคำพูดหรือไม่

    for ch in json_string:
        if ch == '"':  # จัดการเครื่องหมายคำพูด
            if not in_quote:
                stack.push(ch)  # เปิดคำพูด
                in_quote = True
            else:
                if stack.is_empty() or stack.pop() != '"':  # ปิดคำพูด
                    return False
                in_quote = False
        elif ch in "{[":
            stack.push(ch)  # เก็บสัญลักษณ์เปิด
        elif ch in "}]":
            if stack.is_empty() or stack.pop() != matching[ch]:
                return False

    return stack.is_empty() and not in_quote
# รับ JSON string จากผู้ใช้งาน
json_string = input("กรุณาป้อน JSON string ที่ต้องการตรวจสอบ: ")
# ตรวจสอบความถูกต้อง
if is_valid_json(json_string):
    print("JSON string ถูกต้อง")
else:
    print("JSON string ไม่ถูกต้อง")