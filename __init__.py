"""
Sales Data Analysis Tool
Professional sales data analysis tool for sales reporting and visualization.

Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Data Analyst"
__email__ = "contact@example.com"

from sellsdata import (
    load_data,
    calculate_totals,
    prepare_dates,
    generate_analysis,
    print_analysis,
    create_visualizations,
    export_to_excel,
    generate_summary,
    main,
)

__all__ = [
    "load_data",
    "calculate_totals",
    "prepare_dates",
    "generate_analysis",
    "print_analysis",
    "create_visualizations",
    "export_to_excel",
    "generate_summary",
    "main",
]
