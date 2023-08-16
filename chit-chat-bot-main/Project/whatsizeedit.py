from tabnanny import check
from pythainlp import sent_tokenize, word_tokenize
import pandas as pd

from Project.instock2 import CheckStock

# text = "001 ไซส์เท่าไหร่"
#print(word)
# count = 0
# num = []

# stock = [[0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]]

# size = ['S','M','L','XL']
# stock1 = ['','','','']
# stock2 = ['','','','']
# stock3 = ['','','','']
# stock4 = ['','','','']
# keep = []
# ans = ""

#================================================================================================================================================================================#

def checkk(number):
    stock = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

    size = ['S','M','L','XL']
    stock1 = ['','','','']
    stock2 = ['','','','']
    stock3 = ['','','','']
    stock4 = ['','','','']
    
    location = 'C:/Users/User/Desktop/PP/demo.xlsx'
    reader = pd.read_excel(location)
    stock[0][0] = reader['S'][0];   stock[1][0] = reader['S'][1];   stock[2][0] = reader['S'][2];   stock[3][0] = reader['S'][3]#s 001,002,003,004
    stock[0][1] = reader['M'][0];   stock[1][1] = reader['M'][1];   stock[2][1] = reader['M'][2];   stock[3][1] = reader['M'][3]#m 001,002,003,004
    stock[0][2] = reader['L'][0];   stock[1][2] = reader['L'][1];   stock[2][2] = reader['L'][2];   stock[3][2] = reader['L'][3]#l 001,002,003,004
    stock[0][3] = reader['XL'][0]; stock[1][3] = reader['XL'][1]; stock[2][3] = reader['XL'][2]; stock[3][3]= reader['XL'][3]#xl 001,002,003,004

    
    if number == "001":
        for i in range(4):
            if stock[0][i] > 0:
                stock1[i] = size[i]
        return stock1

    if number == "002":
        for i in range(4):
            if stock[1][i] > 0:
                stock2[i] = size[i]
        return stock2

    if number == "003":
        for i in range(4):
            if stock[2][i] > 0:
                stock3[i] = size[i]
        return stock3

    if number == "004":
        for i in range(4):
            if stock[3][i] > 0:
                stock4[i] = size[i]
        return stock4

#================================================================================================================================================================================#    
def whatsize(text):

    num = []
    keep = []
    ans = ""
    count = 0
    checks=0

    word = word_tokenize(text)
    for i in word:
        if i == "ไซส์" or i == "ขนาด" or i == "อก" or i == "เอว" or i == "ยาว":
            keep.append(i)

        if i == "001" or i == "002" or i == "003" or i == "004":
            num.append(i)
        
    if "001" not in num and "002" not in num and "003" not in num and "004" not in num:
        return("หากคุณลูกค้าต้องการทราบรายละเอียดของเสื้อแต่ละตัว\nรบกวนระบุรหัสสินค้าก่อนถามไซส์นะครับ\nตย. 001 ไซส์เท่าไหร่ครับ")

    if "001" in num:
        stock1 = checkk("001")
        if 'S' in stock1 or 'M' in stock1 or 'L' in stock1 or 'XL' in stock1:
            ans += "001 มีไซส์ "
        for i in stock1:
            if i != "":
                count +=1
                ans += i+" "
                if count == 4:
                    checks+=1
                    continue
        count = 0
                
    if "002" in num:
        stock2 = checkk("002")
        if 'S' in stock2 or 'M' in stock2 or 'L' in stock2 or 'XL' in stock2:
            ans += "002 มีไซส์ "
        for i in stock2:
            if i != "":
                count +=1
                ans += i+" "
                if count == 4:
                    checks+=1
                    continue
        count = 0

    if "003" in num:
        stock3 = checkk("003")
        if 'S' in stock3 or 'M' in stock3 or 'L' in stock3 or 'XL' in stock3:
            ans += "003 มีไซส์ "
        for i in stock3:
            if i != "":
                count +=1
                ans += i+" "
                if count == 4:
                    checks+=1
                    continue
        count = 0

    if "004" in num:
        stock4 = checkk ("004")
        if 'S' in stock4 or 'M' in stock4 or 'L' in stock4 or 'XL' in stock4:
            ans += "004 มีไซส์ "
        for i in stock4:
            if i != "":
                count +=1
                ans += i+" "
                if count == 4:
                    check+=1
                    continue
        count = 0

    if "001" in num or "002" in num or "003" in num or "004" in num:
        if ans == "":
            ans += "หมดแล้ว"
        if checks < len(num) and checks != len(num) and checks != 0:
            ans += "นอกนั้นหมดแล้ว" 
        ans += "ครับ"
        
    if len(keep) > 0:
        return(ans)
