# Peer To Peer Lending
Peer to Peer (P2P) Lending Sample Application Tech Stack : Python, MongoDB Atlas Cluster (AWS), Unit tests
Application is used by investors and people who are interested in geeting short term loans.

Class Structure :

1. User:
   - Attributes: user_id, username, password, email, balance
   - Methods: register, login, update_profile, check_balance, add_funds, withdraw_funds

2. Investor(User):
   - Attributes: investments
   - Methods: create_investment, view_investments, receive_payment

3. Borrower(User):
   - Attributes: loan_applications
   - Methods: apply_for_loan, view_loan_applications, make_payment

4. Loan:
   - Attributes: loan_id, borrower, amount, interest_rate, duration, status
   - Methods: calculate_total_payment, check_status

5. RiskProfile:
   - Attributes: profile_id, risk_score
   - Methods: add_profile, update_profile, get_profile, remove_profile

6. P2PLendingApp:
   - Attributes: users, loans, risk_profiles
   - Methods: register_user, login_user, create_loan, approve_loan, repay_loan, invest_in_loan
