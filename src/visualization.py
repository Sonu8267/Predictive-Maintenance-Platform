import matplotlib.pyplot as plt

def plot_results(actual, predicted):
    plt.plot(actual, label="Actual")
    plt.plot(predicted, label="Predicted")
    plt.legend()
    plt.show()
