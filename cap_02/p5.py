import matplotlib.pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
print(xs)

#We can make multy layers for plt.plot, to show up multy series in the same graphic
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label='bias^2')

plt.plot(xs, total_error, 'b:', label='total error')

#As we assign labels for each serie, can we make a legend too
plt.legend(loc=9)
plt.xlabel('model complexity')
plt.xticks([])
plt.title('the Bias-Variance Tradeoff')
plt.show()