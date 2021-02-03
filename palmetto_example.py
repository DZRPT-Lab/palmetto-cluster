from numpy.random import normal

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Take samples
smpls = normal(size=2000)

# Create histogram and save it
fig, ax = plt.subplots(1,1)

ax.hist(smpls, bins=50)
ax.set_title('Histogram of Gaussian Values');

plt.savefig('gaussian.png')
