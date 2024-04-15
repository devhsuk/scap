import mss

with mss.mss() as s:
    M = s.monitors
    for i, m in enumerate(M):
        print(i, m)
