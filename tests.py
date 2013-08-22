import os
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = 'suggestionbox.testsettings'
from suggestionbox import testsettings as settings


def run_tests(settings):
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner(interactive=False)
    failures = test_runner.run_tests(['suggestionbox'])
    return failures


def main():
    failures = run_tests(settings)
    sys.exit(failures)

if __name__ == '__main__':
    main()
