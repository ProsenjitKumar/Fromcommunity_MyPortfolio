# import the pyplot library

import matplotlib.pyplot as plotter

# Guest age group

ageGroupLabel = 'Below 5', '5-10', '10-15', '15-20', '20-30', '30-40', '40-50', '50-60', '60-80', '80-100', 'Above 100'

# Number of Guests expected in age group

guestNumbers = [5, 10, 10, 15, 10, 30, 25, 25, 20, 15, 10]

figureObject, axesObject = plotter.subplots()

explode = (0.4, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.3)

colors = ("red", "green", "orange", "cyan", "brown", "grey", "blue", "indigo", "beige", "yellow")

# Draw the pie chart

axesObject.pie(guestNumbers,

               explode=explode,

               colors=colors,

               labels=ageGroupLabel,

               autopct='%1.2f',

               startangle=90)

# Aspect ratio

axesObject.axis('equal')

plotter.show()