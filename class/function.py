class TeamA:
    def __init__(self,name,age):
        self.x=name #private nên không lấy ra trực tiếp được
        self.y=age
    def get_name(self):#hàm lấy name ra
        return self.__x
    def set_name(self,name):#hàm tự chỉnh name
        self.__x=name
s=TeamA("qnhu",18)
s.blood="B"#thêm thuộc tính 
s.set_name("quynhnhu") #chỉnh name theo ý muốn
print(s.x) #in ra name đã chỉnh thông qua hàm get_name
#cach 2: add thêm hàm ngoài vào class
def set_blood(self):
    return self.blood
TeamA.set_blood=set_blood
print(s.set_blood())