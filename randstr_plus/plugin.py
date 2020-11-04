import pytest

from . import stringer as _stringer


@pytest.fixture
def server_thread(server_thread_factory):
    yield _stringer
