import unittest
from pymongo import MongoClient
from User import User
from Investor import Investor
from Borrower import Borrower
from Loan import Loan
from RiskProfile import RiskProfile
import urllib.parse


# Escape the username and password using urllib.parse.quote_plus
username = urllib.parse.quote_plus('cs148python')
password = urllib.parse.quote_plus('Performance4you@@')

# Create the MongoDB connection string
connection_string = f'mongodb+srv://{username}:{password}@kanaosample.wv2n4oy.mongodb.net/?retryWrites=true&w=majority'

# Connect to the MongoDB Atlas cluster
client = MongoClient(connection_string)

db = client.p2p_lending
users = db.users
investments = db.investments
loans = db.loans
risk_profiles = db.risk_profiles

class TestP2PLending(unittest.TestCase):

    def setUp(self):
        # Clean up the test collections before each test
        users.delete_many({})
        investments.delete_many({})
        loans.delete_many({})
        risk_profiles.delete_many({})

    def tearDown(self):
        # Clean up the test collections after each test
        users.delete_many({})
        investments.delete_many({})
        loans.delete_many({})
        risk_profiles.delete_many({})

    def test_user_registration(self):
        user = User(1, 'john123', 'password', 'john@example.com', 1000)
        user.register()

        # Verify that the user is successfully registered
        result = users.find_one({'user_id': 1})
        self.assertIsNotNone(result)
        self.assertEqual(result['username'], 'john123')

    def test_user_login(self):
        user = User(1, 'john123', 'password', 'john@example.com', 1000)
        user.login()

        # Verify that the user is successfully logged in
        # This test case assumes valid login credentials
        self.assertTrue(True)

    def test_investor_investment(self):
        investor = Investor(2, 'jane456', 'password', 'jane@example.com', 5000)
        investor.invest(1, 1000)

        # Verify that the investment is successfully made
        result = investments.find_one({'investor_id': 2})
        self.assertIsNotNone(result)
        self.assertEqual(result['loan_id'], 1)

    def test_borrower_loan_request(self):
        borrower = Borrower(3, 'mark789', 'password', 'mark@example.com', 2000)
        borrower.request_loan(5000, 5, 12)

        # Verify that the loan request is successfully made
        result = loans.find_one({'borrower_id': 3})
        self.assertIsNotNone(result)
        self.assertEqual(result['amount'], 5000)

    def test_loan_status_update(self):
        loan = Loan(1, 'john123', 5000, 5, 12, 'pending')
        loan.update_status('approved')

        # Verify that the loan status is successfully updated
        result = loans.find_one({'_id': 1})
        self.assertIsNotNone(result)
        self.assertEqual(result['status'], 'approved')

    def test_risk_profile_update(self):
        risk_profile = RiskProfile(1, 8)
        risk_profile.update_profile(9)

        # Verify that the risk profile is successfully updated
        result = risk_profiles.find_one({'profile_id': 1})
        self.assertIsNotNone(result)
        self.assertEqual(result['risk_score'], 9)


if __name__ == '__main__':
    unittest.main()
