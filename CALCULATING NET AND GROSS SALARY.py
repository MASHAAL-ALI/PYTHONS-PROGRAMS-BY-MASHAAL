n=int(input("ENTER NUMBER OF EMPLOYEE YOU WANT TO TAKE : "))
for i in range(n):
    employee_salary=int(input('ENTER EMPLOYEE SALARY: '))
    if employee_salary<=10000:
        HRA = employee_salary*0.2
        DA= employee_salary*0.8
        DD = employee_salary*0.02
        GS = employee_salary+HRA+DA
        NS = GS-DD
        print('GROSS SALARY IS: ',int(GS))
        print('NET SALARY IS: ',int(NS))
    if employee_salary<=20000:
        HRA = employee_salary*0.2
        DA= employee_salary*0.8
        DD = employee_salary*0.02
        GS = employee_salary+HRA+DA
        NS = GS-DD
        print('GROSS SALARY IS: ',int(GS))
        print('NET SALARY IS: ',int(NS))
    else:
        HRA = employee_salary*0.2
        DA= employee_salary*0.8
        DD = employee_salary*0.02
        GS = employee_salary+HRA+DA
        NS = GS-DD
        print('GROSS SALARY IS: ',int(GS))
        print('NET SALARY IS: ',int(NS))
        
