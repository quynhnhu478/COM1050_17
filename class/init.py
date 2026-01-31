class TeamA:
    def __init__(self,name,age):
        self.__x=name #private nên không lấy ra trực tiếp được
        self.__y=age
    def get_name(self):#hàm lấy name ra
        return self.__x
s=TeamA("qnhu",18)
print(s.get_name()) #in ra name thông qua hàm get_name


        