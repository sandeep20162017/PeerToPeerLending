from pymongo import MongoClient

class Loan:
    def __init__(self, loan_id, borrower, amount, interest_rate, duration, status):
        self.loan_id = loan_id
        self.borrower = borrower
        self.amount = amount
        self.interest_rate = interest_rate
        self.duration = duration
        self.status = status

    def update_status(self, new_status):
        """Update the status of a loan in the 'loans' collection."""
        client = MongoClient('mongodb+srv://cs148python:{hide password}@@kanaosample.wv2n4oy.mongodb.net/?retryWrites=true&w=majority')
        db = client.p2p_lending
        loans = db.loans

        filter_query = {'_id': self.loan_id}
        update_query = {'$set': {'status': new_status}}
        loans.update_one(filter_query, update_query)
        client.close()
        self.status = new_status
        print("Loan status updated successfully.")
