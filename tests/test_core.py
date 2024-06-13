from pytest import fixture
from markdown import Markdown
import importlib
import importlib.metadata


@fixture
def md():
    md = Markdown(extensions=['classes'])
    return md


def test_metadata():
    meta = importlib.metadata.entry_points(group='markdown.extensions')
    for m in meta:
        if m.name == 'classes':
            break
    else:
        raise ValueError("Entry point not registered correctly")


def test_extension_can_register():
    md = Markdown()
    md.registerExtension('classes')
    for e in md.registeredExtensions:
        if e == 'classes':
            break
    else:
        raise ValueError("Extension not registered correctly")


def test_extension_gets_ran(md: Markdown):
    text = "# hello world!"
    parsed = md.convert(text)
    assert 'h1' in parsed