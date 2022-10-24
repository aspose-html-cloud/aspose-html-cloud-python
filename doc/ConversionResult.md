## ConversionResult


### Fields
| Field            | Type        | Description                                                                  |
|------------------|-------------|------------------------------------------------------------------------------|
| **code**         | int         | Http return code                                                             |
| **id**           | str         | Conversion Id                                                                |
| **status**       | str         | Conversion status ("pending", "running", "completed", "faulted", "canceled") |
| **description**  | str         | Description of error                                                         |
| **links**        | list\[str\] | Reserved                                                                     |
| **file**         | str         | Result file. Zip if multi-file result                                        |

