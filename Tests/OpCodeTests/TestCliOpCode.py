from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestCliOpCode(OpCodeTestBase):

    def test_cli_implied_command_calls_cli_method(self):
        self.assert_opcode_execution(OpCodes.cli_implied_command, self.target.get_cli_command_executed)
