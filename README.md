# Bus Company Database Application

## Installation

Download the project, then create and activate virtual environment in the project directory.

In order to create and activate a Python virtual environment in the project directory, use your systems default Python3 environment

```shell
$ python -m venv .venv
$ source .venv/bin/activate # on Linux, or
$ ./venv/Scripts/activate # on Windows
```

After activating the virtual environment it is common for a `(.venv)` prefix to exist in the terminal line.

Next install the dependencies defined in `requirements.txt`

```shell
$ pip install -r requirements.txt
```

This installs the project libraries below

| Name  | Description                                                  | Link                                             |
| ----- | ------------------------------------------------------------ | ------------------------------------------------ |
| Typer | Library for building CLI applications                        | https://typer.tiangolo.com/                      |
| Rich  | Library for writing *rich* text (with color and style) to the terminal | https://rich.readthedocs.io/en/stable/index.html |

