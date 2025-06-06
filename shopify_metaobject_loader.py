"""
Shopify Metaobject Loader Module

This module provides functionality to load data from CSV files into Shopify metaobjects
using the Shopify Admin GraphQL API. It handles both creation and updates of metaobjects
based on a unique handle field.

Dependencies:
    - pandas: For CSV parsing
    - requests: For HTTP requests to Shopify API
    - python-dotenv: For environment variable management
    - typing: For type hints
    - logging: For logging functionality
    - tenacity: For retry logic
"""

import os
import logging
from typing import Dict, List, Optional, Any, TypedDict, Union, Iterator
import pandas as pd
import requests
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from datetime import datetime
import json
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ShopifyAPIError(Exception):
    """Base exception for Shopify API errors."""
    pass

class ShopifyRateLimitError(ShopifyAPIError):
    """Exception raised when Shopify API rate limit is exceeded."""
    pass

class ShopifyUserError(ShopifyAPIError):
    """Exception raised when Shopify API returns user errors."""
    pass

class MetaobjectFieldDefinition(TypedDict):
    """Type definition for metaobject field definitions."""
    key: str
    name: str
    type: str
    description: Optional[str]
    required: bool
    validations: List[Dict[str, Any]]

class MetaobjectDefinition(TypedDict):
    """Type definition for metaobject definitions."""
    type: str
    name: str
    description: Optional[str]
    fields: List[MetaobjectFieldDefinition]

# Remove the Metaobject and ShopifyMetaobjectLoader class definitions from this file after migration to the package.
# Keep only legacy CLI or script logic if needed, or deprecate this file.

def main():
    """Example usage of the ShopifyMetaobjectLoader class."""
    # Load environment variables
    load_dotenv()
    
    # Get credentials from environment variables
    shop_domain = os.getenv("SHOPIFY_SHOP_DOMAIN")
    access_token = os.getenv("SHOPIFY_ACCESS_TOKEN")
    
    if not shop_domain or not access_token:
        logger.error("Missing required environment variables")
        return
        
    # Initialize the loader with caching
    loader = ShopifyMetaobjectLoader(
        shop_domain=shop_domain,
        access_token=access_token,
        cache_dir=".cache"
    )
    
    try:
        # Example: Create and upsert multiple metaobjects
        metaobjects = [
            Metaobject(
                type="product_spec",
                handle=f"example-spec-{i}",
                fields={
                    "spec_name": f"Spec {i}",
                    "spec_value": str(i * 100),
                    "unit": "g"
                }
            )
            for i in range(3)
        ]
        
        # Batch upsert
        stats = loader.batch_upsert_metaobjects(metaobjects, batch_size=2)
        print(f"Batch upsert stats: {stats}")
        
        # Export to CSV
        loader.export_metaobjects_to_csv(
            metaobject_type="product_spec",
            output_file="exported_specs.csv",
            include_metafields=True
        )
        
        # Get statistics
        stats = loader.get_metaobject_stats("product_spec")
        print(f"Metaobject stats: {json.dumps(stats, indent=2)}")
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()