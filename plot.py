import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StationsHolland.csv')
print(df.head())

boundingBox = (df.x.min(),   df.x.max(),
               df.y.min(), df.y.max())

print(boundingBox)
