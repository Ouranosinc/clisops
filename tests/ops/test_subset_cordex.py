from pathlib import Path
from clisops.ops.subset import subset

from .._common import (
    _check_output_nc,
    C3S_CORDEX_PSL,
)


def test_subset_time_cordex(load_esgf_test_data, tmpdir):
    """Test subset on cordex data"""

    result = subset(
        ds=C3S_CORDEX_PSL,
        time=("2010-01-01", "2011-12-31"),
        # area=(-5.25, 42.39, 8.05, 50.86),  # France
        output_dir=tmpdir,
        output_type="netcdf",
        file_namer="standard",
    )

    _check_output_nc(
        result,
        fname="psl_EUR-11_MOHC-HadGEM2-ES_rcp85_r1i1p1_IPSL-WRF381P_v1_day_20100101-20111230.nc",
    )
