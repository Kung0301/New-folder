import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('hello-world-firebase-2f6d8-firebase-adminsdk-bsqr2-dc73c9f372.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hello-world-firebase-2f6d8-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('restricted_access/secret_document')
print(ref.get())