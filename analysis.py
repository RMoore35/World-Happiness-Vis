import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('world_happiness_2019.csv')
print(df)

# Get the Overall Rank and score columns
rank = df['Overall rank']
score = df['Score']

# Lets start with a very basic plot of the Happiness Score vs. the Overall Rank
plt.plot(rank, score)
plt.show()

# Next, lets build on that plot and add a title, and x and y axis labels
plt.plot(rank, score)
plt.title('Happiness Score vs World Rank')
plt.xlabel('Country Rank')
plt.ylabel('Country Score')
plt.show()

# Next, lets read in the GDP per capita and Healthy life expectancy columns and plot
# Then, we'll start witha basic plot
gdp = df['GDP per capita']
lifeExp = df['Healthy life expectancy']
plt.plot(rank, gdp)
plt.plot(rank, lifeExp)
plt.show()

# I will look at the plot of World Rank vs. GDP and Life Expectancy two different ways
# Option 1
plt.plot(rank, gdp)
plt.plot(rank, lifeExp)
plt.title('World Rank vs GDP and Life Expectancy')
plt.xlabel('Country Rank')
plt.legend(['GDP', 'Life Expectancy'])
plt.show()

# Option 2
plt.plot(rank, gdp, color='green')
plt.plot(rank, lifeExp, color='blue')
plt.title('World Rank vs GDP and Life Expectancy')
plt.xlabel('Country Rank')
plt.legend(['GDP', 'Life Expectancy'])
plt.show()

# Next, lets look at a scatter plot of Happiness Score vs. GDP
# to see what trends there are.
plt.scatter(gdp, score)
plt.title('Happiness Score vs. GDP')
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness Score')
plt.ylim(0, 8)
plt.show()

# Lets next create a histogram to see what the distribution of happiness score looks like
plt.hist(score, bins=10)
plt.title('Happiness Score Distribution')
plt.xlabel('Happiness Score')
plt.ylabel('Frequency')
plt.show()

# Next, for our last plot, we will note that it may be easier to see integers
# counted in the histogram, rather than some of the scores being in decimal form
roundedHappinessScore = score.apply(int)
count = roundedHappinessScore.value_counts()
hapScore = count.index

# And let's plot
plt.bar(hapScore, count)
plt.title('Happiness Scores')
plt.xlabel('Score')
plt.ylabel('Count')
plt.show()
