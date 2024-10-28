def calculate_bmi(height,weight):
    print("Height =" +str(height))
    print("Weight =" +str(weight))
    bmi=weight/(height*height)
    print(f"Your BMI is {bmi:.2f}")
    if bmi<18.5:
        classidentification= "Under weight"
        return -1
    elif 18.5 <= bmi <= 25.0:
        classidentification= "Normal Weight"
        return 0
    else:
        classidentification= "Over Weight"
        return 1
    print(f"Weight Classification: {classidentification}")
calculate_bmi(weight=57,height=1.73)    