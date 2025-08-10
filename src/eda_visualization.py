import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda():
    df = pd.read_csv("data/Crop_recommendation.csv")
    mean_values = df.groupby('label').mean(numeric_only=True).reset_index()

    plt.rcParams['figure.figsize'] = (16, 10)
    plt.subplots_adjust(hspace=0.5, wspace=0.3)

    features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

    for i, feature in enumerate(features, start=1):
        plt.subplot(2, 4, i)
        sns.barplot(x=feature, y='label', data=mean_values, palette="viridis")
        plt.xlabel(f'Mean {feature.capitalize()}', fontsize=10)
        plt.ylabel('Crop', fontsize=10)

    plt.suptitle('Visualizing Mean Conditions Across Crops', fontsize=18)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
