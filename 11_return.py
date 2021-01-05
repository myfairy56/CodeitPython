#개념 복습
#변수 : 값을 저장하는 것
#함수 : 명령을 저장하는 것
#파라미터 : 함수에 넘겨 주는 값

#return : 함수에 정보를 주면 다른 정보를 돌려주는 것


def get_square(x):
    return x * x

print(get_square(3))
#파라미터로 3을 넘겨줬다고 가정 > x로 3이 들어가서 return 3*3이 된다
# 함수를 호출한 get_square 3 부분이 9로 바뀌게 된다.

y = get_square(3)
print(y)
#등호 : 지정연산자 오른쪽 값을 왼쪽 변수에 넣어준다
#get_square 함수가 호출되는데 정수값 3이 파라미터로 넘어간다.
#return 3 * 3으로 get_square(3)은 9로 바뀐다

print(get_square(3) + get_square(4))
#3이 먼저 호출. 정수 3이 파라미터 x로 들어가서 9
#4가 호출. 4가 파라미터 x로 들어가서 16이 리턴
#결국 print 9+16이기 때문에 25 출력
