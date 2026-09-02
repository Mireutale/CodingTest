"""
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
ex) 아래의 경우 구조대는 지영석 전호번호의 접두사
- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

phone_book : 전화번호부에 적힌 전화번호를 담은 배열
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false아니면 true를 return
"""
def solution(phone_book):
    phone_book.sort() # 전화번호부 정렬
    # 접두어가 있다면, 인접해 있음
    for i in range(len(phone_book)-1):
        # find는 문자열 전체에서 위치를 찾으므로, 0이면 맨 앞에 있는 것.
        if phone_book[i+1].find(phone_book[i]) == 0:
            return False
    return True