from typing import Any

import h5py as h5
import numpy as np
import pandas as pd


def read_metadata(file: str, path: str, att_key: str) -> Any:
    pass


def gen_path_in_hdf5(beta: float, n: float, var: str, setup: list[str]) -> list[str]:
    pass


def read_data(file: str, path: str) -> np.ndarray | None:
    pass


def check_signum(
    data: np.ndarray, threshold: float = 0.0, positive: bool = False
) -> None:
    pass


def check_number_of_measurements(data: np.ndarray, f: float, t: float) -> None:
    pass


def processing_data_for_speed(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    pass


def total_uncertainty(
    stat: np.ndarray | float, sys: np.ndarray | float
) -> np.ndarray | float:
    pass


def cal_density(
    phi_f: float, p: np.ndarray | float, t: np.ndarray | float
) -> np.ndarray | float:
    pass


def cal_density_uncert(
    rho: np.ndarray | float,
    p: np.ndarray | float,
    p_uncert: np.ndarray | float,
    t: np.ndarray | float,
    t_uncert: np.ndarray | float,
) -> np.ndarray | float:
    pass


def cal_expansion_number(
    gama: float, p: np.ndarray | float, p_0: np.ndarray | float
) -> np.ndarray | float:
    pass


def cal_mass_flow(
    epsilon: np.ndarray | float, area: float, delta_p: np.ndarray | float, rho: float
) -> np.ndarray | float:
    pass


def cal_mass_flow_uncert(
    mass_flow: np.ndarray | float,
    delta_p: np.ndarray | float,
    delta_p_uncert: np.ndarray | float,
) -> np.ndarray | float:
    pass


def cal_volume_flow(
    mass_flow: np.ndarray | float, density: np.ndarray | float
) -> np.ndarray | float:
    pass


def cal_volume_flow_uncert(
    volume_flow: np.ndarray | float,
    mass_flow: np.ndarray | float,
    mass_flow_uncert: np.ndarray | float,
    density: np.ndarray | float,
    density_uncert: np.ndarray | float,
) -> np.ndarray | float:
    pass


def cal_dynamic_pressure(
    mass_flow: np.ndarray | float,
    density_1: np.ndarray | float,
    density_2: np.ndarray | float,
    area_1: float,
    area_2: float,
) -> np.ndarray | float:
    pass


def archiv_plot_data(
    data: dict[str, np.ndarray], file: str, group_path: str, metadata: dict[str, Any]
) -> None:
    pass


def read_plot_data(
    file: str, group_path: str
) -> tuple[pd.DataFrame, tuple[str, str, str], list[str]]:
    pass


def main():
    # DEBUG und Test
    pass


if __name__ == "__main__":
    main()
