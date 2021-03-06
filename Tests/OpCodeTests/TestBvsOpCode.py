from Chip import OpCodeDefinitions
from Tests.OpCodeTests.OpCodeTestBase import OpCodeTestBase


class TestBvsOpCode(OpCodeTestBase):
    def test_bvs_relative_command_calls_bvs_method(self):
        self.assert_opcode_execution(OpCodeDefinitions.bvs_relative_command, self.target.get_bvs_command_executed)
