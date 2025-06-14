from collections.abc import Iterable, Mapping
from typing import Any, Generator, Union

def deep_flatten(data: Any, stop_at: Union[type, tuple] = (str, bytes)) -> Generator:
    """
    
    Recursively flattens nested iterables and mappings unless the element is of a type
    in 'stop-at'.

    Args:
        data (Any): The input data to flatten.
        stop_at (Union[type, tuple]): Types to exclude from flattening (default: (str, bytes))
    
    Yields:
        Flattened Items.

    """
    if isinstance(data, stop_at):
        yield data

    elif isinstance(data, Mapping):
        for k, v in data.items():
            yield from deep_flatten(k, stop_at)
            yield from deep_flatten(v, stop_at)
    
    elif isinstance(data, Iterable) and not isinstance(data, (str, bytes)):
        for item in data:
            yield from deep_flatten(item, stop_at)
    else:
        yield data


def flatten_limited(data: Any, depth: int = 1, stop_at: Union[type, tuple] = (str, bytes)) -> Generator:

    """
    
    Flattens nested data up to a specific depth.

    Args:
        data (Any): The input data to flttten.
        depth (int): Maximum depth to flatten (default: 1).
        stop_at (Union[type, tuple]): Types to exclude from flattening (default: (str, bytes))

        Yields: Flattened items up to the specifies depth

    """
    if depth == 0 or isinstance(data, stop_at):
        yield data
    
    elif isinstance(data, Mapping):
        for k, v in data.items():
            yield from flatten_limited(k, depth - 1, stop_at=stop_at)
            yield from flatten_limited(v, depth - 1, stop_at=stop_at)
    
    elif isinstance(data, Iterable):
        for item in data:
            yield from flatten_limited(item, depth - 1, stop_at=stop_at)
    
    else:
        yield data


def flatten_list(data: Any, stop_at: Union[type, tuple] = (str, bytes)) -> list[Any]:
    """
    
    Fully flattens nested data into a list, stopping at types in 'stop_at".

    Args:
        data (Any): The input data to flatten.
        stop_at(Union[type, tuple]): Types to exceute from flattening (default: (str, bytes))

        Returns:
            list[Any]: Fully flattened list.
    """
    return list(deep_flatten(data, stop_at=stop_at))

