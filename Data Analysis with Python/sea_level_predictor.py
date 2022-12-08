import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    m = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years = range(df['Year'].min(), 2051)
    t = [round(m.slope * i + m.intercept, 7) for i in years]
    plt.plot(years, t, 'r-')
  
    # Create second line of best fit
    df_twenty = df[df['Year'] >= 2000]

    m2 = linregress(df_twenty['Year'], df_twenty['CSIRO Adjusted Sea Level'])

    years2 = range(df_twenty['Year'].min(), 2051)

    t2 = [m2.slope * i + m2.intercept for i in years2]

    plt.plot(years2, t2, 'g-')
    

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()