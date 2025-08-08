import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# Sample dataset
data = {
    'ticket': [
        'Cannot access email', 'Website is down', 'Forgot password',
        'Server is slow', 'Need new mouse', 'Laptop overheating',
        'Internet is not working', 'Software installation request',
        'VPN connection fails', 'Blue screen error'
    ],
    'category': [
        'Access Issue', 'Server Issue', 'Access Issue',
        'Server Issue', 'Hardware', 'Hardware',
        'Network', 'Software', 'Network', 'Hardware'
    ]
}

df = pd.DataFrame(data)

# Vectorizer and classifier for category
category_vectorizer = TfidfVectorizer()
X_category = category_vectorizer.fit_transform(df['ticket'])
y_category = df['category']
category_classifier = MultinomialNB()
category_classifier.fit(X_category, y_category)

# Save category model and vectorizer
joblib.dump(category_classifier, 'category_classifier.joblib')
joblib.dump(category_vectorizer, 'category_vectorizer.joblib')

# Optional: Duplicate for presence detection (dummy example)
# In real usage, this would be a separate dataset/task
presence_labels = ['yes' if c != 'Hardware' else 'no' for c in y_category]  # Dummy presence label
presence_vectorizer = TfidfVectorizer()
X_presence = presence_vectorizer.fit_transform(df['ticket'])
presence_classifier = MultinomialNB()
presence_classifier.fit(X_presence, presence_labels)

# Save presence model and vectorizer
joblib.dump(presence_classifier, 'presence_classifier.joblib')
joblib.dump(presence_vectorizer, 'presence_vectorizer.joblib')

print("✅ All 4 model and vectorizer files saved successfully.")
