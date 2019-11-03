import pytest

from plenum.test.view_change_service.helper import check_view_change_adding_new_node


@pytest.fixture(scope="module", params=['twice', 'once'])
def vc_counts(request):
    return request.param


@pytest.fixture(scope="module", params=[True, False])
def slow_node_is_next_primary(request):
    return request.param


@pytest.mark.skip('INDY-2262')
def test_view_change_while_adding_new_node_2_slow_commit(looper, tdir, tconf, allPluginsPath,
                                                         txnPoolNodeSet,
                                                         sdk_pool_handle,
                                                         sdk_wallet_client,
                                                         sdk_wallet_steward):
    check_view_change_adding_new_node(looper, tdir, tconf, allPluginsPath,
                                      txnPoolNodeSet,
                                      sdk_pool_handle,
                                      sdk_wallet_client,
                                      sdk_wallet_steward,
                                      slow_nodes=[txnPoolNodeSet[1], txnPoolNodeSet[2]],
                                      delay_pre_prepare=False,
                                      delay_commit=True,
                                      expected_viewno=5)
