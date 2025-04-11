import pandas as pd

class EmployeeDataAnalysis:
    def __init__(self, file_path):
        """Load employee data into a Pandas DataFrame."""
        self.df = pd.read_csv(file_path)

    def display_head(self):
        """Return the first 5 rows of the DataFrame."""
        return self.df.head()

    def dataframe_info(self):
        """Return DataFrame column names and data types."""
        return self.df.info()

    def handle_missing_values(self):
        """Replace missing values with the column mean for numeric columns."""
        numeric_columns = self.df.select_dtypes(include=["float64", "int64"]).columns
        for column in numeric_columns:
            mean_value = self.df[column].mean()
            self.df[column].fillna(mean_value, inplace=True)

    def export_updated_csv(self, output_file="updated_employee_data.csv"):
        """Save the updated DataFrame to a new CSV file."""
        self.df.to_csv(output_file, index=False)
        return output_file

    def check_missing_values(self):
        """Check if there are any missing values in the DataFrame."""
        return self.df.isnull().sum().sum() == 0  # Returns True if no missing values
