from pathlib import Path
from dataclasses import dataclass
from typing import Optional

@dataclass
class PathsConfig:
    workdir: Path

@dataclass
class NEBConfig:
    k: float = 0.1                              # spring constant
    climb: bool = False                         # climbing image
    method: Optional[str] = None                # aseneb, improvedtangent, eb, spline
    interpolation_method: Optional[str] = None  # linear or idpp
    mic: bool = True                            # minimum image convention

@dataclass
class NEBStageConfig:
    k: float = 0.1
    climb: bool = False

@dataclass
class OptimizerConfig:
    name: str                         # e.g. FIRE, BFGS
    fmax: Optional[float] = None      # maximum force tolerance
    steps: Optional[int] = None       # maximum number of optimization steps
    a: Optional[float] = None         # parameter specific to the optimizer

@dataclass
class CalculatorConfig:
    type: str                        # mace or DFT
    model: Optional[str] = None      # path to the model file
    device: Optional[str] = None     # cpu or cuda
    head: str = "default"            # name of model head

@dataclass
class RunConfig:
    paths: PathsConfig
    neb: NEBConfig
    neb_stages: Optional[list[NEBStageConfig]] = None
    optimizer: Optional[OptimizerConfig] = None
    calculator: Optional[CalculatorConfig] = None


