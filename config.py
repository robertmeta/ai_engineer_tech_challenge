import os
from functools import cache

from dotenv import dotenv_values


@cache
def get_config():
    config_dir = os.path.realpath(os.path.dirname(__file__))

    config = {
        "CONFIG_DIR": config_dir,
        **dotenv_values(os.path.join(config_dir, ".env")),
        # load shared development variables
        # **dotenv_values(
        #     os.path.join(src_dir, "..", ".env.secret")
        # ),  # load sensitive variables
        **os.environ,  # override loaded values with environment variables
    }

    if config["DEBUG"].lower() == "true":
        config["DEBUG"] = True
    else:
        config["DEBUG"] = False

    return config
