import datetime
from typing import NamedTuple
import random

class ExperimentResult:
    def __init__(self, N: int, mean_delta: datetime.timedelta, measurements: int) -> None:
        self.N = N
        self.ops = (2 + 3 + 3) * N // 100 + 3 * N
        self.measurements = measurements
        self.mean_delta = mean_delta


def run_algorithm(N: int) -> datetime.timedelta:
    start = datetime.datetime.now()

    table = {k: [] for k in range(N // 100)}  # 2 * N // 100

    for i in range(N):  # 1
        pos = random.randint(0, len(table.keys()) - 1)  # N
        num = random.randint(1, 100)  # N
        table[pos].append(num)  # N

    n_min = min(len(v) for v in table.values())  # 3 * N // 100
    n_max = max(len(v) for v in table.values())  # 3 * N // 100

    end = datetime.datetime.now()

    return end - start


def run_experiment(N: int, m: int) -> ExperimentResult:
    deltas_sum = datetime.timedelta()
    for i in range(m):
        deltas_sum += run_algorithm(N)
    return ExperimentResult(
        N=N,
        measurements=m,
        mean_delta=deltas_sum / m
    )


if __name__ == '__main__':
    Ns = [100, 1_000, 10_000, 100_000]
    m = 100
    print('{:>10} {:>10} {:>10} {:>10} {:>10}'.format('N', 'm', 'ops.', 'mean µs', 'ops./µs'))
    for N in Ns:
        result = run_experiment(N, m)
        print(f'{N:10} {m:10} {result.ops:10} {result.mean_delta.microseconds:10} {result.ops / result.mean_delta.microseconds:10.3f}')

