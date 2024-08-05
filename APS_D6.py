# 패턴 매칭
# 고지식한 패턴검색(Brute Force)
t = 'TTTTTATTAATA'
p = 'TTA'
N = len(t)
M = len(p)
cnt = 0
for i in range(N-M+1):      # 비교 시작 위치
    for j in range(M):
        if t[i + j] != p[j]:
            break       # for j, 다음 글자부터 비교 시작
                        # 주석에 break의 대상을 표시해주면 디버깅이 편함. (for j)
    else:       # for j가 중단없이 반복되면
        cnt += 1        # 패턴 개수 1 증가
print(cnt)      # 2 (t에 p가 2개 있다)

##----------------------------------------------


# 오늘 배운 KMP, 보이어-무어 내용들은 알고만 있자 (B형 고난이도, 실무)
# 오늘은 Brute Force 로 패턴을 찾는 방법만 완벽하게 익히는 것을 추천 드립니다.
# 문자열 암호화(카이사르 암호) 관련 추천 문제
# https://www.acmicpc.net/problem/5598
# .find => 검색 시 brute force 로 구현됨 O(N*M)

# replace (1단계. Brute force)
# stack 활용 (2단계; 이번 주 4일간 학습 예정)
# DP활용, LCS (3단계)
# B형 (4단계)
