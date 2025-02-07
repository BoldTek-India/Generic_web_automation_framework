import pytest
class WebApp:

    def __init__(self, name, config):
        self.name = name
        self.config = config

    def run_tests(self):
        """Run test cases."""
        test_module_path = f"tests/test_case_{self.name}.py"
        pytest.main(["-s", test_module_path])
