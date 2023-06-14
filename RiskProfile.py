from pymongo import MongoClient

class RiskProfile:
    def __init__(self, profile_id, risk_score):
        self.profile_id = profile_id
        self.risk_score = risk_score

    def add_profile(self):
        """Add a new risk profile to the 'risk_profiles' collection."""
        client = MongoClient('mongodb+srv://cs148python:{hide password}@@kanaosample.wv2n4oy.mongodb.net/?retryWrites=true&w=majority')
        db = client.p2p_lending
        risk_profiles = db.risk_profiles

        profile_data = {
            'profile_id': self.profile_id,
            'risk_score': self.risk_score
        }
        risk_profiles.insert_one(profile_data)
        client.close()
        print("Risk profile added successfully.")

    def update_profile(self, new_risk_score):
        """Update an existing risk profile in the 'risk_profiles' collection based on profile_id."""
        client = MongoClient('mongodb+srv://cs148python:{hide password}@@kanaosample.wv2n4oy.mongodb.net/?retryWrites=true&w=majority')
        db = client.p2p_lending
        risk_profiles = db.risk_profiles

        filter_query = {'profile_id': self.profile_id}
        update_query = {'$set': {'risk_score': new_risk_score}}
        risk_profiles.update_one(filter_query, update_query)
        client.close()
        self.risk_score = new_risk_score
        print("Risk profile updated successfully.")

    def remove_profile(self):
        """Remove a risk profile from the 'risk_profiles' collection based on profile_id."""
        client = MongoClient('mongodb+srv://cs148python:{hide password}@@kanaosample.wv2n4oy.mongodb.net/?retryWrites=true&w=majority')
        db = client.p2p_lending
        risk_profiles = db.risk_profiles

        query = {'profile_id': self.profile_id}
        risk_profiles.delete_one(query)
        client.close()
        print("Risk profile removed successfully.")
