# โปรแกรมหาค่ามากสุด และ น้อยที่สุด #
for i in range(5):
      number = int(input("กรอกตัวเลขตัวที่ "+ str(i+1)+": "))
      if i == 0 :
            max = number
            min = number
      else:
            if number > max :
                  max = number
            elif number < min:
                  min = number
print("ค่ามากที่สุด คือ " ,max)
print("ค่าน้อยที่สุด คือ ", min)