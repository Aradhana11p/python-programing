def calculate_bmi(weight, height):
    """Calculates and returns BMI."""
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """Categorizes BMI into health categories."""
    if bmi < 18.5:
        return "Underweight"
    
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    elif 30.0 <= bmi < 34.9:
        return "Obese"
    else:
        return "obesity"

def main():
    """Main function to get input, calculate BMI, and display results."""
    name = input("Enter your name: ")

    try:
        # Input for height and weight
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kgs: "))

        # Validate height and weight
        if height <= 0 or weight <= 0:
            print("Height and weight must be positive values.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Output the calculated BMI and its category
        print(f"\n{name}'s BMI Report:")
        print(f"Calculated BMI: {bmi:.2f}")
        print(f"Category: {categorize_bmi(bmi)}")

    except ValueError:
        print("Please enter valid numeric values for height and weight.")

if _name_ == "_main_":
    main()
