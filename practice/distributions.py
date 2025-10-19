# python -m pip install numpy matplotlib
import numpy as np
import matplotlib.pyplot as plt

# The simple function below can be used to automatically produce a plot illustrating a distribution of samples.
def distribution_plot(samples, bins=100, figsize=(5,3)):
    
    '''
    Helper function to visualise the distributions
    
    Params:
    -----
    samples: np.ndarray
        A numpy array of quantitative data to plot as a histogram.
        
    bins: int, optional (default=100)
        The number of bins to include in the histogram
        
    figsize: (int, int) (default=(5,3))
        Size of the plot in pixels
        
    Returns:
    -------
        fig, ax: a tuple containing matplotlib figure and axis objects.
    '''
    hist = np.histogram(samples, bins=bins, 
                        density=True)

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot()
    _ = ax.plot(hist[0])
    _ = ax.set_ylabel('p(x)')
    _ = ax.set_xlabel('x')
    
    return fig, ax

# Creating a random number generator object
rng = np.random.default_rng()
print( type(rng))
print(rng)

# Steps to create a sample
# In general, the approach to sampling is:

  # Create a random number generator object
  # Using the object call the method for the statistical distribution
  # Each method has its own custom parameters
  # Each method will include a size parameter that you use to set the number of samples to generate
  # Store the result in an appropriately named variab

# Step 1: create a random number generator object - set seed to 42(every time you run, you get same results)
rng = np.random.default_rng(42)

# Step 2 and 3: call the appropriate method of the generator and store result
# range for uniform distribution between 10 and 40
samples = rng.uniform(low=10, high=40, size=1_000_000)

# Illustrate with plot.
_ = distribution_plot(samples, bins=50)