import yaml
from pathlib import Path

from aseneb.config import *


def load_config(path):

    with open(path) as f:
        data = yaml.safe_load(f)

    workdir = Path(
        data.get("paths", {}).get("workdir", Path.cwd())
    )

    neb_stages = None

    if "neb_stages" in data:
        neb_stages = [
            NEBStageConfig(**stage)
            for stage in data["neb_stages"]
        ]

    return RunConfig(
        paths=PathsConfig(workdir=workdir),

        neb=NEBConfig(
            k=data["neb"].get("k", 0.1),
            climb=data["neb"].get("climb", False),
            method=data["neb"].get("method"),
            interpolation_method=data["neb"].get(
                "interpolation_method",
                "idpp",
            ),
            mic=data["neb"].get("mic", True),
        ),

        neb_stages=neb_stages,

        optimizer=OptimizerConfig(**data["optimizer"]),
        calculator=CalculatorConfig(**data["calculator"]),
    )