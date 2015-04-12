from contextlib import contextmanager
import os


@contextmanager
def shell_env(**extra_environment_variables):
    """
    Implementation of shell_env from Fabric.
    """
    original_environ = dict(os.environ)
    temporary_environ = dict(os.environ)
    temporary_environ.update(extra_environment_variables)
    yield
    os.environ.clear()
    os.environ.update(original_environ)


@contextmanager
def lcd(directory):
    """
    Implementation of lcd from Fabric.
    """
    original_directory = os.getcwd()
    os.chdir(directory)
    yield
    os.chdir(original_directory)
