def average(list):
    return sum(list) / len(list)
# input.split은 문자열 리스트로 한꺼번에 입력받음
# 이를 int형으로 변환하기 위해서는 map(int,input().split())
# 이것은 리스트이므로 map -> list로 변환
a = list(map(int,input('수들을 입력하시오. : ').split()))
print(average(a))