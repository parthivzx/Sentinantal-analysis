# Drug Review Sentiment Analysis

This is a Natural Language Processing (NLP) based project that analyzes drug reviews and predicts user sentiment (positive, negative, or neutral) using machine learning. Final results are visualized with an interactive Power BI dashboard.

## 🔍 Features
- Text cleaning and preprocessing
- TF-IDF vectorization
- Sentiment classification using Logistic Regression
- Evaluation metrics (accuracy, confusion matrix, classification report)
- Power BI dashboard with visual insights

## 📁 Files Included
- data_cleaning.py: Clean raw review data
- nlp.py: Text processing and vectorization
- feature_engineering.py: Train-test split and saving datasets
- model_evaluator.py: Train and evaluate model
- sentiment analysis project.pbix: Power BI dashboard
- model_predictions.csv, metrics.txt, and plots

## 📊 Dashboard Features
- Sentiment Distribution
- Review Trends by Year
- Top Conditions Reviewed
- Review Length by Sentiment
- Rating Distribution

  ## 🧠 Project Workflow

1. Data Cleaning: Removed unnecessary characters, converted text to lowercase, formatted date columns.
2. NLP Preprocessing: Used TF-IDF to convert text into numerical features.
3. Feature Engineering: Split the dataset into train and test sets, and saved them for reuse.
4. Model Training: Used Logistic Regression to train on the TF-IDF features.
5. Evaluation: Calculated accuracy, classification report, confusion matrix.
6. Visualization: Built a Power BI dashboard using the model results and cleaned dataset.


## ⚙ How to Run
python data_cleaning.py
python nlp.py
python feature_engineering.py
python model_evaluator.py
