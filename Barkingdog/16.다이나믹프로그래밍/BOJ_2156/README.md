# 백준 2156번 - 포도주 시식

[문제 보러 가기](https://www.acmicpc.net/problem/2156)

## 요약

- 규칙 1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.

- 규칙 2. 연속으로 놓여 있는 3잔을 모두 마실수는 없다.

가능한 많은 양의 포도주를 맛보기 위해서 포도주 잔을 선택

1부터 n까지 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블에 놓여 있고, 포도주 잔에 들어있는 양이 주어진다.

## 핵심 규칙

- 첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000) 
- 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 
- 포도주의 양은 1,000 이하의 음이 아닌 정수이다.
- 첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

## 예제 입출력

입력 및 출력 예시는 [문제 링크](https://www.acmicpc.net/problem/2156) 참고.

### 문제풀이

`1. 관찰`

- 예제 1 처럼 6, 10, 13, 9, 8, 1이 순서대로 포도주 잔에 들어있다고 해보자.

dp[0] = list[0] = 6  
dp[1] = list[0] + list[1]  
dp[2] = max(list[0] + list[2], dp[1], list[1]+list[2])  
dp[i] = max(dp[i-2] + list[i], dp[i-1], dp[i-3] + list[i-1] + list[i])

- 위 형식대로 점화식을 구성할 수 있다.