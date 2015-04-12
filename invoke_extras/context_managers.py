from contextlib import contextmanager
import os


@contextmanager
def shell_env(**extra_environment_variables):
    """
    Context manager for setting shell environment variables for wrapped commands.

    Examples:

        Set the TMPDIR environment variable to configure a gcc execution::

            with shell_env(TMPDIR="info"):
                run("gcc helloworld.c")
    """
    original_environ = dict(os.environ)
    os.environ.update(extra_environment_variables)
    yield
    os.environ.clear()
    os.environ.update(original_environ)


@contextmanager
def cd(path):
    """
    Context manager for running for wrapped commands with a different working
    directory.

    Examples:

        Run ``find`` in the HOME directory::

            with cd(os.path.expanduser('~'):
                run('find . -name "*.py"')

    """
    original_path = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(original_path)
