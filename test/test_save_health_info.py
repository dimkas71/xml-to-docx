import pytest

from converter import save_health_info
from . import empty_content
from pytest_mock import mocker


def test_for_empty_content_save_health_info_should_produce_an_output(empty_content, tmp_path):
    test_dir = tmp_path / 'test'
    test_dir.mkdir()
    source = test_dir / 'export.xml'

    with open(source, 'w') as f:
        f.write(empty_content)

    target = test_dir / 'reestr.docx'

    save_health_info(source, target)

    assert target.exists()


def test_mocked_load_health_info_should_produce_an_output(mocker, tmp_path):
    mocker.patch('converter.load_health_info', return_value=[])
    temp_dir = tmp_path / 'test'
    temp_dir.mkdir()
    target = temp_dir / 'reestr.docs'

    save_health_info(None, target)
    assert target.exists()
