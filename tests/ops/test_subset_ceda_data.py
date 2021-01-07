import os
import pytest

import xarray as xr

from clisops.ops.subset import subset
from clisops.utils.output_utils import _format_time


CRU_TS_TMPL = '../mini-ceda-archive/archive/badc/cru/data/cru_ts/cru_ts_4.04/data/{var_id}/*.{var_id}*.nc'
CRU_TS_WET_FILE = CRU_TS_TMPL.format(var_id='wet')


# Decide whether to skip all tests
CHECK_CEDA_DATASETS = os.environ.get('CHECK_CEDA_DATASETS', False)
pytestmark = pytest.mark.skipif(not CHECK_CEDA_DATASETS, reason='Not using CEDA datasets')


def _check_output_nc(result, fname="output_001.nc"):
    assert fname in [os.path.basename(_) for _ in result]


def _load_ds(fpath):
    return xr.open_mfdataset(fpath)


def test_subset_cru_ts_wet(tmpdir):
    """Tests clisops subset function with CRU TS dataset."""
    area = (-30.0, -20.0, 60.0, 50.0)
    tm = ("2005-01-01T00:00:00", "2009-12-30T00:00:00")

    kwargs = dict(
        ds=CRU_TS_WET_FILE,
        time=tm,
        area=area,
        output_dir=tmpdir,
        file_namer="simple",
    )

    res1 = subset(output_type='nc', **kwargs)
    _check_output_nc(res1)

    res2 = subset(output_type='xarray', **kwargs)
    ds = res2[0]

    # Check area subset is in range
    assert area[0] <= ds.lon.data[0] <= area[2]
    assert area[1] <= ds.lat.data[0]<= area[3]

    # Check in time range
    assert tm[0] <= _format_time(ds.time.values[0])
    assert tm[1] >= _format_time(ds.time.values[-1])
    assert len(ds.time) == 60

    # Check variable
    assert 'wet' in ds


def test_subset_cru_ts_all(tmpdir):
    """Tests clisops subset function with CRU TS dataset."""
    area = (-90.0, -90.0, 90.0, 90.0)
    tm = ("2009-07-01T00:00:00", "2009-12-30T00:00:00")

    var_ids = 'cld  dtr  frs  pet  pre  tmn  tmp  tmx  vap  wet'.split()

    kwargs = dict(
        time=tm,
        area=area,
        output_type='xarray'
    )

    # Extract results based on assumption that each variable id exists in the correct input file
    results = [subset(ds=CRU_TS_TMPL.format(var_id=var_id), **kwargs)[0][var_id] for var_id in var_ids]

    # Assert outputs are uniform
    assert len(set([res.shape for res in results])) == 1
    assert len(set([res.size for res in results])) == 1 
    assert set([len(res.time) for res in results]) == {6}
    
