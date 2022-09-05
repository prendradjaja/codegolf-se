import subprocess
import sys

expected = open('expected-output').read().rstrip('\n')

_ = subprocess.check_output(['python3', 'active.py']).decode('utf-8').rstrip('\n')
_ = _.splitlines()
_ = [line.rstrip() for line in _]
_ = '\n'.join(_)
actual = _

print(expected == actual)
