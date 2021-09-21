# -*- coding: utf-8 -*-
class Point():
    #Point 객체가 만들어질 때 마다 처음에 불러지는 함수
    def __init__(self,x, y) :
    #self는 만들어진 객체 자신을 가르키는 말
        self.x = x
        self.y = y

#새 객체 만들기
p = Point(2,8)
print(p.x)
print(p.y)
