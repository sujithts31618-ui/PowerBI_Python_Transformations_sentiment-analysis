# PowerBI_Python_Transformations_sentiment-analysis
Python scripts demonstrating data transformations, text cleaning, and advanced Sentiment Analysis for Power BI projec


## 🧠 Project Overview
This project analyzes **customer feedback** to measure sentiment and satisfaction.  
It identifies the **volume of Positive, Negative, and Neutral feedback** and visualizes it in **Power BI** dashboards.

## 🧩 Data Flow
1. **Raw Feedback Data** collected from surveys or support channels.  
2. **Python Script (`text_processing.py`)**:
   - Cleans text (lowercase, remove punctuation)  
   - Corrects common spelling issues  
   - Calculates sentiment polarity using TextBlob  
   - Categorizes as **Positive / Negative / Neutral**  
3. **Processed Output (`processed_feedback.csv`)**:
   - Contains original feedback, sentiment score, sentiment label  
4. **Power BI Report**:
   - Visualizes sentiment distribution and trends
  
## 🧰 Script Description (`text_processing.py`)```python
# Steps:
# 1. Clean and normalize text
# 2. Correct common spelling issues
# 3. Calculate sentiment polarity using TextBlob
# 4. Label feedback as Positive / Negative / Neutral
# 5. Export cleaned and categorized data for Power BI
  
## 📊 Power BI Report
- **Bar Chart:** Volume of Positive, Negative, and Neutral feedback

## 🚀 Business Impact
- Helped **Customer Experience Team** identify recurring negative feedback topics.

- 🧑‍💻 Author

Sujith T S
Power BI Developer | 
