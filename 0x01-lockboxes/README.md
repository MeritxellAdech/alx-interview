# Lockboxes
This directory contains the implementation of Lockboxes

## Usage
For this project, the following entry point can be used as sampling.

`main.py`
```python
    #!/usr/bin/python3

    canUnlockAll = __import__('0-lockboxes').canUnlockAll

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
```

## Run
The following script is used to run the script

```Python
    ./main
```

