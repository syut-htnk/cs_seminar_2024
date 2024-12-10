import matplotlib.pyplot as plt
import pandas as pd

# Load Tsv file
data = pd.read_csv('./tsv/utsumi.tsv', sep='\t')
print('Header Column', data.columns)


# Plotting 
plt.plot(data['Gaze point X'], data['Gaze point Y'])
plt.xlabel('Gaze point X')
plt.ylabel('Gaze point Y')
plt.show()

# Plot other X-Y pairs
# Plot each X-Y pair with colors based on 'Recording Timestamp'
# If the Y column exists, plot the X-Y pair
for x_col in [col for col in data.columns if 'X' in col]:
    y_col = x_col.replace('X', 'Y')
    if y_col in data.columns:
        plt.figure()
        plt.scatter(data[x_col], data[y_col], c=data['Recording timestamp'], cmap='viridis')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{x_col} vs {y_col}')
        plt.colorbar(label='Recording Timestamp')
        plt.show()