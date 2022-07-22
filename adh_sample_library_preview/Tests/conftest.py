def pytest_addoption(parser):
    parser.addoption("--e2e", action="store", default=False)