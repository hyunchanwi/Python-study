# print("전체 주석 처리는 command / ")
#pythonTutor >> 코드 분석

#github 에 보내는법
#1. 터미널을 열고 (맨 처음) git init
#2. git add.
#3. git commit -m "first commit"
#4. git remote add origin https://github.com/hyunchanwi/Python-study.git
#5. git push origin master

# #하나만 출력합니다.
# print("#하나만 출력합니다.")
# print("hello python programming..")
# print()


# #여러개를 출력합니다.
# print("#여러개를 출력합니다.")
# print(10,20,30,40,50)
# print("안녕하세요","저의 이름은","위현찬입니다.")
# print()

# #아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
# print("#아무것도 출력하지 않습니다.")
# print("---확인 전용선---")
# print()
# print()
# print()
# print("---확인 전용선---") 

# print("print 함수에서 글자로 나열된 것은 string 이라고 표현")
# print("작은 따음표화 큰 따옴표로 문자열 만들기 가능")
# print()
# print("#이스케이프 문자를 사용해 문자열 만들기")
# print("문자열 내부에 \와 큰따옴 또는 짝은따옴표 붙여서 문자열 안에 큰따옴표 or 작은 따옴표 기능 가능")
# print("\ 와 n 을 붙인 것은 줄바꿈을 의미한다")
# print("\와 t를 붙인 것을 탭을 의미한다")
# print("\를 연속 2번 사용하면 \ \ \ \ 형식으로 나온다.")
# print()
# print("#여러 줄 문자열 만들기")
# print("긴 문자열 정리 가능")
# print("큰 따옴표 또는 작은 따옴표를 세번 반복한 기호 사용")
# print("추가로 \ 도 양끝에 붙여주면 의도치 않은 줄바꿈을 없앤다. ")
# print()
# print()
# print("#문자열 연결 연산자")
# print("+ 또는 * 를 사용해 문자 붙이기 또는 반복 가능")
# print("다만 문자는 문자끼리!")
# print()
# print("#문자 선택 연산자(인덱싱)")

###11월 24일 학습

# print()
# print()
# print("11월 24일")
# print()
# print("#3462를 17로 나눌 때")
# print("-몫:",3462//17)
# print("-나머지:",3462%17)

# pi = 3.14
# r = 10

# print("원주율 = ", pi )
# print("반지를 = ", 2*pi*r)
# print("원 넓이 = ", pi*r*r)

# print()
#복합 대입 연산자 

# a = 0

# print(a)
# a += 1
# print(a)
# a += 1
# print(a)
# a += 1
# print(a)
# a += 1
# print(a)
# a += 1

# print()

# string = "안녕하세요!"
# string += "!"
# string += "!"
# print(string)

# print()
# print()

# input() 함수

# input("입력해 주세요: ")
# input(">>> ")
# print()

#input 간단 활용

# print(input("입력해주세요: "))

# a = input(">>> ")
# print(a)

#문자열 > 숫자

# a = input("number1: ")
# b = input("number2: ")

# a = float(a)
# b = float(b)

# # print(a + b)

# #숫자 > 문자열
# c = str(a)
# print(a + b)
# print(c, type(c))

#총 정리
# string_a = input("숫자 1: ")
# int_a = int(string_a)

# string_b = input("숫자 2: ")
# int_b = int(string_b)

# print("문자열 결과: ", string_a + string_b)
# print("숫자열 결과: ", int_a + int_b)
# print("더하기: ", int_a + int_b)
# print("뺴기: ",int_a - int_b)
# print("곱하기: ",int_a * int_b)
# print("나누기: ",int_a / int_b)
# print("나눈 후 나머지: ",int_a % int_b)

#test 숫자 결과 후 문자열로 변환
# a = input("n1: ")
# b = input("n2: ")
# a = float(a)
# b =float(b)
# print(a + b)

# str_a = str(a)
# str_b = str(b)
# print(type(str_a), str_a )
# print(type(str_b), str_b)

#inch 단위를 cm 단위로 변경하기

# 입력: inch 단위를 입력
# a = input("inch 단위 숫자를 입력해주세요: ")


# # 처리: inch >> cm
# a = float(a) * 2.54


# # 출력: cm 단위를 출력
# print("cm 단위로는", a, "입니다")

#깔끔띠하게 도전쓰
#입력
# input_inch = input("cm으로 변환할 값을 입력해주세요: ")
# inch = float(input_inch)
# cm = inch * 2.54
# print(inch,"inch를 변환하면",cm,"cm입니다." )

#원 둘레, 넓이 계산
#132pg

#2개의 문자열을 입력받고 교대로 나열함을 출력하는 프로그램 만들기
#입력
# a = input("문자열 입력> ")
# b = input("문자열 입력> ")
#처리

#출력
# print(a, b)
#스왑
# c = a
# a = b
# b = c

# print(a, b)



#format함수 사용
# print("{}년 {}월 {}일".format(2024,11,24))

# #split() 
# print("10 20 30 40".split(" "))

###11월 25일 학습
#format 함수 좀더 쉽게 사용하는 문법 f-

#예)
# a = input("더할 값 1: ")
# b = input("더할 값 2: ")

# input_a = float(a)
# input_b = float(b)
# # "{}+{}={}".format()
# #>>
# print(f"{input_a}+{input_b}={input_a + input_b}")
# print("{}+{}={}".format(a, b, int(a)+input(b)))

#도전문제 [구의 부피와 겉넓이 구하기 프로그램]

# #입력
# r = input("반지름을 입력해주세요: ")
# #처리
# pi = 3.141592
# r = float(r)
# 넓이 = r * r * pi
# 부피 = (4/3) * pi * (r ** 3)
# 겉넓이 = 4 * pi * (r ** 2)
# #출력
# print(f"""\n 원의 넓이는 {넓이} 입니다.\n 구의 부피는 {부피} 입니다.\n 구의 겉넓이 {겉넓이} 입니다.""")

# #입력
# r = input("반지름을 입력해주세요: ")
# #처리
# pi = 3.141592
# r = float(r)
# 넓이 = r * r * pi
# 부피 = (4/3) * pi * (r ** 3)
# 겉넓이 = 4 * pi * (r ** 2)
# #출력
# print(f"""{"원의 넓이는", 넓이} 입니다. {"구의 부피는", 부피} 입니다. {"구의 겉넓이는", 겉넓이} 입니다.""")

#도전문제 2 [피타고라스의 정리 공식]

# 밑변 = input("밑변의 길이를 입력해주세요>>> ")
# 높이 = input("높이의 길이를 입력해주세요>>> ")
# a = float(밑변)
# b = float(높이)
# c = (a**2 + b**2)**(1/2)
# print( )
# print(f"빗변: {c}")

#upper() & lower()
#strip(): 문자열 양옆의 공백 제거 (lstrip, rstrip)
#isNN() -> 종류 다양
#find() & rfind() : 왼쪽부터 탐색, 오른쪽부터 탐색 (단 오른쪽부터 탐색할 때에는 오른쪽부터 찾고 인덱스는 원래대로 센다!!)



# i = input("무엇을 도와드릴까요?: ")

# if "몇시" in i or "몇 시" in i :

#     import datetime
#     import pytz 

#     seoul = pytz.timezone("Asia/Seoul")
#     now = datetime.datetime.now(seoul) 
    
#     print(
#         "{}년 {}월 {}일 {}시 {}분 {}초 ".format(
#             now.year,
#             now.month,
#             now.day,
#             now.hour,
#             now.minute,
#             now.second
#         )
#     )
    
# else :
#     print("몇시인지 물어봐 주십시오")


