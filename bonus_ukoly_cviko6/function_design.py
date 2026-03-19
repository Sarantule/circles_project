#Kontrola síly hesla
def analyze_password(password, min_length=8, require_digit=True, require_upper=True,
                     require_symbol=False, banned_words=None):
    if banned_words == None:
        banned_words = ['sardinka', 'pavouk', '1492']

    symbols = "!@#$%^&*()-_=+[]{};:,.?"
    missing_rules = []
    total_rules = 0
    passed_rules = 0

    # 1) minimální délka hesla
    total_rules = total_rules + 1
    if len(password) >= min_length:
        passed_rules = passed_rules + 1
    else:
        missing_rules.append("min_length")

    # 2) musí číslo obsahovat číslici?
    if require_digit == True:
        total_rules = total_rules + 1
        has_digit = False
        for i in range(len(password)):
            if password[i].isdigit():
                has_digit = True

        if has_digit == True:
            passed_rules = passed_rules + 1
        else:
            missing_rules.append("digit")

    # 3) musí obsahovat velké písmeno?
    if require_upper == True:
        total_rules = total_rules + 1
        has_upper = False
        for i in range(len(password)):
            if password[i].isupper():
                has_upper = True

        if has_upper == True:
            passed_rules = passed_rules + 1
        else:
            missing_rules.append("upper")

    # 4) aspoň 1 symbol
    if require_symbol == True:
        total_rules = total_rules + 1
        has_symbol = False
        for i in range(len(password)):
            if password[i] in symbols:
                has_symbol = True

        if has_symbol == True:
            passed_rules = passed_rules + 1
        else:
            missing_rules.append("symbol")

    # 5) zakázaná slova?
    total_rules = total_rules + 1
    password_lower = password.lower()
    contains_banned = False

    for i in range(len(banned_words)):
        if banned_words[i].lower() in password_lower:
            contains_banned = True

    if contains_banned == True:
        missing_rules.append("banned_word")
    else:
        passed_rules = passed_rules + 1

    # 3 výstupy:
    # 1. splní všechna pravidla?
    if len(missing_rules) == 0:
        is_strong = True
    else:
        is_strong = False
    # procentuální podíl splněných pravidel?
    score_percent = int((passed_rules / total_rules) * 100)
    # seznam pravidel, které heslo nesplnilo?
    return is_strong, score_percent, missing_rules


#  4 testíky
#1. čistě poziční
print(analyze_password("Abc12345", 8, True, True, False, None))
print("Poziční")

#2. mix pozičních a pojmenovaných argumentů
print(analyze_password("Abcdef1234", 10, require_upper=True, require_symbol=True))
print("Mix")

#3. volání s vypnutým pravidlem pro symbol
print(analyze_password("Abcdef12", require_symbol=False))
print("Vypnutí symbolu")

#4. volání s vlastní seznamem banned_words
print(analyze_password("sardinka1492", require_symbol=True,
                      banned_words=['sardinka', 'pavouk', '1492']))
print("Moje banned_words")