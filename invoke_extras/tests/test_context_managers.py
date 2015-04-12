import os
from os.path import expanduser, abspath
import subprocess
from unittest import TestCase
from invoke_extras.context_managers import shell_env, lcd


class TestShellEnv(TestCase):
    def test_shell_env(self):
        self.assertEqual(os.environ.get('INVOKE_EXTRAS_TESTSTUFF', None), None)
        with shell_env(INVOKE_EXTRAS_TESTSTUFF='test'):
            self.assertEqual(os.environ.get('INVOKE_EXTRAS_TESTSTUFF', None), 'test')
        self.assertEqual(os.environ.get('INVOKE_EXTRAS_TESTSTUFF', None), None)

    def test_shell_env_works_with_child_process(self):
        # This test requires a posix environment to work
        with shell_env(INVOKE_EXTRAS_TESTSTUFF='test'):
            output = subprocess.check_output('echo $INVOKE_EXTRAS_TESTSTUFF', shell=True).strip()
            self.assertEqual(output, b'test')


class TestLcd(TestCase):
    def test_lcd(self):
        homedirectory = abspath(expanduser("~"))
        self.assertNotEqual(os.getcwd(), homedirectory)
        with lcd(homedirectory):
            self.assertEqual(os.getcwd(), homedirectory)
        self.assertNotEqual(os.getcwd(), homedirectory)

    def test_lcd_works_with_child_process(self):
        # This test requires a posix environment to work
        homedirectory = abspath(expanduser("~"))
        with lcd(homedirectory):
            output = subprocess.check_output('pwd', shell=True).strip()
            self.assertEqual(output, homedirectory.encode('utf-8'))
