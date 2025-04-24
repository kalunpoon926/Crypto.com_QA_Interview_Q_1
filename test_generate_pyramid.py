from generate_pyramid import generate_pyramid
import pytest
import re
from logger_config import setup_logger


logger = setup_logger(__name__)


def test_generate_pyramid_default_char():
    logger.info("Testing default '*' character with n=5")
    expected = (
        '    *    \n'
        '   ***   \n'
        '  *****  \n'
        ' ******* \n'
        '*********'
    )
    result = generate_pyramid(5)
    logger.info("\n" + result)
    assert result == expected


def test_generate_pyramid_default_char_n20():
    logger.info("Testing default '*' character with n=20")
    result = generate_pyramid(20)
    logger.info("Generated Pyramid:\n" + result)
    lines = result.split('\n')
    # Check number of levels
    assert len(lines) == 20

    # Check first line (should contain 1 '*')
    assert lines[0].strip() == '*'

    # Check last line (should contain 39 '*')
    assert lines[-1].strip() == '*' * 39

    # Check centering of a few lines
    assert lines[0] == '*'.center(39)

    assert lines[9] == ('*' * 19).center(39)
    assert lines[-1] == ('*' * 39).center(39)

def test_generate_pyramid_custom_char():
    logger.info("Testing custom '#' character with n=3")
    expected = (
        '  #  \n'
        ' ### \n'
        '#####'
    )
    result = generate_pyramid(3, '#')
    logger.info("\n" + result)
    assert result == expected

def test_generate_pyramid_invalid_char():
    logger.info("Testing invalid character '@'")
    with pytest.raises(ValueError):
        generate_pyramid(5, '@')

def test_generate_pyramid_n20_default_char():
    logger.info("Testing n=20 with default '*' character")
    result = generate_pyramid(20)
    logger.info("\n" + result)
    lines = result.split('\n')
    assert len(lines) == 20  # 20 levels + final empty line
    assert lines[0].strip().startswith('*')  # Top level: 1 *
    assert lines[19].strip().startswith('*' * 39)  # Bottom level: 39 *
    assert lines[0].endswith(' ')  # Trailing space in first line
    assert lines[18].endswith(' ')  # Trailing space in last non-empty line

def test_generate_pyramid_invalid_n_too_large():
    logger.info("Testing invalid n=21")
    with pytest.raises(ValueError, match="n must be an integer between 1 and 20"):
        generate_pyramid(21)

def test_generate_pyramid_invalid_n_non_integer():
    logger.info("Testing invalid n=3.5")
    with pytest.raises(ValueError, match="n must be an integer between 1 and 20"):
        generate_pyramid(3.5)

def test_generate_pyramid_invalid_char_empty():
    logger.info("Testing invalid empty char")
    with pytest.raises(ValueError, match=re.escape("char must be either '*' or '#'.")):
        generate_pyramid(3, '')

def test_generate_pyramid_invalid_char_multi():
    logger.info("Testing invalid multi-character char '**'")
    with pytest.raises(ValueError, match=re.escape("char must be either '*' or '#'.")):
        generate_pyramid(3, '**')

def test_generate_pyramid_invalid_char_non_string():
    logger.info("Testing invalid non-string char None")
    with pytest.raises(ValueError, match=re.escape("char must be either '*' or '#'.")):
        generate_pyramid(3, None)
