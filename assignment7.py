from amortization.amount import calculate_amortization_amount
from amortization.schedule import amortization_schedule
from tabulate import tabulate


class AmortizationSchedule:
    principal = None
    monthlyInterestRate = None
    numberOfMonths = None

    def __init__(self, principal, monthlyInterestRate, numberOfMonths):
        self.principal = principal
        self.monthlyInterestRate = monthlyInterestRate
        self.numberOfMonths = numberOfMonths

    def createAmortizationGenerator(self):
        schedule = amortization_schedule(
            self.principal, (self.monthlyInterestRate/12)/100, self.numberOfMonths)
        for i in schedule:
            yield i

    def calculate(self):
        table = self.createAmortizationGenerator()
        print(
            tabulate(
                table,
                headers=["Number", "Amount",
                         "Interest", "Principal", "Balance"],
                floatfmt=",.2f",
                numalign="right"
            )
        )


principal = float(input('What is the value of the principal:\t\t'))
monthlyInterestRate = float(
    input('What is the value of the monthly interest rate:\t'))
numberOfMonths = int(input('What is the number of months:\t\t\t'))

schedule = AmortizationSchedule(principal, monthlyInterestRate, numberOfMonths)
schedule.calculate()
