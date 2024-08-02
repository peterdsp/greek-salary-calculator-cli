import click


def calculate_net_salary(gross_monthly_salary, num_children):
    # Constants
    EMPLOYER_CONTRIBUTION_RATE = 0.2229
    EMPLOYEE_INSURANCE_CONTRIBUTION_RATE = 0.13867
    INSURABLE_EARNINGS_CEILING = 7126.94
    TAX_FREE_THRESHOLD = 8636

    # Tax brackets and rates
    TAX_BRACKETS = [
        (10000, 0.09),
        (10000, 0.22),
        (10000, 0.28),
        (10000, 0.36),
        (float('inf'), 0.44)
    ]

    # Child tax credits
    CHILD_TAX_CREDITS = {
        0: 777,
        1: 810,
        2: 900,
        3: 1120,
        4: 1340
    }

    # Calculate annual gross salary based on 14 months
    annual_gross_salary = gross_monthly_salary * 14

    # Calculate employee's insurance contribution
    if gross_monthly_salary > INSURABLE_EARNINGS_CEILING:
        insurance_contribution_monthly = INSURABLE_EARNINGS_CEILING * \
            EMPLOYEE_INSURANCE_CONTRIBUTION_RATE
    else:
        insurance_contribution_monthly = gross_monthly_salary * \
            EMPLOYEE_INSURANCE_CONTRIBUTION_RATE

    # Calculate annual insurance contribution
    annual_insurance_contribution = insurance_contribution_monthly * 14

    # Calculate annual taxable income
    annual_taxable_income = annual_gross_salary - annual_insurance_contribution

    # Calculate total tax based on taxable income and tax brackets
    remaining_income = annual_taxable_income
    total_tax = 0

    for bracket, rate in TAX_BRACKETS:
        if remaining_income > bracket:
            total_tax += bracket * rate
            remaining_income -= bracket
        else:
            total_tax += remaining_income * rate
            break

    # Calculate tax credit based on number of children
    if annual_taxable_income <= 12000:
        tax_credit = CHILD_TAX_CREDITS.get(num_children, 0)
    else:
        tax_credit_base = CHILD_TAX_CREDITS.get(num_children, 0)
        tax_credit_reduction = ((annual_taxable_income - 12000) // 1000) * 20
        tax_credit = max(0, tax_credit_base - tax_credit_reduction)

    # Calculate final tax after applying tax credit
    final_tax = max(0, total_tax - tax_credit)

    # Calculate net annual and monthly income
    net_annual_income = annual_gross_salary - \
        annual_insurance_contribution - final_tax
    net_monthly_income = net_annual_income / 14

    return net_monthly_income, net_annual_income, annual_gross_salary


@click.command()
@click.option('--gross-monthly-salary', prompt='Gross Monthly Salary', type=float)
@click.option('--num-children', prompt='Number of Children', type=int)
def main(gross_monthly_salary, num_children):
    """
    CLI command to calculate the net monthly and annual salary based on the provided gross monthly salary and number of children.
    """
    net_monthly_salary, net_annual_salary, annual_gross_salary = calculate_net_salary(
        gross_monthly_salary, num_children)
    click.echo(
        f"Insurance institution: Electronic National Social Security Institution (e-NSSI)")
    click.echo(f"Annual salaries: 14")
    click.echo(f"Gross monthly salary: €{gross_monthly_salary:.2f}")
    click.echo(f"Gross annual salary: €{annual_gross_salary:.2f}")
    click.echo(f"Net monthly salary: €{net_monthly_salary:.2f}")
    click.echo(f"Net annual salary: €{net_annual_salary:.2f}")


if __name__ == '__main__':
    main()
