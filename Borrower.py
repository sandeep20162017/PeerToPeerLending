from pymongo import MongoClient
from User import User

class Borrower(User):
    def __init__(self, user_id, username, password, email, balance):
        super().__init__(user_id, username, password, email, balance)
        self.loans = []

    def request_loan(self, amount, interest_rate, duration):
        """Request a new loan by inserting the loan details into the 'loans' collection."""
        client = MongoClient('mongodb+srv://cs148python:{hide password}@@kanaosample.wv2n4oy.mongodb.net/?retryWrites=true&w=majority')
        db = client.p2p_lending
        loans = db.loans

        loan_data = {
            'borrower_id': self.user_id,
            'amount': amount,
            'interest_rate': interest_rate,
            'duration': duration,
            'status': 'pending'
        }
        result = loans.insert_one(loan_data)
        loan_id = result.inserted_id
        client.close()
        self.loans.append((loan_id, amount, interest_rate, duration))
        print("Loan requested successfully.")

    def view_loans(self):
        """View the list of loans requested by the borrower."""
        print("Loans:")
        for loan in self.loans:
            loan_id, amount, interest_rate, duration = loan
            print(f"Loan ID: {loan_id}, Amount: {amount}, Interest Rate: {interest_rate}, Duration: {duration}")
