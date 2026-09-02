# Problem/Programmers/python/Q42576/Q42576_완주하지 못한 선수.py
from collections import Counter

def solution(participant, completion):
    dict_p = Counter(participant)
    dict_c = Counter(completion)
    for name in tuple(participant):
        if dict_p[name] != dict_c[name]:
            return name

    # LLM 풀이
    # return next(iter(Counter(participant) - Counter(completion)))
    # return list(Counter(participant) - Counter(completion))[0]