import matplotlib.pyplot as plt

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel('# of times i heard someone say "data science"')

#if you dont, matplotlib will make axe X as 0, 1
#and add a +2.013e3 off in conner
plt.ticklabel_format(useOffset=False)

#Axe Y show just above 500
plt.axis([2016.5, 2018.5, 499, 506])
plt.title('Look at the "Huge" increase!')
plt.show()
