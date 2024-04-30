# import matplotlib.pyplot as plt
# x = [1950,1970,1990,2010,2030,2050]
# y = [3.56,2.6,2.8,4.6,5.7,6.9]
# plt.plot(x,y)
# plt.show()


# The code in the script already includes plt.show() and plt.clf() calls; plt.show() displays a plot; plt.clf() cleans it up again so you can start afresh.

# In Python, a histogram is a graphical representation of the distribution of numerical data

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')  x-axis per logarithmic scale show hoga

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title
plt.title(title)

# After customizing, display the plot
plt.show()