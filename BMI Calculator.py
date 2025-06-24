def bmi_calculator():
    print("BMI Calculator")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obesity")

if __name__ == "__main__":
    bmi_calculator()
