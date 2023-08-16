from calendar import c
from csv import reader
from os import remove
from tkinter import N
from cv2 import multiply
import pandas as pd
from pathy import register_client
from pythainlp import sent_tokenize, word_tokenize
from pythainlp.tag import pos_tag
from Project import Sorting
from pythainlp.util import emoji_to_thai,eng_to_thai,isthaichar,normalize,num_to_thaiword,thaiword_to_num,isthaichar,isthai



def CheckStock(x,y,n):
    location = 'C:/Users/NANTANUT WATHANAKUL/Desktop/Expo/Test/demo.xlsx'
    reader = pd.read_excel(location,sheet_name='Sheet1')
    result=""
    s = ['S','M','L','XL']
    r = reader[s[x]][y]
    print("read ",s[x]," ",y)
    if r == 0:
        result+=("ขออภัยครับ สินค้ารหัส "+name+" ไซส์ "+s[x]+" หมดครับลูกค้า")
        return(result,0)
    else:
        if int(r)-n < 0:
            result+="ขออภัยครับคุณลูกค้า รหัสสินค้า "+name+" ไซส์ "+s[x]+" ในสต็อกสินค้ามีจำนวนไม่พอสำหรับการสั่งซื้อครับ\n"
            result+="ตอนนี้ในสต็อกมี "+str(r)+" ตัวครับ T_T\n"
            return(result,0)
        else:
            result+="สินค้ารหัส "+name+"ไซส์ "+s[x]+" มีสินค้าครับ\n"
            return(result,1)

def keep_total(x,y):
    global recent,asked
    recent=x
    asked=y

def finish(text):
    print("====== finish ======\n\n")
    global total,name,ans
    location = 'C:/Users/NANTANUT WATHANAKUL/Desktop/Expo/Test/demo.xlsx'
    reader = pd.read_excel(location,sheet_name='Sheet1')
    stock_001_s = reader['S'][0];   stock_002_s = reader['S'][1];   stock_003_s = reader['S'][2];   stock_004_s = reader['S'][3]
    stock_001_m = reader['M'][0];   stock_002_m = reader['M'][1];   stock_003_m = reader['M'][2];   stock_004_m = reader['M'][3]
    stock_001_l = reader['L'][0];   stock_002_l = reader['L'][1];   stock_003_l = reader['L'][2];   stock_004_l = reader['L'][3]
    stock_001_xl = reader['XL'][0]; stock_002_xl = reader['XL'][1]; stock_003_xl = reader['XL'][2]; stock_004_xl = reader['XL'][3]

    total=0
    ans=""
    check1=False
    check2=False
    check3=False
    price = [250,350,450,550]
    keep = []
    quantity = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
    word = word_tokenize(text)
    for i in word:
        if i == " ":
            word.remove(i)
    print(word)
    tag = pos_tag(word)
    print(tag)

    if Sorting.neg:
        return("ขอบคุณที่ส่งข้อความมาหาเราครับ ทุกข้อความที่ได้รับ ทางเราจะนำไปปรับปรุงแก้ไขร้านค้าของเราให้ดีขึ้น :)")

    for i in word:
        print("'%s'"%i)
        try:
            if i == "001" or i == "002" or i == "003" or i == "004":
                print("in")
                code=int(i)-1
                name=i
                keep.append(i)
                check1=True
            else:
                try:
                    num = thaiword_to_num(i)
                except:
                    num = int(i)
                check2=True
                print("num = ",num)
        except:
            if i.upper() == "S":
                size = 0
                check3=True
            elif i.upper() == "M":
                size = 1
                check3=True
            elif i.upper() == "L":
                size = 2
                check3=True
            elif i.upper() == "XL":
                print("in XL")
                size = 3
                check3=True
        print("check = ",check1,check2,check3)
        t = tag[word.index(i)][1]
        infer = check1 and check2 and check3
        # i=="/" or i=="," or t == "JCRG" or t == "RPRE" or 
        if infer:
            if not(check1 and check2 and check3):
                return("กรุณาระบุรหัส ไซส์ และจำนวนสินค้าด้วยครับ")
            print("t = ",t)
            print("size = ",size)
            print("code = ",code)
            x,y = CheckStock(size,code,num)
            ans+=x
            if y == 0:
                return ans
            print("size[%d][%d] = %d" %(size,code,num))
            quantity[size][code] = num
            check1=False
            check2=False
            check3=False

    print("124 : num = ",num)
    if check1 or check2 or check3:
        return("กรุณาระบุรหัส ไซส์ และจำนวนสินค้าด้วยครับ")
    # x,y = CheckStock(size,code,num)
    # ans+=x
    # print("size[%d][%d] = %d" %(size,code,num))
    # quantity[size][code] = num
    # if y == 0:
    #     return ans
    
    stock_001_s -= quantity[0][0];  stock_002_s -= quantity[0][1];  stock_003_s -= quantity[0][2];  stock_004_s -= quantity[0][3]
    stock_001_m -= quantity[1][0];  stock_002_m -= quantity[1][1];  stock_003_m -= quantity[1][2];  stock_004_m -= quantity[1][3]
    stock_001_l -= quantity[2][0];  stock_002_l -= quantity[2][1];  stock_003_l -= quantity[2][2];  stock_004_l -= quantity[2][3]
    stock_001_xl -= quantity[3][0]; stock_002_xl -= quantity[3][1];  stock_003_xl -= quantity[3][2];  stock_004_xl -= quantity[3][3]
    
    df = pd.DataFrame({'Name': ['001', '002', '003', '004'],
                    'S': [stock_001_s,stock_002_s,stock_003_s,stock_004_s],
                    'M': [stock_001_m,stock_002_m,stock_003_m,stock_004_m],
                    'L': [stock_001_l,stock_002_l,stock_003_l,stock_004_l],
                    'XL': [stock_001_xl,stock_002_xl,stock_003_xl,stock_004_xl]})
    writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
        
    print(quantity)
    ans+="\nขออนุญาตรวมยอดนะครับ\n"
    w = ""
    for i in keep:
        code = int(i)-1
        sum = quantity[0][code]+quantity[1][code]+quantity[2][code]+quantity[3][code]
        total+=price[code]*(sum)
        if w!=i:
            ans+="รหัสสินค้า "+i+" ราคา "+str(price[code])+" บาท จำนวน "+str(sum)+" ตัว\n"
        w=i
    ans+="ราคาทั้งหมด "+str(total)+" บาทครับ"
    if total >= 500:
        new_total = total-(total/10)
        ans+="\nเนื่องจากลูกค้าซื้อสินค้ามากกว่า 500 บาท ทางร้านมีส่วนลดให้ 10 เปอร์เซ็นต์ครับ"
        ans+="\nรวมราคาทั้งหมดจาก "+str(total)+" ลดเหลือ "+str(int(new_total))+" บาท"
        keep_total(0,True)
    ans+="\nขอบพระคุณที่อุดหนุนร้านค้าของเราครับ :)"
    keep_total(int(total),True)
    total=0
    return(ans)



        
