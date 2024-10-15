import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  print(df.columns)
  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  filtered_df = df[df['sex'] == 'Male']

  average_age_men = filtered_df['age'].mean().round(decimals=1)

  # What is the percentage of people who have a Bachelor's degree?
  filtered_df = df[df['education'] == 'Bachelors']
  partial = len(filtered_df)
  total = len(df)
  percentage_bachelors = round((partial / total) * 100)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  filtered_df_degree = df[df['education'].isin(
    ['Bachelors', 'Masters', 'Doctorate'])]
  total_degree = len(filtered_df_degree)

  educational_high_degree = filtered_df_degree[filtered_df_degree['salary'] ==
                                               '>50K']
  partial_high_degree = len(educational_high_degree)
  total_high_degree = len(filtered_df_degree)
  """educational_low_degree = filtered_df_degree[filtered_df_degree['salary'] == '<=50K']
  partial_low_degree=len(educational_low_degree)
  total_low_degree=len(filtered_df_degree) """

  # What percentage of people without advanced education make more than 50K?
  filtered_df_low = df[-df['education'].
                       isin(['Bachelors', 'Masters', 'Doctorate'])]
  total_not_degree = len(filtered_df_low)

  educational_low = filtered_df_low[filtered_df_low['salary'] == '>50K']
  partial_low = len(educational_low)
  total_low = len(filtered_df_low)

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = round((total_degree / total) * 100)
  lower_education = round((total_not_degree / total) * 100)

  # percentage with salary >50K
  higher_education_rich = round(
    (partial_high_degree / total_high_degree) * 100)
  lower_education_rich = round((partial_low / total_low) * 100)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  df_filter_1 = df[df['hours-per-week'] == min_work_hours]
  df_filter_2 = df_filter_1[df_filter_1['salary'] == '>50K']
  num_min_workers = len(df_filter_2)

  rich_percentage = round((num_min_workers / total) * 100)

  # What country has the highest percentage of people that earn >50K?
  highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts()/ df['native-country'].value_counts() * 100).sort_values(ascending=False).fillna(0).idxmax()
  highest_earning_country_percentage = round(len(df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')]) / len(df[(df['native-country'] == highest_earning_country)])*100,1)

  # Identify the most popular occupation for those who earn >50K in India.
  top_IN_occupation = df[(df['salary'] == ">50K") & (df['native-country'] == "India")]["occupation"].value_counts().index[0]

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich': higher_education_rich,
    'lower_education_rich': lower_education_rich,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }
