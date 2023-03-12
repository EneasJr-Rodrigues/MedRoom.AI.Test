import os
import papermill as pm
from pytest import mark


def main():
    pm.execute_notebook(
        'tests/rproject-nlp.ipynb',
    )


if __name__ == '__main__':
    main()
