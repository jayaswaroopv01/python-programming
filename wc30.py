lang1=int(input("enter lang1 marks:"))
lang2=int(input("enter lang2 marks:"))
lang3=int(input("enter lang3 marks:"))
maths=int(input("enter maths marks:"))
science=int(input("enter science marks:"))
social=int(input("enter social marks:"))
if(lang1>100 or lang2>100 or lang3>100 or maths>100 or science>100 or social>100)or(lang1<0 or lang2<0 or lang3<0 or maths<0 or science<0 or social<0):
    print("enter valid marks")
elif(lang1<35 or lang2<35 or lang3<35 or maths<35 or science<35 or social<35):
    print("fail")
else:
    total_marks=lang1+lang2+lang3+maths+science+social
    per=(total_marks/500)*100
    print("per=",per)
    if(per>=75):
        print("passed in distinction")
    elif(per>=60):
        print("passed in first class")
    elif(per>=50):
        print("passed in second class")
    elif(per>=35):
        print("just pass")
    else:
        print("fail")
        