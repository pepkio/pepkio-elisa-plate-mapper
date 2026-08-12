# Pepkio ELISA Plate Mapper

Python client for Pepkio `elisa-plate-mapper` tool.

## Installation

```bash
pip install pepkio-elisa-plate-mapper
```

## Quick Start

```python
from pepkio_elisa_plate_mapper import PepkioClient

with PepkioClient() as client:
    manifest = client.get_manifest()
    example_input = client.get_example_input("example_sandwich_elisa")
    result = client.run(example_input)
    print(result.status, result.result)
```

## Command Line Interface

```bash
pepkio-elisa-plate-mapper manifest
pepkio-elisa-plate-mapper run --example example_sandwich_elisa
```
