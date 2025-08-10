import sys
from src import eda_visualization, model_training

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [train|eda]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "train":
        print("Training model...")
        model_training.train_model()
    elif command == "eda":
        print("Performing exploratory data analysis...")
        eda_visualization.perform_eda()
    else:
        print(f"Unknown command '{command}'. Use 'train' or 'eda'.")

if __name__ == "__main__":
    main()
