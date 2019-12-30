from . import autoencode, classify, train, mlflow_ui

SETUP_COMMANDS = [autoencode.setup_parser,
                  train.setup_parser,
                  classify.setup_parser,
                  mlflow_ui.setup_parser,
                 ]