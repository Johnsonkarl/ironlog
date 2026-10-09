def calculate_one_rep_max(weight, reps):
    return round(weight * (1 + reps / 30), 1)


if __name__ == "__main__":
    print("Welcome to IronLog!")

    weight = float(input("Weight lifted (lbs): "))
    reps = int(input("Reps completed: "))

    estimated_max = calculate_one_rep_max(weight, reps)

    print(f"Estimated 1RM: {estimated_max} lbs")