# rdbl

This is a small package made for convenience in handling currencies and other figures. It's installable via:

```console
pip install git://github.com/nikhilwoodruff/rdbl
```

## Usage

Usage is simple enough, just import a specific number function in a Python file and pass to the function:

```
from rdbl import gbp

gbp(22231155.22)

# out: '£22.2m'

gbp(0.229)

# out: '23p'

gbp(-22333933932)

# out: '-£22.3bn'
