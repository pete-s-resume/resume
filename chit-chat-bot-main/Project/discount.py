from csv import reader
from pythainlp import sent_tokenize, word_tokenize
import pandas as pd
from Project import instock2

def discount(text):
    r=""
    word = word_tokenize(text)
    print("from discoint : ",instock2.recent)
    for i in word:
        print(i)
        if i == "ลดราคา":
            r = check(instock2.recent)
            return r
        if i == "ลด":
            r =check(instock2.recent)
            return r
        if i == "โปร":
            r =check(instock2.recent)
            return r

def check(q):
    print("from check : ",q)
    if q == 0:
        if instock2.asked:
            print("ได้รับส่วนลดแล้ว!\n")
            instock2.asked = False
            return("คุณลูกค้าได้รับส่วนลด 10 เปอร์เซ็นต์จากราคาทั้งหมดแล้วครับ")
        else:
            print("ยังไม่ได้สั่งเบย!\n")
            return("ตอนนี้ทางร้านมีส่วนลด 10 เปอร์เซ็นต์สำหรับลูกค้าที่ยอดสั่งสินค้าถึงราคา 500 บาทครับ")
    if q < 500:
        print("YES")
        return("ขออภัยครับ เนื่องจากยอดสั่งซื้อสินค้าไม่ถึง 500 บาท จึงไม่สามารถรับส่วนลดได้ครับ")
