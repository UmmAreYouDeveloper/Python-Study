def is_odd(n):
    if n % 2 == 0:
        print('주어진 수는 짝수입니다.')
    else:
        print('주어진 수는 홀수입니다.')  

a = input('수를 입력하세요 : ')
# int(str) => str을 숫자로 변환
is_odd(int(a))