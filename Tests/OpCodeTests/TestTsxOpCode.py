from Chip import OpCodes
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestTsxOpCode(OpCodeTestBase
):

    def test_tsx_implied_command_calls_tsx_method(self):
        self.assert_opcode_execution(OpCodes.tsx_implied_command, self.target.get_tsx_command_executed)
