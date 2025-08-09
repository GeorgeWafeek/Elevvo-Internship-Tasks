import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(
    "C:/Users/gogow/PycharmProjects/Elevvo Internship/kaggle_survey_2017.csv",
    dtype=str
)

# Clean data
df.drop_duplicates(inplace=True)
df.fillna("Not Answered", inplace=True)

# Standardize country format
df['Country'] = df['Country'].str.strip().str.title()

# Preview
df.info()
print(df.head())

# Set style
sns.set(style="whitegrid")
fig, axes = plt.subplots(3, 2, figsize=(14, 12))
fig.suptitle("Kaggle Data Science Survey 2017 - Top Insights", fontsize=16, fontweight='bold')

# 1- Gender Distribution
gender_counts = df['GenderSelect'].value_counts().head(5)
sns.barplot(x=gender_counts.values, y=gender_counts.index, ax=axes[0,0])
axes[0,0].set_title("Gender Distribution")

# 2- Top 5 Countries
country_counts = df['Country'].value_counts().head(5)
sns.barplot(x=country_counts.values, y=country_counts.index, ax=axes[0,1])
axes[0,1].set_title("Top 5 Countries")

# 3- Top 5 Job Titles
job_counts = df['CurrentJobTitleSelect'].value_counts().head(5)
sns.barplot(x=job_counts.values, y=job_counts.index, ax=axes[1,0])
axes[1,0].set_title("Top 5 Job Titles")

# 4- Top 5 Recommended Languages
lang_counts = df['LanguageRecommendationSelect'].value_counts().head(5)
sns.barplot(x=lang_counts.values, y=lang_counts.index, ax=axes[1,1])
axes[1,1].set_title("Top 5 Recommended Languages")

# 5- Top 5 Learning Platforms
platform_counts = df['LearningPlatformSelect'].value_counts().head(5)
sns.barplot(x=platform_counts.values, y=platform_counts.index, ax=axes[2,0])
axes[2,0].set_title("Top 5 Learning Platforms")

# Remove last empty subplot
axes[2,1].axis('off')
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
