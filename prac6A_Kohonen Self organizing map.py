
import numpy as np
import matplotlib.pyplot as pl 
from minisom import MiniSom
# Define the color data (RGB values) 
colors = np.array(
[[0., 0., 0.],
[0., 0., 1.],
[0., 0., 0.5],
[0.125, 0.529, 1.0],
[0.33, 0.4, 0.67],
[0.6, 0.5, 1.0],
[0., 1., 0.],
[1., 0., 0.],
[0., 1., 1.],
[1., 0., 1.],
[1., 1., 0.],
[1., 1., 1.],
[.33, .33, .33],
[.5, .5, .5],
[.66, .66, .66]])

# Define corresponding color names 
color_names = [
'black', 'blue', 'darkblue', 'skyblue',
'greyblue', 'lilac', 'green', 'red',
'cyan', 'violet', 'yellow', 'white', 'darkgrey', 'mediumgrey', 'lightgrey'
]

# Initialize and train the SOM (Self-Organizing Map)
som = MiniSom(20, 30, 3, sigma=1.0, learning_rate=0.5) 
# Grid size (20, 30) and 3 input features (RGB) 
som.train(colors, 100) # Train the SOM for 100 iterations

# Plot the distance map of the SOM 
pl.imshow(som.distance_map().T, cmap='bone', origin='lower')
# Map each color to its corresponding position on the SOM 
for i, color in enumerate(colors):
    x, y = som.winner(color) 
    # Find the best matching unit for the color 
    pl.text(y, x, color_names[i], ha='center',
va='center', bbox=dict(facecolor='white', alpha=0.5, lw=0))
# Display the plot with the color names 
pl.title('Color SOM')
pl.show()
