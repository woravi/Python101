# Fire Station Class

class FireStation:

    def __init__(self,subject = 'งานดับเพลิง'):
        print('ระบบการสอบปฏิบัติงานดับเพลิง')
        self.subject = subject
    # Attributes
    name = 'สถานีดับเพลิง การยาสูบแห่งประเทศไทย'
    address = '123 นิคมอุตสาหกรรม โรจนะ'
    firetrucks = 3
    firefighters = 20
    firechief = 'นายวรวิทย์ โต๊ะสัมฤทธิ์'

    # Methods
    def sound_alarm(self):
        print('เสียงสัญญาณดังขึ้น!')
        
    def deploy_trucks(self):
        print(f'รถดับเพลิงจำนวน {self.firetrucks} คันไปที่เกิดเหตุ.')
        
    def send_firefighters(self):
        print(f'เจ้าหน้าที่ดับเพลิง {self.firefighters} นายไปที่เกิดเหตุ.')

class Fireman2(FireStation):
    def __init__(self,fullname, level, subject):
        super().__init__(subject)
        self.fullname = fullname
        self.level = level
     
    def check(self):
        if self.level >= 80:
            print(f'หลักสูตร {self.subject} เข้าดับไฟได้ดีมาก')
        elif self.level >= 70:
            print(f'หลักสูตร {self.subject} เข้าดับไฟได้ดี')
        elif self.level >= 60:
            print(f'หลักสูตร {self.subject} ฝึกทบทวนซ้ำ')
        elif self.level >= 50:
            print(f'หลักสูตร {self.subject} ไม่สามารถเข้าไฟได้')
        else:
            print(f'หลักสูตร {self.subject} สอบใหม่')


print('================================')
station1 = Fireman2('นายสมปอง ลุยทุ่ง',80,'การเข้าพื้นที่')
print(f'ชื่อสถานีดับเพลิง{station1.name}')
print(f'ชื่อนักดับเพลิง{station1.fullname}')
print(f'ระดับความสามารถ {station1.level}')
station1.check()
print(f'หัวหน้าสถานี {station1.firechief} ควบคุมการสอบ')
print('================================')
station2 = Fireman2('นายสุริยา ทุ่งสง',50,'เข้าประตูมีความร้อนสูง')
print(f'ชื่อสถานีดับเพลิง{station2.name}')
print(f'ชื่อนักดับเพลิง{station2.fullname}')
print(f'ระดับความสามารถ {station2.level}')
station2.check()
print(f'หัวหน้าสถานี {station2.firechief} ควบคุมการสอบ')
print('================================')
station2 = Fireman2('นายวัยวุฒย์ คล่องดี',60,'เข้าประตูมีความร้อนสูง')
print(f'ชื่อสถานีดับเพลิง{station2.name}')
print(f'ชื่อนักดับเพลิง{station2.fullname}')
print(f'ระดับความสามารถ {station2.level}')
station2.check()
print(f'หัวหน้าสถานี {station2.firechief} ควบคุมการสอบ')












