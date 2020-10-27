import string

def wrap_business(hw):
    result = list()
    for line in hw.readlines():
        for c in line:
            #remove unnecessary punctuation
            if (c in string.punctuation) and (c != "-"):
                line = line.replace(c, " ")
                line = line.strip()
        result.append(line)
    #print(result)
    name = list()
    purpose = list()
    for i in result:
        #find business names
        if i[0] == "N":
            a = i[5:]
            a = a.strip()
            name.append(a)
        #find business purpose
        elif i[0] == "P":
            b = i[8:]
            b = b.strip()
            purpose.append(b)
    return(name,purpose)

# open files downloaded from the discussion board
jd = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/jiefu dong.txt")
hl = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/han luo.txt")
zxx = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/zhixuan xia.txt")
tyy = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/tianyi yang.txt")
mgg = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/mengge geng.txt")
content1 = wrap_business(jd)
content2 = wrap_business(hl)
content3 = wrap_business(zxx)
content4 = wrap_business(tyy)
content5 = wrap_business(mgg)
business_name = content1[0] + content2[0] + content3[0] + content4[0] + content5[0]
business_purpose = content1[1] + content2[1] + content3[1] + content4[1] + content5[1]