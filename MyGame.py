import time

a="-"
b="-"
c="-"
d="-"
e="-"
f="-"
g="-"
h="-"
i="-"


def board():
    print(a, "|", b, "|", c)
    print("--+---+-- ")
    print(d, "|", e, "|", f)
    print("--+---+-- ")
    print(g, "|", h, "|", i)

def Horroziontal():
    if a == b == c and (a != "-"):
        print(a, " Won!")
        time.sleep(3)
        quit()
    elif d == e == f and (d != "-"):
        print(d, " Won!")
        time.sleep(3)
        quit()
    elif g == h == i and (g != "-"):
        print(g, " Won!")
        time.sleep(3)
        quit()

def Vertical():
    if a == d == g and (a != "-"):
        print(a, " Won!")
        time.sleep(3)
        quit()
    elif b == e == h and (b != "-"):
        print(b, " Won!")
        time.sleep(3)
        quit()
    elif c == f == i and (c != "-"):
        print(c, " Won!")
        time.sleep(3)
        quit()
    else:
        None

def Diagonal():
    if a == e == i and (a != "-"):
        print(a, " Won!")
        time.sleep(3)
        quit()
    elif c == e == g and (c != "-"):
        print(c, " Won!")
        time.sleep(3)
        quit()
    else:
        None

def Tie():
    if a != "-" and b != "-" and c != "-" and d != "-" and e != "-" and f != "-" and g != "-" and h != "-" and i != "-":
            print("The gaem was a tie.")
            time.sleep(3)
            quit()
    else:
        None

board()
GameRunning = True
while GameRunning:
        P1 = int(input("Pick 1-9: "))
        if (P1 == 1) and (a != "X" and a != "O"):
            a = "X"
        elif (P1 == 2) and (b != "X" and b != "O"):
            b = "X"
        elif (P1 == 3) and (c != "X" and c != "O"):
            c = "X"
        elif (P1 == 4) and (d != "X" and d != "O"):
            d = "X"
        elif (P1 == 5) and (e != "X" and e != "O"):
            e = "X"
        elif (P1 == 6) and (f != "X" and f != "O"):
            f = "X"
        elif (P1 == 7) and (g != "X" and g != "O"):
            g = "X"
        elif (P1 == 8) and (h != "X" and h != "O"):
            h = "X"
        elif (P1 == 9) and (i != "X" and i != "O"):
            i = "X"
        else:
            print("Cant Do That")
            time.sleep(2)
            exit()

        board()
        Horroziontal()
        Vertical()
        Diagonal()
        Tie()
        
        P2 = int(input("Pick 1-9: "))
        if (P2 == 1) and (a != "X" and a != "O"):
            a = "O"
        elif (P2 == 2) and (b != "X" and b != "O"):
            b = "O"
        elif (P2 == 3) and (c != "X" and c != "O"):
            c = "O"
        elif (P2 == 4) and (d != "X" and d != "O"):
            d = "O"
        elif (P2 == 5) and (e != "X" and e != "O"):
            e = "O"
        elif (P2 == 6) and (f != "X" and f != "O"):
            f = "O"
        elif (P2 == 7) and (g != "X" and g != "O"):
            g = "O"
        elif (P2 == 8) and (h != "X" and h != "O"):
            h = "O"
        elif (P2 == 9) and (i != "X" and i != "O"):
            i = "O"
        else:
            print("Cant Do That")
            time.sleep(2)
            exit()

        board()
        Horroziontal()
        Vertical()
        Diagonal()
        Tie()
        
