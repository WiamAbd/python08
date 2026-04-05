import importlib
from typing import Optional, Any


def check_package(name: str) -> Optional[Any]:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version})")
        return module
    except ImportError:
        print(f"[MISSING] {name}")
        return None


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")

    pandas = check_package("pandas")
    numpy = check_package("numpy")
    matplotlib = check_package("matplotlib")

    if not (pandas and numpy and matplotlib):
        print("\nSome dependencies are missing.\n")
        print("Install them using:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        return

    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    data = numpy.random.randn(1000)

    df = pandas.DataFrame(data, columns=["values"])
    df["values"].mean()
    df["values"].std()

    print("Processing 1000 data points...")

    df["values"].plot()
    plt.title("Matrix Data")

    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
