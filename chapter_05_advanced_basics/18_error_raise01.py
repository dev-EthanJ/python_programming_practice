# 오류 일부러 발생시키기

class Bird:
    # 메소드 오버라이딩 강제화 위해 error raise
    def fly(self):
        raise NotImplemented

class Eagle(Bird):
    def fly(self):
        print("I'm flying.")

eagle = Eagle()
eagle.fly()