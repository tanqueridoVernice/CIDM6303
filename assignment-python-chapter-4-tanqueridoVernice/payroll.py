# create a function to calculate various taxes for an employee
# see instructions for details
# Vernice Tanquerido

def calc_payroll_tax(gross_pay):
    medicare = gross_pay*.0145
    futa = gross_pay*.006
    ss_tax_employer = gross_pay*.062
    ss_tax_employee = gross_pay*0.062
    total_tax = medicare + futa + ss_tax_employee
    net_pay = gross_pay-total_tax
    return (f"Gross Pay: $ {gross_pay: .2f}\nMedicare Tax: $ {medicare: .2f}\nFUTA tax: $ {futa: .2f}\nSocial Security Tax paid by employer: $ {ss_tax_employer: .2f}\nSocial Security Tax paid by employee: $ {ss_tax_employee: .2f}\nTotal Payroll Tax paid by employee: $ {total_tax: .2f}\nNet Pay: $ {net_pay: .2f}")


payroll = calc_payroll_tax(200)
print(payroll)
print("-"*20)
payroll = calc_payroll_tax(4000)
print(payroll)
print("-"*20)
payroll = calc_payroll_tax(21000)
print(payroll)
print("-"*20)
