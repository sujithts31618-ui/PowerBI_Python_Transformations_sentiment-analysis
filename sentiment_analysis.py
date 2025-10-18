# text_processing.py
# This script demonstrates text cleaning and sentiment analysis for Power BI projects

import pandas as pd
from textblob import TextBlob

# Load sample data
df = pd.read_csv('../data/sample_feedback.csv')  # Make sure sample_feedback.csv is in data/ folder

# Step 1: Clean text (lowercase, remove punctuation)
df['Cleaned_Feedback'] = df['Feedback'].str.lower().str.replace(r'[^\w\s]', '', regex=True)

# Step 2: Correct common misspellings (example)
df['Cleaned_Feedback'] = df['Cleaned_Feedback'].replace({'luv': 'love'}, regex=True)

# Step 3: Sentiment analysis
df['Sentiment'] = df['Cleaned_Feedback'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Step 4: Categorize sentiment
df['Sentiment_Label'] = df['Sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

# Show result
print(df)

# Save processed data (optional)
df.to_csv('../data/processed_feedback.csv', index=False)