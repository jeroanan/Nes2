from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestPhpOpcode(OpCodeTestBase):
    def test_execute_php_implied_command_calls_php_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.php_implied_command, self.target.get_php_command_executed)
