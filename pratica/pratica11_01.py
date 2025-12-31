for c in range(ord('0'), ord('9') + 1):
    print(f"{chr(c)} – {c} – {format(c, '08b')}")
for c in range(ord('A'), ord('Z') + 1):
    print(f"{chr(c)} – {c} – {format(c, '08b')}")
for c in range(ord('a'), ord('z') + 1):
    print(f"{chr(c)} – {c} – {format(c, '08b')}")
