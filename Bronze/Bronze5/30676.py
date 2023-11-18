import sys

input = sys.stdin.readline
lam = int(input())
if 620 <= lam <= 780:
    print("Red")
elif 590 <= lam < 620:
    print("Orange")
elif 570 <= lam < 590:
    print("Yellow")
elif 495 <= lam < 570:
    print("Green")
elif 450 <= lam < 495:
    print("Blue")
elif 425 <= lam < 450:
    print("Indigo")
elif 380 <= lam < 425:
    print("Violet")
