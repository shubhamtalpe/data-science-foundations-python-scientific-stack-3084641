# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
img = img.copy()  # make img writable
plt.imshow(img)

#%%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5

# Left side
img[350:850, 190:195, 0:2] = 0
img[350:850, 190:195, 2] = 255

# Right side
img[350:850, 680:685, 0:2] = 0
img[350:850, 680:685, 2] = 255

# Top side
img[350:355, 190:685, 0:2] = 0
img[350:355, 190:685, 2] = 255

#Bottom side
img[845:850, 190:685, 0:2] = 0
img[845:850, 680:685, 2] = 255

plt.imshow(img)
# %%
