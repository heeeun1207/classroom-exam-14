def exampleOne(a):
    if not isinstance(a, int):
        raise TypeError('정수를 입력해야 합니다.')
    return a

try:
    a = int(input("정수를 입력하세요: "))
    result = exampleOne(a)
    print("결과:", result)
except ValueError:
    print("정수를 입력해주세요.")
except TypeError as e:
    print(str(e))
# python3.10 정희은.py   