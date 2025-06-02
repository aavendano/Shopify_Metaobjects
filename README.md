# Shopify Metaobject Loader

A Python module for loading data from CSV files into Shopify metaobjects using the Shopify Admin GraphQL API.

## Features

- Load data from CSV files into Shopify metaobjects
- Automatic upsert (update or insert) based on handle field
- Comprehensive error handling and logging
- Type hints for better code maintainability
- Environment variable support for secure credential management

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with your Shopify credentials:

```env
SHOPIFY_SHOP_DOMAIN=your-store.myshopify.com
SHOPIFY_ACCESS_TOKEN=your-admin-api-access-token
```

## Usage

### CSV File Format

Your CSV file should have a header row with column names that correspond to the fields of your Shopify metaobject. The first column must be named `handle` and will be used as the unique identifier for upsert operations.

Example CSV format:
```csv
handle,fabric_name,stretch_level,is_organic
main-cotton,Classic Cotton,2,true
stretch-denim,Stretch Denim,8,false
organic-linen,Organic Linen,1,true
```

### Basic Usage

```python
from shopify_metaobject_loader import ShopifyMetaobjectLoader

# Initialize the loader
loader = ShopifyMetaobjectLoader(
    shop_domain="your-store.myshopify.com",
    access_token="your-admin-api-access-token"
)

# Process the CSV file
stats = loader.process_csv(
    file_path="data.csv",
    metaobject_type="my_fabric_type"
)

print(f"Created: {stats['created']}")
print(f"Updated: {stats['updated']}")
print(f"Failed: {stats['failed']}")
```

### Running as a Script

You can also run the module directly as a script:

```bash
python shopify_metaobject_loader.py
```

Make sure your `.env` file is properly configured before running the script.

## Error Handling

The module includes comprehensive error handling for:
- File not found or CSV parsing errors
- Network issues or failed connections to the Shopify API
- GraphQL API errors (invalid permissions, malformed queries, validation errors)

All errors are logged with appropriate context and severity levels.

## Logging

The module uses Python's built-in logging module. Logs include:
- Successful operations (INFO level)
- Warnings and non-critical errors (WARNING level)
- Critical errors (ERROR level)

## Contributing

Feel free to submit issues and enhancement requests! 

Metaobject Type: Fabric Type (my_fabric_type)
Description: A type for describing different fabric materials

Field Summary:
Total Fields: 4
Required Fields: 2
Optional Fields: 2

Field Types:
- single_line_text_field: 2
- number_integer: 1
- boolean: 1

Required Fields:
- Fabric Name (fabric_name)
  Type: single_line_text_field
  Description: The name of the fabric material
  Validations:
    - min_length: 2
    - max_length: 100

- Stretch Level (stretch_level)
  Type: number_integer
  Description: The stretch level of the fabric (1-10)
  Validations:
    - min: 1
    - max: 10

Optional Fields:
- Is Organic (is_organic)
  Type: boolean
  Description: Whether the fabric is made from organic materials

- Handle (handle)
  Type: single_line_text_field
  Description: The unique identifier for the fabric
  Validations:
    - pattern: ^[a-z0-9-]+$ 

from shopify_metaobject_loader import ShopifyMetaobjectLoader

# Initialize the loader
loader = ShopifyMetaobjectLoader(
    shop_domain="your-store.myshopify.com",
    access_token="your-access-token"
)

# Define the fields for your metaobject type
fields = [
    {
        "key": "fabric_name",
        "name": "Fabric Name",
        "type": "single_line_text_field",
        "description": "The name of the fabric material",
        "required": True,
        "validations": [
            {"name": "min_length", "value": "2"},
            {"name": "max_length", "value": "100"}
        ]
    },
    {
        "key": "stretch_level",
        "name": "Stretch Level",
        "type": "number_integer",
        "description": "The stretch level of the fabric (1-10)",
        "required": True,
        "validations": [
            {"name": "min", "value": "1"},
            {"name": "max", "value": "10"}
        ]
    },
    {
        "key": "is_organic",
        "name": "Is Organic",
        "type": "boolean",
        "description": "Whether the fabric is made from organic materials",
        "required": False
    },
    {
        "key": "handle",
        "name": "Handle",
        "type": "single_line_text_field",
        "description": "The unique identifier for the fabric",
        "required": True,
        "validations": [
            {"name": "pattern", "value": "^[a-z0-9-]+$"}
        ]
    }
]

# Create the metaobject definition
definition = loader.create_metaobject_definition(
    type_name="my_fabric_type",
    display_name="Fabric Type",
    description="A type for describing different fabric materials",
    fields=fields
)

# Print a human-readable description
loader.print_metaobject_type_description("my_fabric_type")

# Or get the description as a dictionary
description = loader.describe_metaobject_type("my_fabric_type")

# Access specific parts of the description
print(f"Total fields: {description['field_summary']['total_fields']}")
print(f"Required fields: {description['field_summary']['required_fields']}")
print(f"Optional fields: {description['field_summary']['optional_fields']}")

# Get field types summary
for field_type, count in description['field_summary']['field_types'].items():
    print(f"- {field_type}: {count}")

# Access field details
for field in description['fields']['required']:
    print(f"\nField: {field['name']}")
    print(f"Key: {field['key']}")
    print(f"Type: {field['type']}")
    print(f"Description: {field['description']}")
    print("Validations:", field['validations']) # Shopify_Metaobjects
