######
## Justification performant
######

from typing import Any, Callable

from jpipe_runner.framework.decorators.jpipe_decorator import jpipe

# jpipe-runner --library steps/performant.py --diagram performant --format svg performant.json

mock = {
    'accuracy':     0.92,
    'model_file':   'https://huggingface.co/boltuix/bert-emotion',
    'test_dataset': 'tests.csv'
}

@jpipe(consume=["accuracy"])
def my_model_is_performant(produce: Callable[[str, Any], None]) -> bool:
    return True

@jpipe(consume=["model", "tests"], produce=["accuracy"])
def accuracy_is_greater_than_85(model: bool, tests: bool,
                                produce: Callable[[str, Any], None]) -> bool:
    #if (ok := model and mock['accuracy'] > 0.85):
    if (ok := model and tests and mock['accuracy'] > 0.85):
        produce("accuracy", mock['accuracy'])
    return ok

@jpipe(produce=["model"])
def model_is_available(produce: Callable[[str, Any], None]) -> bool:
    if (found := 'model_file' in mock):
        produce('model', True)
    return found  

@jpipe(produce=["tests"])
def test_dataset_is_available(produce: Callable[[str, Any], None]) -> bool:
    if (found := 'test_dataset' in mock):
        produce('tests', True)
    return found  
