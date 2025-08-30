import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_adult_adhd(data):
    # Perform statistical analysis on adult ADHD data
    summary = data.describe()
    plt.figure(figsize=(10, 6))
    sns.histplot(data['adhd_score'], bins=30, kde=True)
    plt.title('Distribution of ADHD Scores in Adults')
    plt.xlabel('ADHD Score')
    plt.ylabel('Frequency')
    plt.show()
    return summary

def analyze_autism(data):
    # Perform statistical analysis on autism data
    summary = data.describe()
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='autism_diagnosis', y='age', data=data)
    plt.title('Age Distribution by Autism Diagnosis')
    plt.xlabel('Autism Diagnosis')
    plt.ylabel('Age')
    plt.show()
    return summary

def generate_insights(data):
    # Generate insights from the processed data
    insights = {
        'total_records': len(data),
        'average_age': data['age'].mean(),
        'adhd_prevalence': data['adhd'].mean() * 100,
        'autism_prevalence': data['autism'].mean() * 100
    }
    return insights