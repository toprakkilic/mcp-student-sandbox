# Clean Code Refactored Version
# Constants
TAX_RATE = 1.15
LOG_FILE_PATH = "log.txt"

class DataProcessor:
    def __init__(self, log_file_path=LOG_FILE_PATH):
        self.log_file_path = log_file_path

    def calculate_values(self, data):
        """Calculate adjusted values with tax rate."""
        return [d * TAX_RATE for d in data]

    def print_results(self, values):
        """Print formatted results to console."""
        for val in values:
            print(f"Total: {val:.2f}")

    def log_results(self, results):
        """Log results to file."""
        with open(self.log_file_path, "a") as f:
            f.write(str(results) + "\n")

    def process_data(self, data):
        """Main processing method: calculate, print, and log."""
        values = self.calculate_values(data)
        self.print_results(values)
        self.log_results(values)
        return values

# Usage example
if __name__ == "__main__":
    processor = DataProcessor()
    data = [100, 200, 300]
    result = processor.process_data(data)
