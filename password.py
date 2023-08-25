import random
import string


# 첫번째 비밀번호 만들기, 원하는 조건에 맞는
### 규칙 ####
# 1. 영어가 있는지 확인
# 2. 숫자가 있는지 확인
# 3. 특수문자

# 두번쨰 랜덤 비밀번호 생성



punctuation = string.punctuation
ascii_letters = string.ascii_letters
digits = string.digits



def checkLet(str1:str):
    count = 0

    for i in str1:             
        if (ascii_letters.find(i)) > 0:
            count += 1

    
    if(count ==0):
        print ("비밀번호에 영어가 하나는 필요합니다")
        return False
    return True

def checkDigit(str1:str):

    count = 0

    for i in str1:             
        if (digits.find(i)) > 0:
            count += 1
    
    if(count ==0):
        print ("비밀번호에 숫자가 하나는 필요합니다")
        return False
    return True
def checkPunctuation(str1:str):

    count = 0

    for i in str1:             
        if (punctuation.find(i)) > 0:
            count += 1
            

    if(count ==0):
        print ("비밀번호에 특수문자 하나는 필요합니다")
        return False
    return True


if __name__ == '__main__':
   
    isLet = False
    isDit = False
    isPun = False
  


    print("main!!")

    passWord = input("password : ")
    isLet = checkLet(passWord)
    isDit = checkDigit(passWord)
    isPun = checkPunctuation(passWord)

    if (isLet & isDit & isPun):
        print("비밀번호 규칙에 알맞습니다")
    else:
        print("비밀번호를 다시 입력해주세요")



