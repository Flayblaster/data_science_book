from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.7, 10289.7, 14598.3]

#Make a line graphic, years in X and gdp in Y
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

#Add a title
plt.title('Nominal GDP')

#Add a rotule to X axis
plt.xlabel('BIllions of $')
plt.show()