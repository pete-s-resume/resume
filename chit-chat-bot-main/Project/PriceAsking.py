# from glob import glob
from multiprocessing.connection import answer_challenge
# from pythainlp.word_vector import most_similar_cosmul
from pythainlp import word_tokenize
from Project import Sorting

price = [250,350,450,550]
ask=[]
morePrice=False

def AskPrice(text):
    global morePrice,check,what_clothes
    isCode=False
    morePrice=False
    question=0
    word = word_tokenize(text)
    print("word = ",word)

    for i in word:
        print(i)
        if i == "ไหม" or i == "มั้ย" or i == "หรือเปล่า" or i == "บ้าง" :
            question+=1
        if i == "ราคา":
            question+=1
        if i == "เท่าไหร่":
            question+=2
        if i == "กี่":
            if word[word.index(i)+1] == "บาท":
                print("กี่บาทนะ")
                question+=2
        if i == "มีราคา":
            ask.append(i)
            question+=1
        if i == "ต่ำกว่า":
            ask.append(i)
            morePrice = True
            question+=1
        if i == "ราคาแพง":
            if word[word.index(i)+1] == "กว่า":
                ask.append(i)
                ask[len(ask)-1]=ask[len(ask)-1]+"กว่า"
                morePrice = True
                question+=1
        if i == "ถูก":
            if word[word.index(i)+1] == "กว่า":
                ask.append(i)
                ask[len(ask)-1]=ask[len(ask)-1]+"กว่า"
                morePrice = True
                question+=1
        if i == "สูง":
            if word[word.index(i)+1] == "กว่า":
                ask.append(i)
                ask[len(ask)-1]=ask[len(ask)-1]+"กว่า"
                morePrice = True
                question+=1
        if i == "แพง":
            if word[word.index(i)+1] == "กว่า":
                ask.append(i)
                ask[len(ask)-1]=ask[len(ask)-1]+"กว่า"
                morePrice = True
                question+=1
        if i == "001":
            what_clothes=0
            isCode = True
        if i == "002":
            what_clothes=1
            isCode = True
        if i == "003":
            what_clothes=2
            isCode = True
        if i == "004":
            what_clothes=3
            isCode = True

    if Sorting.others > morePrice or Sorting.others > question:
        return("ขอบคุณที่ส่งข้อความมาหาเราครับ ทุกข้อความที่ได้รับ ทางเราจะนำไปปรับปรุงแก้ไขร้านค้าของเราให้ดีขึ้น :)")
    elif morePrice==True:
        ans = AnotherPrice()
        return ans
    elif question>0 :
        if not isCode:
            print("here")
            return("รบกวนคุณลูกค้าระบุรหัสสินค้าด้วยนะครับ")
        else :
            print("index = ",what_clothes)
            question = False
            return("ราคา "+str(price[what_clothes])+" บาทครับ")
    else :
        return("สวัสดีครับคุณลูกค้า สอบถามอะไรดีครับ")

def AnotherPrice():
    global morePrice,ask,what_clothes
    ans="มีราคา "
    if morePrice:
        print("in if morePrice")
        c=what_clothes
        for i in ask:
            print("in for ask")
            if i == "ต่ำกว่า" or i == "ถูกกว่า":
                c-=1
                print(what_clothes)
                if what_clothes > 0 :
                    while c >= 0 :
                        ans += str(price[c])+" "
                        c-=1
                else :
                    ask=[]
                    return("ราคาต่ำกว่านี้ไม่มีแล้วครับคุณลูกค้า")
                        
            elif i == "สูงกว่า" or i == "แพงกว่า" or i == "ราคาแพงกว่า":
                c+=1
                print("c = ",c)
                if what_clothes < len(price) :
                    while c < len(price) :
                        ans += str(price[c])+" "
                        c+=1
                else :
                    ask=[]
                    return("ราคาสูงกว่านี้ไม่มีแล้วครับคุณลูกค้า")
    else :
        for i in price:
            ans+=str(i)+" "
    ask=[]
    morePrice=False
    ans+="ครับ"
    return(ans)
