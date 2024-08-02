# 🇬🇷 Greek Salary Calculator CLI 🇬🇷

### Calculate your net salary in Greece for 2023 effortlessly!

![Salary Calculator](https://img.shields.io/badge/Salary%20Calculator-Python-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

---

## 🚀 Introduction

Welcome to the **Greek Salary Calculator CLI**! This Python CLI tool helps you calculate your net monthly and annual salary in Greece for the tax year 2023. It takes into account:
- Employer and employee insurance contributions
- Income tax
- Tax credits based on the number of children

---

## 🛠️ Features

- **Employer Contributions**: Automatically calculated based on the gross salary.
- **Employee Insurance Contributions**: Deducted before calculating the taxable income.
- **Income Tax**: Applied on a graduated basis according to Greek tax law.
- **Tax Credits**: Adjusted based on the number of children.

---

## 💻 How to Run

1. **Clone the repository**:
   ```sh
   git clone https://github.com/peterdsp/greek-salary-calculator-cli.git
   ```

2. **Navigate to the project directory**:
   ```sh
   cd greek-salary-calculator-cli
   ```

3. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```sh
   python ng_salary_calculator.py
   ```

---

## 📋 Example

```sh
$ python salary_calculator.py
Gross Monthly Salary: 2000
Number of Children: 2
Insurance institution: Electronic National Social Security Institution (e-NSSI)
Annual salaries: 14
Gross monthly salary: €2000.00
Gross annual salary: €28000.00
Net monthly salary: €1457.29
Net annual salary: €20401.08
```

---

## 🧮 Explanation of the Calculation

1. **Gross Monthly Salary**: The starting salary provided by the user.
2. **Annual Gross Salary**: Calculated as `gross_monthly_salary * 14` since there are 14 monthly payments in the year.
3. **Employee's Insurance Contribution**: Calculated based on whether the gross salary exceeds the insurable earnings ceiling.
4. **Annual Insurance Contribution**: The monthly insurance contribution multiplied by 14.
5. **Annual Taxable Income**: The gross annual salary minus the annual insurance contribution.
6. **Total Tax**: Calculated based on the taxable income using the given tax brackets and rates.
7. **Tax Credit**: Based on the number of children and reduced by income above €12,000.
8. **Final Tax**: The total tax reduced by the tax credit.
9. **Net Annual Income**: The gross annual salary minus the insurance contributions and final tax.
10. **Net Monthly Income**: The net annual income divided by 14.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgements

Special thanks to the developers and contributors who have made this project possible.

---

## 📧 Contact

For any questions, please contact us at [info@peterdsp.dev](mailto:info@peterdsp.dev).