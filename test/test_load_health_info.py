from xml.etree.ElementTree import ParseError

import pytest

from converter import load_health_info

from . import content, empty_content


def test_empty_content_as_bytes_should_return_empty_health_info(empty_content):
    health_info = load_health_info(bytes(empty_content, encoding='UTF-8'))
    assert len(health_info) == 0


def test_health_info_content_as_bytes(content):
    content_as_bytes = bytes(content, encoding='UTF-8')
    health_info = load_health_info(content_as_bytes)
    assert len(health_info) == 1


def test_health_info_content_as_str_path(content, tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    p = d / 'export.xml'

    with open(p, 'w') as f:
        f.write(content)

    health_info = load_health_info(str(p))
    assert len(health_info) == 1


def test_health_info_content_as_path(content, tmp_path):
    d = tmp_path / 'tmp'
    d.mkdir()
    path = d / 'export.xml'

    with open(path, 'w') as f:
        f.write(content)

    health_info = load_health_info(path)
    assert len(health_info) == 1


def test_health_info_unsupported_content_type():
    with pytest.raises(ValueError) as exception_info:
        health_info = load_health_info(100)

    assert exception_info.type == ValueError
    assert exception_info.value.args[0] == "path can be only str or bytes or Path like object"


def test_load_health_info_unsupported_content():
    with pytest.raises(ParseError) as exception_info:
        health_info = load_health_info(bytes("blah blah", encoding='UTF-8'))

    assert exception_info.type == ParseError
    assert exception_info.value.args[0] == "syntax error: line 1, column 0"
