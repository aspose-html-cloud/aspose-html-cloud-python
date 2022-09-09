## FileVersion

### Fields
| Field             | Type     | Description                    |
|-------------------|----------|--------------------------------|
| **name**          | str      | File name                      |
| **is_folder**     | bool     | Folder or file                 |
| **modified_date** | datetime | Date of modification           |
| **size**          | int      | File size. Zero for directory  |
| **path**          | str      | Full path to the file          |
| **version_id**    | str      | Version id, if storage support |
| **is_latest**     | bool     | Last version of file           |
