import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Tips Dataset.csv")

sns.histplot(df["size"], kde=True)
plt.show()

sns.histplot(df["tip"], kde=True)
plt.show()

sns.histplot(df["total_bill"], kde=True)
plt.show()

sns.histplot(df["total_bill"], kde=True)
plt.show()

sns.scatterplot(x="total_bill", y="tip", hue="time", data=df)
plt.show()

sns.pairplot(df, hue="gender")
plt.show()