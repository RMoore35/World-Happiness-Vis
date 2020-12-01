import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('WorldHappiness2018_Data.csv')
print(df)

rank = df['Rank']
score = df['Score']

plt.plot(rank, score)
plt.show()

plt.plot(rank, score)
plt.title('Happiness Score vs World Rank')
plt.xlabel('Country Rank')
plt.ylabel('Country Score')
plt.show()

gdp = df['GDP_Per_Capita']
lifeExp = df['Healthy_Life_Expectancy']
plt.plot(rank, gdp)
plt.plot(rank, lifeExp)
plt.show()

# Option 1
plt.plot(rank, gdp)
plt.plot(rank, lifeExp)
plt.title('World Rank vs GDP and Life Expectancy')
plt.xlabel('Country Rank')
plt.legend()
plt.show()

# Option 2
plt.plot(rank, gdp, color='green')
plt.plot(rank, lifeExp, color='blue')
plt.title('World Rank vs GDP and Life Expectancy')
plt.xlabel('Country Rank')
plt.legend()
plt.show()

plt.scatter(gdp, score)
plt.title('GDP vs Happiness Score')
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness Score')
plt.ylim(0, 8)
plt.show()

plt.hist(score)
plt.title('Happiness Score Distribution')
plt.xlabel('Happiness Score')
plt.ylabel('Frequency')
plt.show()

roundedHappinessScore = score.apply(int)
count = roundedHappinessScore.value_counts()
hapScore = count.index

plt.bar(hapScore, count)
plt.title('Happiness Scores')
plt.xlabel('Score')
plt.ylabel('Count')
plt.show()
