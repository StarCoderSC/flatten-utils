import subprocess
import json
import sys
import os
import unittest
import tempfile

CLI_PATH = os.path.join(os.path.dirname(__file__), '..', 'flatten_utils', 'cli.py')

class TestCLI(unittest.TestCase):

    def run_cli(self, *args):
        """ Helper to run CLI command and return output """
        cmd = [sys.executable, "-m", "flatten_utils.cli"] + list(args)
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result

    def test_cli_flatten_basics(self):
        json_input = '[1, [2, [3, 4]]]'
        result = self.run_cli(json_input)
        self.assertIn('[1, 2, 3, 4]', result.stdout)

    def test_cli_with_depth(self):
        json_input = '[1, [2, [3, [4]]]]'
        result = self.run_cli(json_input, '--depth', '2')
        self.assertIn('[1, 2, [3, [4]]', result.stdout)

    def test_cli_invalid_json(self):
        result = self.run_cli('{not_json}')
        self.assertIn("Invalid JSON input!", result.stdout + result.stderr)

    def test_cli_stop_at_str(self):
        json_input = '["hello", ["world", [1, 2, 3]]]'
        result = self.run_cli(json_input, '--stop_at', 'str')
        output = json.loads(result.stdout)
        self.assertEqual(output, ["hello", "world", 1, 2, 3])

    def test_cli_file_output(self):
        test_data = '[1, [2, 3]]'
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as f:
            f.write(test_data)
            f.flush()
            result = self.run_cli('--file', f.name)
        os.remove(f.name)
        self.assertIn('[1, 2, 3]', result.stdout)


if __name__ == "__main__":
    unittest.main()



