score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
# simplier syntax
elif 70 <= score < 80:
    print("Grade: C")
# simplier simplier
elif score >= 50:
    print("Grade: D")
else:
    print("soooo pooooor")
