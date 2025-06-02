"""
Main script to verify the configuration of the 'region' metaobject in Shopify.

This script:
1. Loads environment variables
2. Initializes the ShopifyMetaobjectLoader
3. Fetches and displays the region metaobject configuration
4. Validates the configuration
5. Shows statistics about existing region metaobjects
"""

import os
import json
from dotenv import load_dotenv
from shopify_metaobject_loader import ShopifyMetaobjectLoader, Metaobject

def verify_region_configuration():
    """Verify the configuration of the 'region' metaobject."""
    # Load environment variables
    load_dotenv()
    
    # Get credentials from environment variables
    shop_domain = os.getenv("SHOPIFY_SHOP_DOMAIN")
    access_token = os.getenv("SHOPIFY_ACCESS_TOKEN")
    
    if not shop_domain or not access_token:
        print("Error: Missing required environment variables")
        print("Please ensure SHOPIFY_SHOP_DOMAIN and SHOPIFY_ACCESS_TOKEN are set in your .env file")
        return
    
    # Initialize the loader
    loader = ShopifyMetaobjectLoader(
        shop_domain=shop_domain,
        access_token=access_token,
        cache_dir=".cache"
    )
    
    try:
        print("\n=== Region Metaobject Configuration Verification ===\n")
        
        # 1. Get and display the metaobject definition
        print("1. Metaobject Definition:")
        print("-" * 50)
        loader.print_metaobject_type_description("region")
        
        # 2. Get detailed description as dictionary
        description = loader.describe_metaobject_type("region")
        
        # 3. Display field statistics
        print("\n2. Field Statistics:")
        print("-" * 50)
        print(f"Total Fields: {description['field_summary']['total_fields']}")
        print(f"Required Fields: {description['field_summary']['required_fields']}")
        print(f"Optional Fields: {description['field_summary']['optional_fields']}")
        
        # 4. Display field types distribution
        print("\n3. Field Types Distribution:")
        print("-" * 50)
        for field_type, count in description['field_summary']['field_types'].items():
            print(f"- {field_type}: {count}")
        
        # 5. Get and display existing region metaobjects statistics
        print("\n4. Existing Region Metaobjects Statistics:")
        print("-" * 50)
        stats = loader.get_metaobject_stats("region")
        print(json.dumps(stats, indent=2))
        
        # 6. Validate a sample region metaobject
        print("\n5. Sample Region Metaobject Validation:")
        print("-" * 50)
        
        # Create a sample metaobject for validation
        sample_region = Metaobject(
            type="region",
            handle="sample-region",
            fields={
                "name": "Sample Region",
                "code": "SR",
                "description": "A sample region for validation"
            }
        )
        
        # Get validation errors
        errors = loader.validate_metaobject_definition(sample_region, description)
        
        if errors:
            print("Validation Errors:")
            for error in errors:
                print(f"- {error}")
        else:
            print("Sample metaobject is valid according to the definition")
        
        # 7. Export current regions to CSV for review
        print("\n6. Exporting Current Regions to CSV:")
        print("-" * 50)
        output_file = "region_export.csv"
        loader.export_metaobjects_to_csv(
            metaobject_type="region",
            output_file=output_file,
            include_metafields=True
        )
        print(f"Regions exported to {output_file}")
        
        print("\n=== Verification Complete ===")
        
    except Exception as e:
        print(f"\nError during verification: {str(e)}")

if __name__ == "__main__":
    verify_region_configuration() 