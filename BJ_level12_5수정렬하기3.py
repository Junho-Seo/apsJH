# gpt 메모리 개선 코드 (정답)
import sys
input = sys.stdin.readline

# 숫자의 개수 N을 입력받음
N = int(input())
arr = [0] * 10001  # 1부터 10000까지의 숫자를 카운트할 배열

# 각 숫자를 입력받아 카운트
for _ in range(N):
    num = int(input())  # 입력받은 숫자를 카운팅
    arr[num] += 1

# 출력: 각 숫자를 등장 횟수만큼 출력
for i in range(10001):
    if arr[i] > 0:
        for _ in range(arr[i]):
            print(i)  # i를 arr[i]만큼 출력



# 처음 풀이 (시간초과)
import sys
input = sys.stdin.readline

N = int(input())
nums = list(int(input())for _ in range(N))
arr = [0]*10001

for i in range(N):
    # arr[nums[i]]에 num이 들어온 개수 count
    arr[nums[i]] += 1

for i in range(10001):
    # arr[i] 에 숫자가 들어왔다면
    if arr[i] != 0:
        # arr[num]에 num이 들어온 개수만큼 출력
        for j in range(arr[i]):
            print(i)

# 카운팅 정렬(시간 초과)
# 개념 참고: https://seongonion.tistory.com/130
#           https://hyonlog.tistory.com/3
# 단점: 배열에 음수가 있다면 사용불가(인덱스 사용불가), 메모리를 비효율적으로 사용한다.
# 문제 조건: 수의 개수 N (1 ≤ N ≤ 10,000,000), 각 수는 10,000보다 작거나 같은 자연수
import sys
input = sys.stdin.readline

N = int(input())
nums = list(int(input())for _ in range(N))
# 배열에 존재하는 값의 각 원소의 개수를 셀 배열
count = [0] * (max(nums)+1)

# count[i] = 숫자 i가 배열에 몇 개 존재하는지에 대한 정보
for i in nums:
    count[i] += 1
# print(count)  # [0, 2, 2, 2, 1, 2, 0, 1]

# 누적합 값으로 갱신
for i in range(1, len(count)):
    count[i] += count[i-1]
# print(count)  # [0, 2, 4, 6, 7, 9, 9, 10]

# nums의 원소를 정렬된 위치에 저장할 배열
result = [0] * len(nums)

for i in nums:
    # nums의 각 원소값을 count의 인덱스로 사용해 값을 가져온 후
    # 해강 값을 다시 result의 인덱스로 사용해 nums의 원소로 저장
    result[count[i]-1] = i
    # 작업 완료 후 count[num[i]]의 값을 1 줄여준다.
    count[i] -= 1

print(*result, sep='\n')