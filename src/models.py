from dataclasses import dataclass
from typing import Tuple

@dataclass
class StyleParameters:
    temperature: float
    tint: float
    contrast: float
    saturation: float
    vibrance: float 

    shadows_rgb: Tuple[float, float, float]
    midtones_rgb: Tuple[float, float, float]
    highlights_rgb: Tuple[float, float, float]

    grain_amount: float

    @staticmethod
    def neutral():
        return StyleParameters(
            temperature=0.0,
            tint=0.0,
            contrast=1.0,
            saturation=1.0,
            vibrance=1.0,
            shadows_rgb=(0.0,0.0,0.0),
            midtones_rgb=(0.0,0.0,0.0),
            highlights_rgb=(0.0,0.0,0.0),
            grain_amount=0.0
        )