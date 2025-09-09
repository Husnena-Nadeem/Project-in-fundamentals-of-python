def employee_details():
    name = input("Enter employee name: ")
    phone = input("Enter phone number: ")
    scale = int(input("Enter your scale (1-22): "))
    designation = input("Enter your designation: ")
    dep = input("Enter your department: ")
    salary = float(input("Enter your basic salary: "))

    # store data in dictionary
    employee = {
        "name": name,
        "phone": phone,
        "scale": scale,
        "designation": designation,
        "department": dep,
        "salary": salary,
    }
    return employee


# Function to calculate allowances
def calculate_allowances(scale, salary):
    house = medical = transport = special = other = 0

    if 1 <= scale <= 4:
        house = 0.10 * salary
        medical = 0.05 * salary
        transport = 0.05 * salary
        other = 2000
    elif 5 <= scale <= 10:
        house = 0.12 * salary
        medical = 0.07 * salary
        transport = 0.06 * salary
        special = 0.02 * salary
        other = 3000
    elif 11 <= scale <= 14:
        house = 0.15 * salary
        medical = 0.10 * salary
        transport = 0.08 * salary
        special = 0.05 * salary
        other = 4000
    else:
        house = 0.20 * salary
        medical = 0.15 * salary
        transport = 0.12 * salary
        special = 0.10 * salary
        other = 6000

    total = salary + house + medical + transport + special + other
    return total


# Function to apply tax
def apply_tax(annual_salary):
    tax = 0

    if annual_salary <= 600000:
        tax = 0
    elif annual_salary <= 2500000:
        tax = annual_salary * 0.05
    elif annual_salary <= 5000000:
        tax = (2500000 * 0.05) + ((annual_salary - 2500000) * 0.1)
    elif annual_salary <= 10000000:
        tax = (2500000 * 0.05) + (2500000 * 0.1) + ((annual_salary - 5000000) * 0.15)
    elif annual_salary <= 20000000:
        tax = (2500000 * 0.05) + (2500000 * 0.1) + (5000000 * 0.15) + ((annual_salary - 10000000) * 0.2)

    return annual_salary - tax


# Simple Text-based payroll system (direct calculator)
def text_calculate():
    salary_input = input("Enter your annual salary: ")
    annalsalary = float(salary_input.replace(",", ""))  # remove commas
    tax = 0

    if annalsalary <= 600000:
        tax = 0
    elif annalsalary <= 2500000:
        tax = annalsalary * 0.05
    elif annalsalary <= 5000000:
        tax = (2500000 * 0.05) + ((annalsalary - 2500000) * 0.1)
    elif annalsalary <= 10000000:
        tax = (2500000 * 0.05) + (2500000 * 0.1) + ((annalsalary - 5000000) * 0.15)
    elif annalsalary <= 20000000:
        tax = (2500000 * 0.05) + (2500000 * 0.1) + (5000000 * 0.15) + ((annalsalary - 10000000) * 0.2)

    annalsalary -= tax
    print(f"Your annual salary after tax is: {annalsalary:,.2f}")

    monthly_salary = annalsalary / 12
    print(f"Your monthly salary after tax is: {monthly_salary:,.2f}")

    print(f"Tax: {tax:,.2f}")


def main():
    n = int(input("Enter number of employees: "))
    employees = []

    for i in range(n):
        print(f"\n--- Employee {i+1} ---")
        emp = employee_details()
        total = calculate_allowances(emp["scale"], emp["salary"])
        final = apply_tax(total)

        print("\nEmployee Details:")
        print("Name:", emp["name"])
        print("Phone:", emp["phone"])
        print("Designation:", emp["designation"])
        print("Department:", emp["department"])
        print("Scale:", emp["scale"])
        print("Basic Salary:", emp["salary"])
        print("Total with Allowances:", total)
        print("Final Salary after Tax:", final)

        employees.append(emp)


# Run program
main()
