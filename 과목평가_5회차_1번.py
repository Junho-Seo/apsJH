T = int(input())  # 테스트 케이스의 수를 입력받음
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    N = int(input())  # 문자열의 길이를 입력받음
    bit = input()  # 비트 문자열을 입력받음

    max_v = 1  # 가장 긴 팰린드롬 길이를 저장할 변수, 초기값은 1 (최소 길이)

    # 문자열의 중심을 기준으로 팰린드롬 길이를 찾기 위한 반복문
    for i in range(1, N - 1):  # 첫 번째와 마지막 문자는 중심이 될 수 없으므로 1부터 N-1까지 반복
        j = 1  # 중심에서 얼마나 멀리 떨어진 위치를 비교할지 결정하는 변수

        # 중심에서 양쪽으로 같은 거리에 있는 문자가 동일한지 비교
        while 0 <= i - j and i + j < N and bit[i - j] == bit[i + j]:
            j += 1  # 팰린드롬의 범위를 확장

        # 현재 중심에서 찾은 팰린드롬 길이가 최대 길이인지 확인
        # (j-1)*2+1: 팰린드롬의 길이 계산 (실패한 위치를 제외한 범위)
        if max_v < (j - 1) * 2 + 1:
            max_v = (j - 1) * 2 + 1  # 최대 팰린드롬 길이를 갱신

    print(f'#{tc} {max_v}')  # 각 테스트 케이스의 결과 출력
