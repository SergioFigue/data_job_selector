import matplotlib.pyplot as plt

# reporting functions


def visualizing_histogram(data, country, job):
    fig, chart = plt.subplots(figsize=(12, 5))

    chart.hist(data, bins=50, facecolor='green')

    chart.set_xlabel('Age')
    chart.set_ylabel('Workers')
    chart.set_title(f'Age distribution for {job} workers from {country}')

    plt.show()


def reporting(result):

    return result.to_csv(f'./data/results/your_mvi_report.csv', index=False)
