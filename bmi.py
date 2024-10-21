def calculate_bmi(height,weight):
    print("Height =" +str(height))
    print("Weight =" +str(weight))
    bmi=weight/(height*height)
    print(f"Your BMI is {bmi:.2f}")
    if bmi<18.5:
        classidentification= "Under weight"
    elif 18.5 <= bmi <= 25.0:
        classidentification= "Normal Weight"
    else:
        classidentification= "Over Weight"
    print(f"Weight Classification: {classidentification}")
calculate_bmi(weight=57,height=1.73)    