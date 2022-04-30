from PIL import Image
from pytesseract import *
import sys
import time
pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract'

print("실행 프로그램과 이미지는 같은 공간에 있어야 합니다\n")
print("파일명은 [img1.jpg] 의 양식을 지켜야 합니다\n")
print("이미지별 인덱스는 시작값이 몇이든 상관없지만 순서대로 이어져야 합니다\n")

print("시작 파일과 끝 파일의 인덱스 입력 img1 ~ img 6 Ex) 1 6 : ", end="")
a, b = map(int,sys.stdin.readline().split())
b +=1


for i in range(a,b):
    filename = f"1 ({i}).jpg"

    image = Image.open(filename)
    text = image_to_string(image, lang='eng')
    f = open(f"1 ({i}).txt", 'w',encoding='UTF-8')
    f.write(text)
    f.close()
    
for i in range(5):
    print("자동 생성 완료 {}초 후 자동 종료됩니다".format(5-i))
    time.sleep(1)
exit()
    
    
