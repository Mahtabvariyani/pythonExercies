# سلام عزیزم ... پایین هر سوال  جواب و بنویس 




# اعداد بخش پذیر  بر ۷ و ضربدر ۵ رو پیدا کن بین اعداد ۱۵۰۰ تا ۲۷۰۰

li = []
for i in range (1500,1550):
    if i % 7 == 0 :
        a = i * 5 
        li.append(a)
print (li)



# برنامه ای بنویس که درجه ی هوا رو از سلسیوس به فارنهایت تبدیل کنه 

while True:
    try:
        x = float(input("hava chand daraje santigrad ast >>>> "))
        a = x*1.8+32
        print ("damaye hava {} daraje f ast".format(a))
        break
    except:print ("not number")




# برنامه ای بنویس که کامپوتر یه عددی رو انتخاب کنه  و فرد با وارد کردن عدد حدس بزنه عدد درسته یا نه 

for i in range (9):
    import random
    x=random.randint(0,10)
    try:
        if int (input("hads shoma >>> ")) == x :
            print (" woooow ok number ")
            break
        else :print ("number is error ")
    except:print("LOTFAN ADD WARED KONID")



# برنامه ای بنویس که کامپوتر از فرد کلمه ای رو بگیره و اون کلمه رو برعکس بنویسه 


while True:
    try:
        a=input("select name  >>> ")
        if a.isalpha()==True:
            b=a[::-1]
            print (b)
            break
        else :print ("name is eroor (add vared nakonid)")
    except:print()


# برنامه ای بنویس که از ۱ تا ۸ اعداد رو کامپوتر بنویسه به غیر از ۵

for i in range(1,9):
    if i == 5 :
        continue
    print(i)



