"""API Services Package

This package provides utilities and services for API interactions and management.
"""

__version__ = "0.1.0"
__author__ = "Your Name"

# Import main services/modules for easier access
from .openfda_api import query_drug_label


__all__ = [
    "query_drug_label"
]