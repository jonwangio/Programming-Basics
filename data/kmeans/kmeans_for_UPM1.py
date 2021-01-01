################

# For the support to UPM1 course
# This is a smaple code for unsupervised classification/clustering
# The sample data is based in Wuhan, China
# All image data has been sampled to same resolution and size, covering exactly the same area

# 2020 Dec 15

################

# This code will use few modules: pathlib, Numpy, matplotlib, Scipy and sklearn
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy import ndimage
from sklearn import cluster

# I start to collect the file names of all the *tif image files
file_list = []  # Empty list to store file names
for file in Path('.').glob('*.tif'):
        file_list.append(file)

# You can print to see how the file_list looks like
print(file_list)

# The I started to read the files and stack them together by calling their names
# I will use the 'for' loop to iterate over the names to read files
stack = np.array([])  # Empty array to store the stacked images
for file in file_list:
    img = ndimage.imread(file)  # Read each image file
    print(img.shape)  # Each time, also check the size of the image
    
    # In order to do clustering, image should be reshaped into a single column
    img_col = img.reshape(-1, 1)
    
    # Each time put the reshaped image into the stack
    stack = np.hstack((stack,img_col)) if stack.size else img_col
    # Also to check the size of the stack
    print(stack.shape)
    
# Now, it's time for the Kmeans
# I start to call KMeans function from the sklearn cluster module
# I also choose an arbitrary number of clusters, I can of course change
# Important!! There are already many clustering algorithms other than KMeans in 'sklearn', you can try many things already by only using 'sklearn'
kmean_cluster = cluster.KMeans(n_clusters=5)  # This is a function to be fitted to the data
labels = kmean_cluster.fit_predict(stack)  # Fitting the data

# Visualization
# Because the predicted labels are still in one column, you need to reshape it back to original image shape
row, col = img.shape  # Get the original dimensions of the image
plt.figure(figsize = (5,6))
plt.imshow(labels.reshape(row, col))







    
    
    
    
    
    
    