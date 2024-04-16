"""Plot word counts."""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('results/frankenstein.csv', header=None,
                 names=('word', 'word_frequency'))
df['rank'] = df['word_frequency'].rank(ascending=False,
                                       method='max')
df['inverse_rank'] = 1 / df['rank']
ax = df.plot.scatter(x='word_frequency',
                     y='inverse_rank',
                     figsize=[12, 6],
                     grid=True,
                     xlim=None)
plt.show()
