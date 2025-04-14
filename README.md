# Naver Real Estate Analyzer

A Flask-based application for analyzing Naver real estate data with price trend visualization and export functionality. This tool helps users make data-driven property investment decisions through easy API integration with Naver's real estate platform.

## Features

- **Data Retrieval**: Fetches property data from Naver Real Estate API using apartment complex IDs
- **Data Analysis**: Calculates statistics like average prices, min/max values, and price trends
- **Data Visualization**: Displays data in sortable, searchable tables
- **Data Export**: Downloads data in CSV or Excel formats for further analysis
- **Standalone Executable**: Packaged as a standalone application that can run without Python installation

## Getting Started

### Prerequisites

- Python 3.6+ (for development only, not needed for running the executable)
- Required Python packages (for development):
  - Flask
  - requests
  - pandas
  - openpyxl

### Installation

#### Running the Executable (End Users)

1. Download the latest release from the releases page
2. Double-click the executable file
3. The application will open in your default web browser

#### Development Setup

1. Clone this repository
   ```
   git clone https://github.com/henrynkoh/house-sale.git
   cd house-sale
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Run the development server
   ```
   python naver_real_estate_app_exe.py
   ```

## Usage

1. Find the Complex ID of an apartment on Naver Real Estate (https://new.land.naver.com)
   - The Complex ID appears in the URL as `complexes/[ID]`
   
2. Enter the Complex ID and other parameters in the application
   - Trade Type (A1: Purchase, B1: Jeonse, B2: Monthly Rent)
   - Year range (1-20 years)
   - Area number within the complex
   
3. View the retrieved data in table format

4. Analyze price trends and statistics in the Analytics tab

5. Export data to CSV or Excel for further analysis

## Building the Executable

To build a standalone executable:

```
./build_executable.sh
```

The executable will be created in the `dist` folder.

## Project Structure

- `naver_real_estate_app_exe.py`: Main application file
- `templates/`: HTML templates for the web interface
- `static/`: Static assets (CSS, JS, images)
- `build_executable.sh`: Script to build the standalone executable
- `requirements.txt`: Python dependencies

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project uses data from Naver Real Estate API
- Built with Flask and Bootstrap for the web interface
