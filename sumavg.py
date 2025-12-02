# Program to calculate sum and average of scores

def calculate_sum_and_average(s):
    total = sum(s)
    average = total / len(s)
    return total, average


if __name__ == "__main__":
    import sys
    print("=== Score Calculator (Sum & Average) ===")

    try:
        if len(sys.argv) > 1:
            s = list(map(float, sys.argv[1:]))
        else:
            s = input("Enter scores separated by space: ")
            s = list(map(float, s.split()))

        print("\n=== Program Parameters ===")
        print(f"Scores entered: {s}")

        total, average = calculate_sum_and_average(s)

        print(f"\nSum of scores = {total}")
        print(f"Average of scores = {average:.2f}")

    except ValueError:
        print("Invalid input. Please enter only numeric values.")
