class School:
     # Attribute

     schoolName = 'การดับเพลิง'

     # Method

     def hello(self):
     	print('สวัสดีตอนเช้า ขอต้อนรับสู่โรงเรียน {self.schoolName}')

# Instance 
school01 = School()
print(school01.schoolName)
school01.hello()
