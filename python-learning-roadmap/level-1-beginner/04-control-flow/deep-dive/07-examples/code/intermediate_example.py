scores = [91, 62, 75, 88]
for score in scores:
    if score < 70:
        print("Needs review")
        continue
    print("Passed")
