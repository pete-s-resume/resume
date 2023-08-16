from email import message
from pickle import FALSE
from pythainlp import sent_tokenize, word_tokenize
# from pythainlp.word_vector import most_similar_cosmul,doesnt_match
from pythainlp.spell import correct
from pythainlp.tag import pos_tag
from pythainlp.util import emoji_to_thai,eng_to_thai,isthaichar,normalize,num_to_thaiword,thaiword_to_num


def sorting(message) :
    global others,neg
    keep = []
    word = word_tokenize(message)
    tag = pos_tag(word)
    print(word)
    count = 0
    asksize = 0
    askprize = 0
    order = 0
    dis = 0
    have =0
    others=0
    neg=False
    for i in word :
        print(tag[word.index(i)][1])
        if tag[word.index(i)][1]=="NEG" or tag[word.index(i)][1]=="ADVN":
            if tag[word.index(i)][1]=="NEG":
                neg=True
            others+=1
    for i in word :
        if i == "ไซส์" or i == "เอว" or i == "ขนาด" or i == "ยาว":
            if order>0:
                asksize=0
                break
            asksize += 1
        if i == "ราคา" or i == "บาท" or i == "มีราคา" or i == "ราคาแพง" or i == "ราคาถูก" or i == "แพง" or i == "ถูก" or i == "เท่าไหร่":
            askprize += 1
        if i == "เอา" or i == "รับ" or i == "ซื้อ":
            order += 1
        if i == "ลดราคา" or i == "ลด" or i == "โปร" or i == "ราคาถูก" or i == "ถูก":
            dis += 1
        if i == "รอ":
            if word[count+1] == "บอก":
                asksize +=1

 #============มีอะไรบ้าง==================#        
        keep = []
        for i in word:
            if i == "มี" or i == "อะไร" or i == "เสื้อ" or i =="ขาย" or i == "ไซส์":
                keep.append(i)   

        for i in word:
            if i == "มี":
                if "อะไร" in keep:
                    findk = keep.index("มี")
                    if keep[findk+1] == "อะไร":
                        have = 1
                    if "ไซส์" in keep or "เอว" in keep or "ขนาด" in keep or "ยาว" in keep:
                        asksize += 1
            if i == "สินค้า":
                have += 1
            if i == "เสื้อ":
                if "อะไร" in keep:
                    findk = keep.index("เสื้อ")
                    if keep[findk+1] == "อะไร":
                        have += 1
            if i == "ขาย":
                if "อะไร" in keep:
                    findk = keep.index("ขาย")
                    if keep[findk+1] == "อะไร":
                        have += 1


    list = [askprize,asksize,order,dis,have]
    print(list)
    for i in list:
        if max(list) == i:
            index1 = list.index(max(list))

    if max(list)==0:
        return("nothing")
    if index1==0:
        print("ask prize.")
        return("askprize")
    if index1==1:
        print("what size.")
        return("asksize")
    if index1==2:
        print("order.")
        return("order")
    if index1==3:
        print("dis")
        return("dis")
    if index1==4:
        print("have")
        return("have")
