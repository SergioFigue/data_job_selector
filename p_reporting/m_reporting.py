
# reporting functions


def reporting(result):
    return result.to_csv(f'./data/results/your_mvi_report.csv', index=False)