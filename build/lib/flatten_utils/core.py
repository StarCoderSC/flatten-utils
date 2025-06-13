from collections.abc import Iterable, Mapping
from typing import Any, Generator, Union

def deep_flatten(data: Any, stop_at: Union[type, tuple] = (str, bytes)) -> Generator:
    if isinstance(data, Mapping):
        for k, v in data.items():
            yield from deep_flatten(k, stop_at)
            yield from deep_flatten(v, stop_at)
    
    elif isinstance(data, Iterable) and not isinstance(data, (str, bytes)):
        for item in data:
            yield from deep_flatten(item)
    else:
        yield data


def flatten_limited(data: Any, depth: int = 1, stop_at: Union[type, tuple] = (str, bytes)) -> Generator:
    if depth == 0 or isinstance(data, stop_at):
        yield data
    
    elif isinstance(data, Mapping):
        for k, v in data.items():
            yield from flatten_limited(k, depth - 1)
            yield from flatten_limited(v, depth - 1)
    
    elif isinstance(data, Iterable):
        for item in data:
            yield from flatten_limited(item, depth - 1)
    
    else:
        yield data

def flatten_list(data: Any) -> list[Any]:
    return list(deep_flatten(data))