# from clisops.core.regrid import Grid, Weights
# from clisops.core.regrid import regrid as core_regrid
from clisops.core.subset import subset_shape

from clisops.utils import get_file
from ._common import XCLIM_TESTS_DATA as TESTS_DATA

import pytest
import os
import xesmf as xe
from xesmf import SpatialAverager
import xarray as xr

nc_file_neglons = get_file("NRCANdaily/nrcan_canada_daily_tasmax_1990.nc")
southern_qc_geojson = os.path.join(TESTS_DATA, "cmip5", "southern_qc_geojson.json")


def test_regrid_import_2():
    ds = xr.open_dataset(nc_file_neglons)

    with pytest.warns(None) as record:
        sub = subset_shape(ds, southern_qc_geojson)
