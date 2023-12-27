import os
from pathlib import Path


files_list_for_structure = [

    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/component/__init__.py",
    "src/component/data_ingestion.py",
    "src/component/data_transformation.py",
    "src/component/model_trainer.py",
    "src/component/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"


]

for file in files_list_for_structure:
    filepath = Path(file)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , "w") as f:
            pass

        