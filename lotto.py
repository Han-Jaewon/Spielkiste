import sys
import random

# % python lotto.py {y/n} {num}    - y/n: 세트 구매(y) 한 줄 구매(n)  - num: 몇 장(줄) 구매?

yn = sys.argv[1]    # "y" or "n" 입력
num = int(sys.argv[2])    # 숫자 입력

# 랜덤 번호 추출
def random_pop(data):
	number = random.choice(data)
	data.remove(number)
	return number

price = 0

if yn == "y":      # 세트 구매 시
    for k in range(1, num+1):
        price = num*5000
        if price > 100000:
            print(f"{'-'*50}\n일일 최대 한도를 넘어섰습니다. 과도한 도박은 좋지 않습니다. 가볍게 즐겨주세요 ‎(*˙︶˙*)و")
            break
        else:
            data = []
            for i in range(1, 46):
                data.append(i)
            print(f"{'-'*50}\n{k}번째 장\n{'-'*50}")
            for i in ['A', 'B', 'C', 'D', 'E']:
                result = []
                for j in range(6):
                    result.append(random_pop(data))
                
                print(f"{i}: 행운의 로또 번호는 {sorted(result)}입니다.")
    print(f"{'-'*50}\n총 금액: {price}원입니다.")

elif yn == "n":    # 한 줄 구매 시
    cnt = 0
    data = []
    for i in range(1, 46):
        data.append(i)
    print('-'*50)
    for i in ['A', 'B', 'C', 'D', 'E']:
        result = []        
        if cnt == num: break
        for j in range(6):
            result.append(random_pop(data))
        print(f"{i}: 행운의 로또 번호는 {sorted(result)}입니다.")
        cnt += 1
    price += num*1000
    print(f"{'-'*50}\n총 금액: {price}원입니다.")
else:
    print("sys.argv[1]에는 y 또는 n으로 입력해 주세요.")
