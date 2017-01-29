import os
import glob
import configparser
import argparse
from board.core_plugins import function_register

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


parser = argparse.ArgumentParser(
    description='Board python object as web app'
)

parser.add_argument(
    '--plugin-folder',
    nargs='*',
    default=SCRIPT_DIR + '/plugins'
)

parser.add_argument(
    '--config',
    default=SCRIPT_DIR + '/config.ini'
)

args = parser.parse_args()

python_files = glob.glob(
    args.plugin_folder + '/**/*.py', recursive=True
)

for filename in python_files:
    try:
        print(filename)
        exec(
            compile(
                open(filename, "rb").read(),
                filename,
                'exec'
            ), globals(), locals()
        )
    except:
        import traceback
        traceback.print_exc()


from board.core import server
server.start_server()
