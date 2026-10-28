# -*-coding:utf-8 -*-
# Date: 2026-10-20 15:16:00


sentence = "Hans isst ein Kaesebrot"
list_sentence = sentence.strip().split()

def parse_S(list_sentence, start: int, end: int) -> bool:
    for j in range(start + 1, end):
        if parse_NP(list_sentence, start, j) and parse_VP(list_sentence, j, end):
            return True
    else:
        return False



def parse_NP(list_sentence, start: int, end: int) -> bool:
    if end == start + 1 and list_sentence[start] == "Hans":
        return True

    for j in range(start + 1, end):
        if parse_Det(list_sentence, start, j) and parse_N(list_sentence, j, end):
            return True
    else:
        return False


def parse_VP(list_sentence, start: int, end: int) -> bool:
    for j in range(start + 1, end):
        if parse_V(list_sentence, start, j) and parse_NP(list_sentence, j, end):
            return True
    else:
        return False


def parse_N(list_sentence, start: int, end: int) -> bool:
    if end == start + 1 and list_sentence[start] == "Kaesebrot":
        print("Kaesebrot")
        return True
    else:
        return False



def parse_V(list_sentence, start: int, end: int) -> bool:
    if end == start + 1 and list_sentence[start] == "isst":
        return True
    else:
        return False

def parse_Det(list_sentence: list, start: int, end: int) -> bool:
    if end == start + 1 and list_sentence[start] == "ein":
        return True
    else:
        return False
