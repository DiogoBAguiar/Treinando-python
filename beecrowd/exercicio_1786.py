w1 = [1,2,3,4,5,6,7,8,9]
w2 = [9,8,7,6,5,4,3,2,1]

while True:
    try:
        s = input().strip()
    except EOFError:
        break
    if len(s) != 9:
        continue

    digs = [ord(c) - 48 for c in s]

    b1 = sum(d*w for d, w in zip(digs, w1)) % 11
    if b1 == 10: b1 = 0
    b2 = sum(d*w for d, w in zip(digs, w2)) % 11
    if b2 == 10: b2 = 0

    print(f"{s[:3]}.{s[3:6]}.{s[6:9]}-{b1}{b2}")

