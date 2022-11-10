'''ข้อที่ 19
a = 5
b = 2
c = (a-b)
print("%.2f + %.2f = %f" %(a, b, c,))'''

'''ข้อที่ 20
a=int(input("birthday : "))
print(" >>> ฉันเกิดวันที่ %d" %a)'''

'''ข้อที่ 21 
a = int(input())
b = int(input())
c = int(a*b)
print(">>> %d เท่าของ %d มีค่าเท่ากับ %d"% (a , b, c,))'''
\
''' 

''อที่25
a= (input())
b=int(input())
c=(a*b)
print(c)'''

'''a = int(input("จำนวนที่1 :"))
b = int(input("จำนวนที่2 :"))
c = int(input("จำนวนที่3 :"))
d = (a+b+c)/3
print(d)'''

'''a = int(input("weight :"))
b = int(input("height :"))
print("weight %d height %d " %(a,b))'''

'''a = (input("Enter your first name : "))
b = (input("Enter your last name : "))
c = int(input("Enter your age:  : "))
print("Hello %s %s \nYou’re %d years old" %(a, b, c,))'''

'''หาส่วนลดสินค้า
full_price = int(input("ราคาสินค้า"))
discount = int(input("ส่วยลด"))
product_price = ((discount / 100)* full_price)
paymant = (full_price-product_price)
print("ส่วนลด %d"%product_price)
print("ราคาหลังหักส่วนลด %.2f" %paymant)'''


'''หาอุณหถูมิ C เป็น K F '''
'''C = int(input("องศาเซลเซียส"))
K = int(C+275.15)
F = int((9/5)*(C))+32
print("เควิน%d ฟาเรนฮาย%d"%(K, F))'''

'''หา พท สามเหลี่ยม'''
'''a = int(input("ค่าความสูง : "))
b = int(input("ค่าฐาน : "))
d = ((1/2)*b*a)
c = print("ค่า พท สามเหลี่ยม%.2f"%d)'''

'''a = int(input("a"))
b = int(input("b"))
addition = a+b
concatanation = str(a)+str(b)
print("addition : %d"%addition)
print("concatanation : %s"%concatanation) '''


'''ตัวอย่างโปรแกรม if / else'''
a = float(input("คะแนนสอบกลางภาค"))
b = float(input("คะแนนสอบปลายภาค"))
c = a+b
d = (a+b)/1.2 #เป็นการหาค่าเฉลี่ยจากคะแนนเต็มแปลงเป็น100คะแนน
if (a)<=60:
    print("คะแนนสอบกลางภาค = %.2f"%(a) )
else:
    print("กรุณาคำนวนคะแนนสอบใหม่กลางภาค\nเนื่องจากคะแนนเต็มมีเพียง 60 คะแนน")
if (b)<=60:
    print("คะแนนสอบปลายภาค = %.2f"%(b) )
else:
    print("กรุณาคำนวนคะแนนสอบใหม่ปลายภาค\nเนื่องจากคะแนนเต็มมีเพียง 60 คะแนน")

t = print("total = %.2f" %c)
avg = print("average = %.2f"%d) #เป็นการหาค่าเฉลี่ยจากคะแนนเต็มแปลงเป็น100คะแนน

if d >= 80:
    print("เกรดเฉลี่ย = A")
elif d >= 75:
    print("เกรดเฉลี่ย = B+")
elif d >= 70:
    print("เกรดเฉลี่ย = B")
elif d >= 65:
    print("เกรดเฉลี่ย = C+")
elif d >= 60:
    print("เกรดเฉลี่ย = C")
elif d>= 55:
    print("เกรดเฉลี่ย = D+")
elif d >= 50:
    print("เกรดเฉลี่ย = D")
else:
    print("F")