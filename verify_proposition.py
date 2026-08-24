"""Numerical audit of Proposition 2.1 for one smooth concave production function."""

from math import exp, log


BETA = 10.0
KAPPA = 0.4
GAMMA = 1.0


def production(x: float) -> float:
    """p(x) = beta * (1-exp(-kappa*x)); increasing, concave, and bounded."""
    return BETA * (1.0 - exp(-KAPPA * x))


def utility(effort: float, skill: float, assistance: float) -> float:
    return production(skill + effort + assistance) - GAMMA * effort


def closed_form_effort(skill: float, assistance: float) -> float:
    x_star = log(BETA * KAPPA / GAMMA) / KAPPA
    return max(x_star - skill - assistance, 0.0)


def grid_optimum(skill: float, assistance: float) -> float:
    """Independent brute-force maximization on e in [0, 20]."""
    step = 0.0005
    candidates = (index * step for index in range(40_001))
    return max(candidates, key=lambda effort: utility(effort, skill, assistance))


def main() -> None:
    x_star = log(BETA * KAPPA / GAMMA) / KAPPA
    cases = [(0.5, 0.0), (1.0, 1.0), (2.0, 2.0), (4.0, 1.0)]

    print(f"Critical total input x* = {x_star:.6f}\n")
    for skill, assistance in cases:
        formula = closed_form_effort(skill, assistance)
        numeric = grid_optimum(skill, assistance)
        predicted_output = max(production(x_star), production(skill + assistance))
        numeric_output = production(skill + numeric + assistance)

        assert abs(formula - numeric) <= 0.001
        assert abs(predicted_output - numeric_output) <= 0.001
        print(
            f"s={skill:.1f}, a={assistance:.1f}: "
            f"formula e*={formula:.4f}, grid e*={numeric:.4f}, "
            f"p*={numeric_output:.4f} — PASS"
        )


if __name__ == "__main__":
    main()
