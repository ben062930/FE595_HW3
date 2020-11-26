import string
from pandas import DataFrame

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
business_name = []
business_purpose = []

docs_ = ["jiefu dong.txt",
"han luo.txt",
"zhixuan xia.txt",
"tianyi yang.txt",
"mengge geng.txt"]
print(type(docs_[0]))
for doc in docs_:
    temp_content = wrap_business(open(doc))
    business_name += temp_content[0]
    business_purpose += temp_content[1]


data = {"Business_name":business_name, "Business_purpose":business_purpose}
df = DataFrame(data)
# print(df)
