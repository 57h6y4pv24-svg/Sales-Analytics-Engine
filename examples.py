"""
Example usage for the Sales Data Analysis Tool.
"""

from sellsdata import (
    load_data,
    calculate_totals,
    prepare_dates,
    generate_analysis,
    create_visualizations,
    export_to_excel,
    generate_summary,
    print_analysis,
)


def example_1_basic_analysis():
    """Example 1: Basic analysis with sample data."""
    print("📌 EXAMPLE 1: Basic analysis with sample data\n")

    df = load_data()
    df = calculate_totals(df)
    df = prepare_dates(df)
    analysis = generate_analysis(df)

    print("\n✓ Analysis completed")
    print(f"Total transactions: {len(df)}")
    print(f"Total sales: Q{df['Total Sales'].sum():,.2f}")


def example_2_custom_file():
    """Example 2: Analysis with a custom file."""
    print("\n📌 EXAMPLE 2: Analysis with a custom file\n")

    try:
        df = load_data('example_data.csv')
        df = calculate_totals(df)
        df = prepare_dates(df)
        analysis = generate_analysis(df)

        print("\n✓ File analyzed successfully")
        print("\nFirst 5 transactions:")
        print(df.head())

    except FileNotFoundError:
        print("⚠️  File not found. Make sure 'example_data.csv' exists.")


def example_3_full_report():
    """Example 3: Generate a full report."""
    print("\n📌 EXAMPLE 3: Generate a full report\n")

    df = load_data()
    df = calculate_totals(df)
    df = prepare_dates(df)
    analysis = generate_analysis(df)

    print("Generating reports...")
    create_visualizations(analysis)
    export_to_excel(df, analysis)
    generate_summary(df, analysis)

    print("\n✓ Full report generated")


def example_4_analysis_only():
    """Example 4: Analysis only, no charts."""
    print("\n📌 EXAMPLE 4: Analysis only\n")

    df = load_data()
    df = calculate_totals(df)
    df = prepare_dates(df)
    analysis = generate_analysis(df)

    print_analysis(df, analysis)


def example_5_custom_analysis():
    """Example 5: Custom analysis."""
    print("\n📌 EXAMPLE 5: Custom analysis\n")

    df = load_data()
    df = calculate_totals(df)
    df = prepare_dates(df)

    purchases_by_customer = df.groupby('Customer').size().sort_values(ascending=False)
    print("Number of purchases by customer:")
    print(purchases_by_customer)

    avg_by_category = df.groupby('Category')['Total Sales'].mean().sort_values(ascending=False)
    print("\nAverage sales by category:")
    print(avg_by_category)


if __name__ == "__main__":
    print("\n" + "="*60)
    print("USAGE EXAMPLES - Sales Data Analysis Tool")
    print("="*60 + "\n")

    print("Select an example:")
    print("1. Basic analysis with sample data")
    print("2. Analysis with a custom file")
    print("3. Generate a full report")
    print("4. Analysis only")
    print("5. Custom analysis")
    print("0. Run all\n")

    option = input("Enter your choice (0-5): ").strip()

    if option == "1":
        example_1_basic_analysis()
    elif option == "2":
        example_2_custom_file()
    elif option == "3":
        example_3_full_report()
    elif option == "4":
        example_4_analysis_only()
    elif option == "5":
        example_5_custom_analysis()
    elif option == "0":
        example_1_basic_analysis()
        example_2_custom_file()
        example_3_full_report()
        example_4_analysis_only()
        example_5_custom_analysis()
    else:
        print("Invalid option")

    print("\n" + "="*60)
    print("✅ Examples completed")
    print("="*60 + "\n")
