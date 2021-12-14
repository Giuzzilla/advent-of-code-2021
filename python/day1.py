import pandas as pd

def star1(df: pd.DataFrame) -> int:
    mask = df.diff() > 0
    return df[mask].count()

def star2(df: pd.DataFrame) -> int:
    mask = df.rolling(3).sum().diff() > 0
    return df[mask].count()

if __name__ == "__main__":
    file_df = pd.read_csv("input.txt", header=None).iloc[:, 0]
    print(f"Star #1: {star1(file_df)}")
    print(f"Star #2: {star2(file_df)}")
