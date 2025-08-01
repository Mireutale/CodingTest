# 백준 1759번 - 암호 만들기

[문제 보러 가기](https://www.acmicpc.net/problem/1759)

## 요약

> 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.  
> 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이다.
> 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다.
> C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

## 핵심 규칙

> 입력
>
> > 첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15)
> > 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다.
> > 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

> 출력
>
> > 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

## 예제 입출력

입력 및 출력 예시는 [문제 링크](https://www.acmicpc.net/problem/1759) 참고.

### 문제풀이

암호는 서로다른 L개의 알파벳소문자들로 구성되며, 최소 한 개의 모음과 최소 두 개의 자음으로 구성된다.

모음 (a, e, i, o, u)를 리스트로 설정
C개의 문자로 L개의 알파벳소문자를 활용한 암호를 설정한 경우, 모음이 1개이상, 자음이 2개이상인 경우 값을 출력
