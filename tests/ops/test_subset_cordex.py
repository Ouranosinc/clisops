from roocs_utils.parameter.param_utils import time_interval

from clisops.ops.subset import subset

from .._common import (
    C3S_CORDEX_AFR_TAS,
    C3S_CORDEX_ANT_SFC_WIND,
    C3S_CORDEX_EUR_ZG500,
    C3S_CORDEX_NAM_PR,
    _check_output_nc,
)


def test_subset_cordex_afr(load_esgf_test_data, tmpdir):
    """Test subset on cordex data AFR domain"""

    result = subset(
        ds=C3S_CORDEX_AFR_TAS,
        time=time_interval("2000-01-01", "2001-12-31"),
        output_dir=tmpdir,
        output_type="netcdf",
        file_namer="standard",
    )

    _check_output_nc(
        result,
        fname="tas_AFR-22_MPI-M-MPI-ESM-LR_historical_r1i1p1_GERICS-REMO2015_v1_day_20000101-20011231.nc",
    )


def test_subset_cordex_nam(load_esgf_test_data, tmpdir):
    """Test subset on cordex data NAM domain"""

    result = subset(
        ds=C3S_CORDEX_NAM_PR,
        time=time_interval("2051-01-01", "2052-12-31"),
        output_dir=tmpdir,
        output_type="netcdf",
        file_namer="standard",
    )

    _check_output_nc(
        result,
        fname="pr_NAM-22_NOAA-GFDL-GFDL-ESM2M_rcp45_r1i1p1_OURANOS-CRCM5_v1_day_20510101-20521231.nc",
    )


def test_subset_cordex_eur(load_esgf_test_data, tmpdir):
    """Test subset on cordex data EUR domain"""

    result = subset(
        ds=C3S_CORDEX_EUR_ZG500,
        time=time_interval("2075-01-01", "2076-12-31"),
        output_dir=tmpdir,
        output_type="netcdf",
        file_namer="standard",
    )

    _check_output_nc(
        result,
        fname="zg500_EUR-11_IPSL-IPSL-CM5A-MR_rcp85_r1i1p1_IPSL-WRF381P_v1_day_20750101-20761231.nc",
    )


def test_subset_cordex_ant(load_esgf_test_data, tmpdir):
    """Test subset on cordex data ANT domain"""

    result = subset(
        ds=C3S_CORDEX_ANT_SFC_WIND,
        time=time_interval("1985-01-01", "1986-12-31"),
        output_dir=tmpdir,
        output_type="netcdf",
        file_namer="standard",
    )

    _check_output_nc(
        result,
        fname="sfcWind_ANT-44_ECMWF-ERAINT_evaluation_r1i1p1_KNMI-RACMO21P_v1_day_19850101-19861231.nc",
    )
