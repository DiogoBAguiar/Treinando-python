A = []
for _ in range(100):
    A.append(float(input()))
for i in range(100):
    if A[i] <= 10:
        print(f"A[{i}] = {A[i]:.1f}")

