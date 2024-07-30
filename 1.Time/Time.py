class Time:
    def __init__(self,hour,minute,second):
        self.h=hour
        self.m=minute
        self.s=second
    def addition(self,hour,minute,second):
        self.h+=hour
        self.m+=minute
        self.s+=second
        if self.m>=60:
            self.m-=60
            self.h+=1
        if self.s>=60:
            self.s-=60
            self.m+=1
        return '{}:{}:{}'.format(self.h,self.m,self.s)
    def substraction(self,hour,minute,second):
        if self.h<hour:
            print('we can not do substraction')
        self.h-=hour
        self.m-=minute
        self.s-=second

        if self.m<0:
            self.m+=60
            self.h-=1
        if self.s<0:
            self.s+=60
            self.m-=1
        return '{}:{}:{}'.format(self.h,self.m,self.s)

T=Time(10,30,20)
add=T.addition(5,30,10)
print(add)