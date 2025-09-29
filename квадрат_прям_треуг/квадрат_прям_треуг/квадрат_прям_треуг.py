from tkinter.tix import Tree


print("Triangle")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print("Square")
d = int(input("d: "))
print("rectangle")
e = int(input("e: "))
f = int(input("f: "))

class form:
    def __init__(self, a, b, c, d, e, f):
        self.funk = {
         "1" : area_triangle,
         "2" : area_square,
         "3" : area_rectangle
                  }
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    
    def area_triangle(self):
        s_tria = (self.a + self.b + self.c) / 2
        return (s_tria * (s_tria - self.a) * (s_tria - self.b) * (s_tria - self.c)) ** 0.5
        

    def area_square(self):
        p_squa=self.d*4
        s_squa=self.d*self.d
        return(p_squa)
        
    
    def area_rectangle(self):
        p_rect=(self.e+self.f)*2
        s_rect=self.e*self.f
        return(p_rect)

    def choice():
        choi = input("input 1, 2 elif 3: ")

        if choi == "1":
            self.area_triangle()
        elif choi == "2":
            area_square(self)
        elif choi == "3":
            area_rectangle(self)
        
# Создание объекта и вычисление площади
forms = form(a, b, c, d, e, f)
print("triangle")
print("s:", forms.area_triangle())
print("square")
print("s:", forms.area_square())
print("rectangle")
print("s:", forms.area_rectangle())