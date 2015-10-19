# valeera

Validator for [district42 schema](https://github.com/nikitanovosibirsk/district42).

### Usage

```python
import valeera
import district42.json_schema as schema

assert 42 == schema.integer.positive
```

### Advanced Usage

```python
import district42.json_schema as schema
from valeera import Validator, Formatter

validator = Validator(Formatter()).validate(-1, schema.integer.positive)

validator.passes() # False
validator.fails()  # True
validator.errors() # ['Number value must be greater than or equal to 1, -1 given']
```

### Installation

```sh
$ pip3 install valeera
```
