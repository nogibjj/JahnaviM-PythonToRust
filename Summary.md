My dataset of choice is on LAPD crime records dating from 2020. To learn more about the raw dataset and relevant columns, please visit: https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data. In my analysis, audience will glean a few key insights:
  (1) Summary Statistics around each column of the data (mean, median, minimum, standard deviation...). 
  (2) A histogram of the time of occurence of crimes according to LAPD.
  (3) A histogram of the target victims' age of crimes reported by LAPD.
  (4) An interactive geoplot of the crime rate in various areas in LA according to LAPD. 

Below is a glimpse of the key insights.

## Summary Statistics:
<img width="1130" alt="image" src="https://github.com/user-attachments/assets/0d2a5c1f-23c5-499a-8079-00024acf578a">
This is a snapshot of the summary statistics for some columns, but running the script will provide the full summary statistics for all columns. Note that the summary statistics are most relevant for continuous variables like "Vict Age". Here, audience can learn that on average, victims are aged around 29 for crimes in LA. This helps to assess that it is not only young people under the age of 25 who are targeted, but rather older people may also be targets of crimes in LA.

## Vicitm Age:
<img width="1113" alt="image" src="https://github.com/user-attachments/assets/fd1bbf6f-cdae-4ce4-82cc-a19407db1ec3">
To continue the analysis on Victim Age from the summary statistics, I proceeded to create this histogram of victim age, specifically for crimes where there was a victim. The previous summary statistic also accounted for cases that were victimless crimes - ie vandilism. In this histogram, we see a skewed distribution, with a peak around 30, but a wide age range, suggesting all ages could be targets for crime.

## Time of Occurence:
<img width="1119" alt="image" src="https://github.com/user-attachments/assets/1f3f54a5-93c0-4957-a656-e3d5716ea906">
The summary statistics of Time of Occurence are not as relevant, so I've created a histogram of the time of occurence. This was insightful as it was interesting to see that crime occurs throughout the day and not only in the nighttime as some people may assume. In reality, around noon we see a large surge in crime and not just in the late hour of the night once the sun has set.

## Geo Plot:

<img width="802" alt="image" src="https://github.com/user-attachments/assets/78da9b8a-37f4-467a-9e20-d22221a6bd30">

Lastly, I created this interactive geographical plot using plotly. When rendered, audience members can interact with the plot to zoom into specific areas in LA and explore which areas are high targets for crime and conduct more analysis. In this plot, at a glance, it is clear that some of the areas with highest crime rate is in the Central are. 
