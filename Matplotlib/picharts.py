import matplotlib.pyplot as plotter


# Distribution of n-grams in a paragraph - maximum wordlength 5

wedgeLabels = ("Unigram", "Bigram", "Trigram", "Four-gram", "Five-gram", "Others")

# Percentage of n-grams

ngramPercent = (5, 5, 10, 5, 10, 65)

figureObject, axesObject = plotter.subplots()

axesObject.pie(ngramPercent,

               labels=wedgeLabels,

               shadow=True,

               frame=True,

               startangle=120,

               autopct='%.1f%%',

               wedgeprops={'linewidth': 3,

                           'edgecolor': "orange"})

axesObject.axis('equal')

plotter.show()