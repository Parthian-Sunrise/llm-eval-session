import os
import pandas as pd
from local_variables import ROOT_DIR


def get_root_dir():
    return ROOT_DIR


def test_root_dir(rel_root):
    cwd = os.getcwd()
    if cwd.replace(str(ROOT_DIR), "").count("/") == rel_root.count("/"):
        print("Root directory set up correctly!")
    else:
        print("Root directory may be incorrect, check local variables")


def preprocess_hallucination(df, volume, seed=42):
    """
    Function to prepare hallucination random sample.

    Args:
        df: original hallucination data
        volume: df size
        seed: seed used for random state

    Returns:
        randomly sampled correct answer df and hallucinated answer df

    """

    df_right_answer = pd.DataFrame(
        {
            "Context": df["knowledge"] + " " + df["question"],
            "Response": df["right_answer"],
            "Ground_truth": 1,
        }
    )

    df_hallucinate_answer = pd.DataFrame(
        {
            "Context": df["knowledge"] + " " + df["question"],
            "Response": df["hallucinated_answer"],
            "Ground_truth": 0,
        }
    )

    return df_right_answer.sample(
        n=volume, random_state=seed
    ), df_hallucinate_answer.sample(n=volume, random_state=seed)
