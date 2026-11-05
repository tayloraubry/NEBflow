import argparse
import os
import pandas as pd
from .analysis_utils import plot_barriers

def load_processed_summary(base_path):
    """Load the processed NEB summary sheets."""
    input_file = os.path.join(base_path, "neb_summary_processed.xlsx")

    if not os.path.exists(input_file):
        raise FileNotFoundError(
            f"Processed summary not found: {input_file}\n"
            "Run aseneb-analyze, then aseneb-summarize, first to generate it."
        )

    sheets = pd.read_excel(
        input_file,
        sheet_name=["averaged_barriers", "min_barriers"],
    )

    return (
        sheets["averaged_barriers"],
        sheets["min_barriers"],
    )

def main():
    parser = argparse.ArgumentParser(
        description="Plot NEB barrier summaries from processed data"
    )

    parser.add_argument(
        "--base-path",
        default=".",
        help="Directory containing neb_summary_processed.xlsx",
    )
    parser.add_argument("--use-min", action="store_true")
    parser.add_argument("--only-singles", action="store_true")
    parser.add_argument("--model-name", default="Model", help="Model name, only affects plot title and file name")
    parser.add_argument("--full-reaction",action="store_true",help="Label the y-axis with the full reaction instead of only the reactant")

    args = parser.parse_args()

    df_avg, df_min_barrier = load_processed_summary(args.base_path)

    data = df_min_barrier if args.use_min else df_avg

    plot_barriers(
        data,
        use_min=args.use_min,
        only_singles=args.only_singles,
        model_name=args.model_name,
        reactant_only=not args.full_reaction,
    )