
# ชื่อ Class ขึ้นต้นตัว ใหญ่ ควรตั้งชื่อให้เป็นคำ นาม
class School:
     #Attribute ควรตั้งชื่อให้เป็นคำ นาม วิเศษ ความสูง กว้าง สี ขึ้นต้นตัวเล็กคำต่อไปขึ้นต้นตัวใหญ่
     schoolName = 'ลุงวิศวกรสอนคำนวณ'
     
     # Constructor
     def __init__(self, subject='python programing'):# ค่าดีฟอลซ์
          print('ให้แสดงข้อความเมื่อมีการสร้าง Instance')
          self.subject = subject

     # Method ควรตั้งชื่อให้เป็นคำ กริยา 
     def hello(self):
          print('สวัสดีตอนเช้า ยินดีต้อนรับ นักเรียนทุกคน')
     def teach(self):
          print(f'โรงเรียนนี้สอนวิชา {self.subject}')

 # ชื่อ Class ขึ้นต้นตัว ใหญ่ ควรตั้งชื่อให้เป็นคำ นาม
class Student(School):
     def __init__(self, fullname, level, scores, subject):
          super().__init__(subject)
          self.fullname = fullname
          self.level = level
          self.scores = scores
     # Method ควรตั้งชื่อให้เป็นคำ กริยา          
     def checkGrade(self):
          if self.scores >= 80:
               print(f'วิชา {self.subject} ได้เกรด A')
          elif self.scores >= 70:
               print(f'วิชา {self.subject} ได้เกรด B')
          elif self.scores >= 60:
               print(f'วิชา {self.subject} ได้เกรด C')
          elif self.scores >= 50:
               print(f'วิชา {self.subject} ได้เกรด D')
          else:
               print(f'วิชา {self.subject} ได้เกรด F')


# Instance
# school1 = School('Physics')#ถ้าไม่ใส่ค่าจะแสดง ค่า ค่าดีฟอลซ์ ออกมาแทน
# print(f'ชื่อโรงเรียน : {school1.schoolName}')
# school1.hello()
# school1.teach()
print('======================================')
student01 = Student('สมชาย สายลม', 1, 75, 'Math')
print(f'ชื่อโรงเรียน {student01.schoolName}')
print(f'ชื่อนักเรียน {student01.fullname}')
print(f'ระดับชั้น {student01.level}')
print(f'คะแนนสอบ {student01.scores}')
student01.checkGrade()
print('======================================')
student02 = Student('สมศรี สายลม', 7, 90, 'English')
print(f'ชื่อโรงเรียน {student02.schoolName}')
print(f'ชื่อนักเรียน {student02.fullname}')
print(f'ระดับชั้น {student02.level}')
print(f'คะแนนสอบ {student02.scores}')
student02.checkGrade()
print('======================================')
student03 = Student('สมปอง สายลม', 12, 49, 'programing')
print(f'ชื่อโรงเรียน {student03.schoolName}')
print(f'ชื่อนักเรียน {student03.fullname}')
print(f'ระดับชั้น {student03.level}')
print(f'คะแนนสอบ {student03.scores}')
student03.checkGrade()


