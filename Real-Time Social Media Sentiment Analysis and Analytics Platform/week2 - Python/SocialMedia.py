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

# Drop rows where post_text is 'No content'
df_post= df_post[df_post['post_text'] != 'No content']
print("Data after dropping rows where post_text is 'No content':")
print(df_post)


# changing of date format
df_user['date_joined'] = pd.to_datetime(df_user['date_joined'], dayfirst=True)
df_post['post_date'] = pd.to_datetime(df_post['post_date'], dayfirst=True)

# Display cleaned data
print("Cleaned user details:")
print(df_user)

print("\nCleaned post details:")
print(df_post)

# Merge user and post dataframes on user_id
merged_df = pd.merge(df_post, df_user, on='user_id', how='inner')
print("Merged DataFrame with user details and posts:")
print(merged_df)

# Save the merged DataFrame as a CSV file
merged_df.to_csv("C:/Users/Swetha/Downloads/merged_user_post_data.csv", index=False)
print("Merged data has been saved as 'merged_user_post_data.csv'.")



# sentiment Analysis

# Filter posts with positive sentiment
positive_posts = merged_df[merged_df['sentiment_score'] > 0]
print("Positive sentiment posts:")
print(positive_posts, "\n")


# Counting Posts by Platform
post_count_by_platform = merged_df['platform'].value_counts()
print("Number of posts by platform:")
print(post_count_by_platform, "\n")

# Count neutral posts by platform
neutral_posts = merged_df[merged_df['sentiment_score'] == 0]
neutral_post_count_by_platform = neutral_posts.groupby('platform').size().reset_index(name='neutral_post_count')
print("Number of neutral sentiment posts by platform:")
print(neutral_post_count_by_platform)










