import unittest
from Chip import OpCodes

from Tests.Chip6502Spy import Chip6502Spy


class Test6502(unittest.TestCase):

    def setUp(self):
        self.__target = Chip6502Spy()

    def test_execute_brk_command_calls_brk_method(self):
        self.assert_opcode_execution(OpCodes.brk_command, self.__target.get_brk_command_executed)

    def test_execute_ora_indirect_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_indirect_x_command, self.__target.get_ora_command_executed)

    def test_execute_ora_zero_page_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_zero_page_command, self.__target.get_ora_command_executed)

    def test_execute_asl_zero_page_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_zero_page_command, self.__target.get_asl_command_executed)

    def test_execute_php_implied_command_calls_php_method(self):
        self.assert_opcode_execution(OpCodes.php_implied_command, self.__target.get_php_command_executed)

    def test_execute_ora_immediate_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_immediate_command, self.__target.get_ora_command_executed)

    def test_execute_asl_accumulator_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_accumulator_command, self.__target.get_asl_command_executed)

    def test_execute_ora_absolute_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_absolute_command, self.__target.get_ora_command_executed)

    def test_execute_asl_absolute_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_absolute_command, self.__target.get_asl_command_executed)

    def test_execute_bpl_relative_command_calls_bpl_method(self):
        self.assert_opcode_execution(OpCodes.bpl_relative_command, self.__target.get_bpl_command_executed)

    def test_execute_ora_indirect_y_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_indirect_y_command, self.__target.get_ora_command_executed)

    def test_execute_ora_zero_page_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_zero_page_x_command, self.__target.get_ora_command_executed)

    def test_execute_asl_zero_page_x_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_zero_page_x_command, self.__target.get_asl_command_executed)

    def test_execute_clc_implied_command_calls_clc_method(self):
        self.assert_opcode_execution(OpCodes.clc_implied_command, self.__target.get_clc_command_executed)

    def test_execute_ora_absolute_y_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_absolute_y_command, self.__target.get_ora_command_executed)

    def test_execute_ora_absolute_x_command_calls_ora_method(self):
        self.assert_opcode_execution(OpCodes.ora_absolute_x_command, self.__target.get_ora_command_executed)

    def test_execute_asl_absolute_x_command_calls_asl_method(self):
        self.assert_opcode_execution(OpCodes.asl_absolute_x_command, self.__target.get_asl_command_executed)

    def test_execute_jsr_absolute_command_calls_jsr_method(self):
        self.assert_opcode_execution(OpCodes.jsr_absolute_command, self.__target.get_jsr_command_executed)

    def test_execute_and_indirect_x_command_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_indirect_x_command, self.__target.get_and_command_executed)

    def test_execute_bit_zero_page_calls_bit_method(self):
        self.assert_opcode_execution(OpCodes.bit_zero_page_command, self.__target.get_bit_command_executed)

    def test_execute_and_zero_page_calls_and_method(self):
        self.assert_opcode_execution(OpCodes.and_zero_page_command, self.__target.get_and_command_executed)

    def test_execute_rol_zero_page_command_calls_rol_method(self):
        self.assert_opcode_execution(OpCodes.rol_zero_page_command, self.__target.get_rol_command_executed)

    def test_execute_plp_implied_command_calls_plp_method(self):
        self.assert_opcode_execution(OpCodes.plp_implied_command, self.__target.get_plp_command_executed)

    def test_execute_and_immediate_command_calls_and_command(self):
        self.assert_opcode_execution(OpCodes.and_immediate_command, self.__target.get_and_command_executed)

    def test_execute_rol_accumulator_command_calls_rol_command(self):
        self.assert_opcode_execution(OpCodes.rol_accumulator_command, self.__target.get_rol_command_executed)

    def assert_opcode_execution(self, op_code, status_method):
        self.__target.execute(op_code)
        self.assertTrue(status_method())