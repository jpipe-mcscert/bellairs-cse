######
## Justification performant
######

from typing import Any, Callable

from jpipe_runner.framework.decorators.jpipe_decorator import jpipe

mock = {
    'accuracy':     0.92,
    'model_file':   'https://huggingface.co/boltuix/bert-emotion',
    'test_dataset': ''
}

## Conclusion c
@jpipe(consume=["a"])
def my_model_is_performant(produce: Callable[[str, Any], None]) -> bool:
    # nothing more to do than reaching this stage
    return True

## Strategy s
@jpipe(consume=["m", "d"], produce=["a"])
def accuracy_is_greater_than_85(m: bool, d: bool,
                                produce: Callable[[str, Any], None]) -> bool:
    # load the model; load the tests; measure accuracy
    print('\n XXXXX \n' + m)
    produce("a", True)
    return True
    #return bool(m) and bool(d) and mock['accuracy'] > 0.85

## Evidence e1
@jpipe(produce=["m"])
def model_is_available(produce: Callable[[str, Any], None]) -> bool:
    print('\n yyyyyyy ')
    # Check that the model file exists and can be loaded
    if 'model_file' in mock:
        produce('m', True)
        return True
    return False

@jpipe(produce=["d"])
def test_dataset_is_available(produce: Callable[[str, Any], None]) -> bool:
    # Check that the dataset exists on the disk
    if 'test_dataset' in mock:
        produce('d', True)
        return True
    return False

