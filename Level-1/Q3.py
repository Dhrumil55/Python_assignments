def grade(p,ch,b,m,co):
    percentage = (p+ch+b+m+co)/5
    if percentage>=90:
        print("Grade A")
    elif percentage>=80:
        print("Grade B")
    elif percentage>=70:
        print("Grade C")
    elif percentage>=60:
        print("Grade D")
    elif percentage>=40:
        print("Grade E")
    else:
        print("Grade F")
grade(80,90,70,60,80)