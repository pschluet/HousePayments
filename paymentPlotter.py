import numpy as np
from matplotlib import pyplot as plt

def getMonthlyMortgagePayment(L, n, r):
    '''
    :param L: Total loan amount
    :param n: Loan term (in months)
    :param r: Interest rate
    :return: The fixed monthly payment required to fully amortize a loan of L
             dollars over a term of n months at an annual interest rate of r
             [If the quoted rate is 6%, for example, c is .06]
    '''

    # Calculate monthly interest rate
    c = r / 12

    return L * (c * (1 + c)**n) / ((1 + c)**n - 1)

if __name__ == "__main__":
    homeVals = np.arange(228, 241) * 1000
    nMonthTerm = 30 * 12
    intRate = 0.045
    annualTaxes = np.arange(4500, 6500, 500)
    annualInsurance = 900
    pmiPercent = 0.0044
    percentDownPayment = 0.1


    for annualTax in annualTaxes:
        monthlyPayments = []
        for homeVal in homeVals:
            loan = homeVal * (1 - percentDownPayment)
            monthlyMortgage = getMonthlyMortgagePayment(loan, nMonthTerm, intRate)
            monthlyPMI = loan * pmiPercent / 12
            monthlyPayment = monthlyMortgage + monthlyPMI + (annualTax + annualInsurance) / 12

            monthlyPayments.append(monthlyPayment)

            print('{} - {:.2f}'.format(homeVal, monthlyPayment))


        plt.plot(homeVals / 1000, monthlyPayments, '-o')
    plt.legend(annualTaxes)
    plt.xlabel('Home Price (thousands)')
    plt.ylabel('Monthly Payment')
    plt.title('Monthly Payment vs Home Price')
    plt.grid()
    plt.savefig('plot.png')
