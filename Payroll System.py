#text based payroll system:
def text_calcutate():
    salary_input = float(input("Enter your salary: "))
    salary = float(salary_input.replace(",", ""))  
    tax = 0

    if salary <= 600000:
        tax = 0
    elif salary <= 2500000:
        tax = salary * 0.05
    elif salary <= 5000000:
        tax = (2500000 * 0.05) + ((salary - 2500000) * 0.1)
    elif salary <= 10000000:
        tax = (2500000 * 0.05) + (2500000 * 0.1) + ((salary - 5000000) * 0.15)
    elif salary <= 20000000:
        tax = (2500000 * 0.05) + (2500000 * 0.1) + (5000000 * 0.15) + ((salary - 10000000) * 0.2)
        print(f"Tax",tax)

text_calcutate()



