from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestCliOpCode(OpCodeTestBase):

    def test_cli_implied_command_calls_cli_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.cli_implied_command, self.target.get_cli_command_executed)
