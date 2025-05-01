import unittest
from finance_tools import (
    calculate_emi,
    calculate_sip,
    calculate_fd,
    calculate_rd,
    estimate_retirement_corpus,
    estimate_home_loan_eligibility,
    calculate_credit_card_balance,
    calculate_taxable_income,
    plan_budget,
    calculate_net_worth
)


class TestFinanceTools(unittest.TestCase):

    # EMI Calculator
    def test_calculate_emi_normal(self):
        self.assertAlmostEqual(calculate_emi(500000, 7.5, 15), 4635.06, places=2)

    def test_calculate_emi_edge(self):
        with self.assertRaises(ValueError):
            calculate_emi(-500000, 7.5, 15)

    # SIP Calculator
    def test_calculate_sip_normal(self):
        self.assertAlmostEqual(calculate_sip(5000, 12, 10), 1161695.38, places=2)

    def test_calculate_sip_edge(self):
        with self.assertRaises(ValueError):
            calculate_sip(0, 12, 10)

    # FD Calculator
    def test_calculate_fd_normal(self):
        self.assertAlmostEqual(calculate_fd(100000, 6.5, 5), 137008.67, places=2)

    def test_calculate_fd_edge(self):
        with self.assertRaises(ValueError):
            calculate_fd(100000, -5, 5)

    # RD Calculator
    def test_calculate_rd_normal(self):
        self.assertAlmostEqual(calculate_rd(2000, 7, 24), 58500.0, places=2)

    def test_calculate_rd_edge(self):
        with self.assertRaises(ValueError):
            calculate_rd(2000, 7, -1)

    # Retirement Corpus Estimator
    def test_estimate_retirement_corpus_normal(self):
        self.assertAlmostEqual(estimate_retirement_corpus(200000, 5000, 12, 20), 7174250.33, places=2)


    def test_estimate_retirement_corpus_edge(self):
        with self.assertRaises(ValueError):
            estimate_retirement_corpus(200000, 5000, 12, 0)

    # Home Loan Eligibility Estimator
    def test_estimate_home_loan_eligibility_normal(self):
        self.assertEqual(estimate_home_loan_eligibility(50000, 20000, 7.5, 20), 3723963.94)


    def test_estimate_home_loan_eligibility_edge(self):
        with self.assertRaises(ValueError):
            estimate_home_loan_eligibility(-50000, 20000, 7.5, 20)

    # Credit Card Interest Calculator
    def test_calculate_credit_card_balance_normal(self):
        self.assertAlmostEqual(calculate_credit_card_balance(50000, 36, 6), 44292.12, places=2)

    def test_calculate_credit_card_balance_edge(self):
        with self.assertRaises(ValueError):
            calculate_credit_card_balance(50000, 36, -1)

    # Taxable Income Calculator
    def test_calculate_taxable_income_normal(self):
        self.assertEqual(calculate_taxable_income(800000, 150000), 650000)

    def test_calculate_taxable_income_edge(self):
        self.assertEqual(calculate_taxable_income(800000, 900000), 0)

    # Budget Planner
    def test_plan_budget_normal(self):
        result = plan_budget(60000, 40000)
        self.assertEqual(result['savings'], 20000)
        self.assertEqual(result['status'], 'Healthy')

    def test_plan_budget_normal(self):
        result = plan_budget(60000, 40000)
        self.assertEqual(result['savings'], 6000.0)  # 30% of 20000
        self.assertEqual(result['investment'], 14000.0)  # 70% of 20000
        self.assertEqual(result['status'], 'Healthy')


    # Net Worth Calculator
    def test_calculate_net_worth_normal(self):
        self.assertEqual(calculate_net_worth(100000, 50000), 50000)

    def test_calculate_net_worth_edge(self):
        self.assertEqual(calculate_net_worth(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
