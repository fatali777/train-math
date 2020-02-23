import random


def generate_division():
    a = random.randint(2, 100) # 32

    bolunenler = []
    for eded in range(2, a):
        if a % eded == 0:
            bolunenler.append(eded)

    if bolunenler == []:
        print("maaalesef pis edede ilishdin: ", a)
        exit()
        
    b = random.choice(bolunenler)
    true_result = a/b
    display_text = f" { a} / { b} = ?"
    return (true_result, display_text)


    # 2->32     2,3,4,5,6,7,31


def generate_subtract():
    a = random.randint(0, 200)
    b = random.randint(0, 200)

    true_result = a - b
    display_text = f"{a} - {b} = ?"

    return (true_result, display_text)


def generate_addition():
    a = random.randint(2, 199)
    b = random.randint(2, 199)

    true_result = a + b
    display_text = f"{a} + {b} = ?"

    return (true_result, display_text)

def generate_multiple():
    num1 = random.randint(2, 15)
    num2 = random.randint(2, 15)

    true_result = num1 * num2
    display_text = f" { num1} x { num2} = ?"

    return (true_result, display_text)

def is_number(s):
    if s.isdecimal():
        return True
    if s.startswith("-"):
        cut_s = s[1:]
        if cut_s.isdecimal():
            return True
    return False

def get_int():
    enter = input(" Cavab: ")
    while not is_number(enter):
        print(" Invalid input")
        enter = input(" Cavab: ")

    int_enter = int(enter)
    return int_enter



#0-50 toplama, 50-100 chixma, 100-200 vurma, 200+ bolme
xal=0
while True:
   if xal < 50:
       answer, text = generate_addition()
       print(text)
       user_input = get_int()

       if user_input == answer:
           print(" Dogru Cavab! ")
           xal = xal +5
           print(f" Xaliniz: {xal}")
       else:
           print(f" YANLISH CAVAB!!! Doghru cavab: {answer}")
           xal=xal - 5
           print(" Xaliniz ", xal)
   elif xal >= 50 and xal < 100:
       answer, text = generate_subtract()
       print(text)
       user_input = get_int()
       if user_input == answer:
           print(" Dogru Cavab! ")
           xal = xal +5
           print(f" Xaliniz: {xal}")
       else:
           print(f" YANLISH CAVAB!!! Doghru cavab: {answer}")
           xal=xal - 5
           print(" Xaliniz ", xal)
   elif xal >= 100 and xal < 200:
       answer, text = generate_multiple()
       print(text)
       user_input = get_int()
       if user_input == answer:
           print(" Dogru Cavab! ")
           xal = xal +5
           print(f" Xaliniz: {xal}")
       else:
           print(f" YANLISH CAVAB!!! Doghru cavab: {answer}")
           xal=xal - 5
           print(" Xaliniz ", xal)
   elif xal >= 200 and xal < 300:
       answer, text = generate_division()
       print(text)
       user_input = get_int()
       if user_input == answer:
           print(" Dogru Cavab! ")
           xal = xal +5
           print(f" Xaliniz: {xal}")
       else:
           print(f" YANLISH CAVAB!!! Doghru cavab: {answer}")
           xal=xal - 5
           print(" Xaliniz ", xal)
