import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

df = pd.read_csv(
    r"C:\Users\adisr\OneDrive\Documents\ml\ml_alpha\Projects\exoplanets\nasa_exoplanets.csv",
    comment="#"
)

# Select the desired columns
exo = df[
    [
        'pl_rade',
        'pl_orbper',
        'disc_year',
        'discoverymethod',
        'sy_dist',
        'pl_bmasse'
    ]
].copy()

# Rename the columns
exo.rename(
    columns={
        'pl_rade': 'radius',
        'pl_orbper': 'orbital_period',
        'disc_year': 'discovery_year',
        'discoverymethod': 'discovery_method',
        'sy_dist': 'distance',
        'pl_bmasse': 'mass'
    },
    inplace=True
)

print(exo.head())