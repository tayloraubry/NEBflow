"""
CLI entry point for downselecting and averaging the tagged NEB summary.

Usage:
    aseneb-summarize --base-path folder/
    aseneb-summarize --max-path-length 20 --max-delta-e 0.1 --include-unconverged
    aseneb-summarize --group-by rxn halide_order
"""

import argparse
from .analysis_utils import process_tagged_summary


def main():
    parser = argparse.ArgumentParser(
        description="Filter, average and take minimums over neb_summary_tagged.xlsx -> neb_summary_processed.xlsx"
    )

    parser.add_argument("--base-path", default=".", help="Directory containing neb_summary_tagged.xlsx")

    parser.add_argument("--max-path-length", type=float, default=25.0, help="Maximum allowed path length for NEB paths, default: 25.0")

    parser.add_argument("--include-unconverged", action="store_true", help="Keep unconverged NEB runs (default: removed)")

    parser.add_argument("--max-delta-e", type=float, default=0.0, help="Maximum allowed deltaE (eV); removes more endothermic paths, default: 0.0")

    parser.add_argument("--group-by", nargs="+", default=["rxn"], help="Tagged-summary column(s) to average/minimize over, default: rxn (e.g. 'rxn halide_order' keeps orderings separate)")

    args = parser.parse_args()

    process_tagged_summary(
        base_path=args.base_path,
        max_path_length=args.max_path_length,
        include_unconverged=args.include_unconverged,
        max_delta_e=args.max_delta_e,
        group_by=args.group_by,
    )


if __name__ == "__main__":
    main()
