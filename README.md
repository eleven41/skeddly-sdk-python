# Skeddly SDK for Python

The official Skeddly SDK for Python.

[![Build status](https://ci.appveyor.com/api/projects/status/d7a4cmmx415u932o?svg=true)](https://ci.appveyor.com/project/eleven41/skeddly-sdk-python)

## Requirements

* Python 3.6 or later

## Installation

Install the SDK using `pip`.

```
pip install skeddly-sdk
```

## Usage

Step 1: In your `.py` file, `import` the Skeddly namespace:

```python
import skeddly
```

Step 2: Create a configuration file in `~/.skeddlyrc`:

```
[default]
accessKey=sk_12345678901234567890123456789012
```

The `default` section header is required.

Step 3: Create your client object:

```python
client = skeddly.Client()
```

Step 4: Call the Skeddly API:

```python
actions = client.list_actions(
    filter={
        "actionTypes": "amazon-start-ec2-instances"
    })
```

### Per-Client Configuration

If you want to set the Skeddly access key via code rather than in the `~/skeddlyrc` file, you can do so by passing the access key into the client constructor:

```python
client = skeddly.Client(accessKey="sk_12345678901234567890123456789012")
```

### Data Formats

#### Responses

Unless otherwise mentioned, responses are `dict`.

```python
actions = client.list_actions()
for action in actions:
    print("Action ID: " + action["actionId"])
    print("Action Name: " + action["name"])
```

## Additional Resources

* [Skeddly API Documentation](https://docs.skeddly.com/)
* [Skeddly Help Centre](http://help.skeddly.com/)

## Getting Help

### SDK Bugs

If you think you found a bug in the code of this SDK, feel free to [create an issue](https://github.com/eleven41/skeddly-sdk-python/issues/new).

### Missing Functionality

If a method if missing from this library that is in the Skeddly API Documentation, feel free to [create an issue](https://github.com/eleven41/skeddly-sdk-python/issues/new).

### Pull Requests

We can accept pull requests. Our review requirements are strict though :)

### All Other Help

Please [contact us](https://www.skeddly.com/contact-us/).