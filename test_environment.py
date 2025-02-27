import selenium
import pytest

def test_selenium_installed():
    # Print the Selenium version to verify installation
    version = selenium.__version__
    print("Selenium version:", version)
    # Ensure that the version string exists
    assert version is not None

def test_pytest_installed():
    # Print the pytest version to verify installation
    version = pytest.__version__
    print("Pytest version:", version)
    # Ensure that the version string exists
    assert version is not None
