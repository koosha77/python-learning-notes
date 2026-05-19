"""
Beam deflection helpers for common static cases (Euler-Bernoulli theory).

Units: SI (N, m, Pa). All formulas assume small deflections and constant EI.

References:
- Gross, D. et al. *Technische Mechanik 2 - Elastostatik*.
- Roark's Formulas for Stress and Strain.
"""
from __future__ import annotations
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Beam:
    """Prismatic beam cross-section / material container."""
    E: float   # Young's modulus [Pa]
    I: float   # Second moment of area [m^4]
    L: float   # Span [m]

    @property
    def EI(self) -> float:
        return self.E * self.I


def max_deflection_udl(beam: Beam, q: float) -> float:
    """Max deflection of a simply-supported beam with uniformly distributed load.

    δ_max = 5 q L^4 / (384 EI), at mid-span.

    Args:
        beam: Beam properties.
        q: line load [N/m].
    Returns:
        Maximum deflection [m].
    """
    return 5.0 * q * beam.L ** 4 / (384.0 * beam.EI)


def max_deflection_point_load(beam: Beam, P: float, a: float | None = None) -> float:
    """Simply-supported beam with a single point load P at distance `a` from left support.

    Mid-span loading (a = L/2): δ_max = P L^3 / (48 EI).
    General case uses the exact expression.
    """
    if a is None or math.isclose(a, beam.L / 2):
        return P * beam.L ** 3 / (48.0 * beam.EI)
    b = beam.L - a
    # exact expression for max deflection (Roark, Table 8.1)
    x = math.sqrt((beam.L ** 2 - b ** 2) / 3.0)
    return P * b * x * (beam.L ** 2 - b ** 2 - x ** 2) / (9.0 * math.sqrt(3) * beam.EI * beam.L)


def cantilever_tip_deflection_udl(beam: Beam, q: float) -> float:
    """Cantilever beam with UDL over full length: δ_tip = q L^4 / (8 EI)."""
    return q * beam.L ** 4 / (8.0 * beam.EI)


if __name__ == "__main__":
    # Example: IPE 200 steel beam, 6 m span, q = 5 kN/m
    steel = Beam(E=210e9, I=1943e-8, L=6.0)
    q = 5_000.0  # N/m
    delta = max_deflection_udl(steel, q) * 1000  # in mm
    print(f"Mid-span deflection: {delta:.2f} mm")
    print(f"Limit L/300 = {steel.L / 300 * 1000:.2f} mm")

