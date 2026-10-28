# -*-coding:utf-8 -*-
# Date: 2026-10-20 15:16:00


sentence = "Hans isst ein Kaesebrot"
list_sentence = sentence.strip().split()

def parse_S(list_sentence, start: int, end: int) -> bool:
    print(f"calling S from {start} till the {end}?")
    for j in range(start + 1, end):
        if parse_NP(list_sentence, start, j) and parse_VP(list_sentence, j, end):
            print(f"S from {start} to {j} is OK")
            return True
    else:
        print(f"S from {start} to {j} is NOT ok")
        return False

def parse_NP(list_sentence, start: int, end: int) -> bool:
    print(f"brr brr: is it NP von {start} bis {end}?")
    if end == start + 1:
        word = list_sentence[start]
        if word == "Hans":
            print(f"Word '{word}' from {start} till {end}?-> yes ")
            print(f"NP from {start} till {end}?-> ja")
            return True
        else:
            print(f"word '{word}' from {start} till {end}?-> no it's patrick")

    for j in range(start + 1, end):
        if parse_Det(list_sentence, start, j) and parse_N(list_sentence, j, end):
            print(f"NP from {start} till {end}? -> yes")
            return True
    else:
        print(f"NP from {start} till {end}?-> no")
        return False


def parse_VP(list_sentence, start: int, end: int) -> bool:
    print(f"Call: VP from {start} to {end}?")
    for j in range(start + 1, end):
        if parse_V(list_sentence, start, j) and parse_NP(list_sentence, j, end):
            print(f"VP from {start} to {end}? -> yes")
            return True
    else:
        print(f"VP from {start} to {end}? -> no")
        return False

def parse_N(list_sentence, start: int, end: int) -> bool:
    print(f"Call: N from {start} to {end}?")

    if end == start + 1:
        word = list_sentence[start]
        if word == "Kaesebrot":
            print(f"Word '{word}' from {start} to {end}? -> yes")
            print(f"N from {start} to {end}? -> yes")
            return True
        else:
            print(f"Word '{word}' from {start} to {end}? -> no")

    print(f"N from {start} to {end}? -> no")
    return False

def parse_V(list_sentence, start: int, end: int) -> bool:
    print(f"Call: V von {start} bis {end}?")
    if end == start + 1 and list_sentence[start] == "isst":
        print(f"Wort '{list_sentence[start]}' von {start} bis {end}?-> ja")
        print(f"V von {start} bis {end}?-> ja")
        return True
    else:
        return False

def parse_Det(list_sentence: list, start: int, end: int) -> bool:
    print(f"Call: Det von {start} bis {end}?")
    if end == start + 1 and list_sentence[start] == "ein":
        print(f"Wort '{list_sentence[start]}' von {start} bis {end}?-> ja")
        print(f"Det von {start} bis {end}?-> ja")
        return True
    else:
        print(f"Det from {start} to {end}? -> no")
        return False

if __name__ == "__main__":
    # --- Satz 1 ---
    print("=" * 50)
    print("Trace für Satz 1: 'Hans isst ein Kaesebrot'")
    print("=" * 50)
    s1 = ["Hans", "isst", "ein", "Kaesebrot"]
    res1 = parse_S(s1, 0, len(s1))
    print(res1)

    print("\n\n" + "-" * 50 + "\n\n")

    # --- Satz 2 ---
    print("=" * 50)
    print("Trace für Satz 2: 'Kaesebrot isst Hans'")
    print("=" * 50)
    s2 = ["Kaesebrot", "isst", "Hans"]
    res2 = parse_S(s2, 0, len(s2))
    print(res2)