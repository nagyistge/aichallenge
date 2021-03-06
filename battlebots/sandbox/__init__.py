import os.path
import shlex

PROFILE_DIR = os.path.dirname(__file__)


def sandboxed(command, directory):
    if not command:
        return ['true']

    return ['/usr/bin/firejail',
            '--quiet',
            '--profile={}/bot.profile'.format(PROFILE_DIR),
            '--private={}'.format(directory),
            '--whitelist={}'.format(directory),
            '--'] + shlex.split(command)
