from pymongo import MongoClient
from User import User

class Investor(User):
    def __init__(self, user_id, username, password, email, balance):
        super().__init__(user_id, username, password, email, balance)
        self.investments = []

    def invest(self, loan_id, amount):
        """Invest in a loan by inserting the investment details into the 'investments' collection."""
        client = MongoClient('mongodb+srv://cs148python:{hide password}@@kanaosample.wv2n4oy.mongodb.net/?retryWrites=true&w=majority')
        db = client.p2p_lending
        investments = db.investments

        investment_data = {
            'loan_id': loan_id,
            'investor_id': self.user_id,
            'amount': amount
        }
        investments.insert_one(investment_data)
        client.close()
        self.investments.append((loan_id, amount))
        print("Investment made successfully.")

    def view_investments(self):
        """View the list of investments made by the investor."""
        print("Investments:")
        for investment in self.investments:
            loan_id, amount = investment
            print(f"Loan ID: {loan_id}, Amount: {amount}")
