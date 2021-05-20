import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])

columns = list(df.columns[1:])

for col in columns:
    print("Topper in",col,"is",df.loc[df[col]==df[col].max(), 'Name'].iloc[0])

df['Total'] = df.sum(axis=1)

toppers = df.nlargest(3, ['Total'])['Name'].values
print("\nBest students in the class are: %s first rank, %s second rank, %s third rank" %(toppers[0], toppers[1], toppers[2]))

print("\nThe time complexity of finding the best 3 students is O(nlog3)")