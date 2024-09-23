import pandas as pd

import numpy as np
df_user=pd.read_csv("C:/Users/Swetha/Downloads/user_details.csv")
print(df_user, "\n")
df_post = pd.read_csv("C:/Users/Swetha/Downloads/post_fact.csv")
print(df_post)

# cleaning the data
df_user.columns = df_user.columns.str.strip()
df_post.columns = df_post.columns.str.strip()


df_user['user_name'] = df_user['user_name'].str.strip().replace('', np.nan)
df_user['location']= df_user['location'].str.strip().replace('', np.nan)
# 1. Handling missing values in user_details
df_user['user_name'] = df_user['user_name'].fillna('Anonymous_user')
df_user['location']= df_user['location'].fillna('Unknown')

print("After changing the null value\n")
print(df_user)

# 2. Handling missing values in post_details
df_post['post_text'] = df_post['post_text'].str.strip().replace('', np.nan)
df_post['platform'] = df_post['platform'].str.strip().replace('', np.nan)
df_post['post_text'] = df_post['post_text'].fillna('No content')
df_post['platform'] = df_post['platform'].fillna('Diff_source')

print("After changing the null value\n")
print(df_post)

# dropping th users who have commented from different_sources
df_post_filtered = df_post[df_post['platform'] != 'Diff_source']
print("Data after dropping users who have platform as 'Diff_source':")
print(df_post_filtered)

# changing of date format
df_user['date_joined'] = pd.to_datetime(df_user['date_joined'], dayfirst=True)
df_post['post_date'] = pd.to_datetime(df_post['post_date'], dayfirst=True)

# Display cleaned data
print("Cleaned user details:")
print(df_user)

print("\nCleaned post details:")
print(df_post)



# sentiment Analysis

# Filter posts with positive sentiment
positive_posts = df_post_filtered[df_post_filtered['sentiment_score'] > 0]
print("Positive sentiment posts:")
print(positive_posts, "\n")


# Counting Posts by Platform
post_count_by_platform = df_post_filtered['platform'].value_counts()
print("Number of posts by platform:")
print(post_count_by_platform, "\n")

# Merge user and post dataframes on user_id
merged_df = pd.merge(df_post_filtered, df_user, on='user_id', how='left')
print("Merged DataFrame with user details and posts:")
print(merged_df)










