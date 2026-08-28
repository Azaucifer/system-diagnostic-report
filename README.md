# System Diagnostic Report

A Python-based system diagnostic tool that monitors CPU, RAM, and disk usage and provides recommendations for potential performance issues.

## 📋 Description

System Diagnostic Report is a Python program that checks the current system resource usage and generates a diagnostic report. The program checks CPU usage, RAM usage, and disk usage using the `psutil` library.

I made this project because I wanted to build something practical that uses Python to interact with the computer instead of just taking input and producing an output. The program gets the current CPU, RAM, and disk usage and then checks whether each resource is in a normal, warning, or critical state.

### Resource Status Levels

| Level        | Threshold     | Icon |
| :----------- | :------------ | :--: |
| **NORMAL**   | Below 70%     |   ✓  |
| **WARNING**  | 70% – 89%     |   ⚠  |
| **CRITICAL** | 90% and above |   ✗  |

## 🚀 Features

* 📊 Monitors CPU, RAM, and disk usage
* ⚠️ Identifies the current status of each resource
* 💡 Provides recommendations for resources with high usage
* 🔍 Generates an overall assessment of system performance
* 🧪 Includes automated tests using `pytest`
* 📋 Displays a formatted diagnostic report in the terminal
* 🔧 Uses separate functions for system statistics, analysis, recommendations, and reporting

## 📁 Project Structure

```text
system-diagnostic-report/
├── system_diagnostic_report.py          # Main program
├── test_system_diagnostic_report.py     # Test suite
├── requirements.txt                     # Project dependencies
├── README.md                            # Project documentation
└── .gitignore                           # Git ignore rules                                    
```

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/azaucifer/system-diagnostic-report.git
cd system-diagnostic-report
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the diagnostic tool with:

```bash
python project.py
```

The program will collect the current CPU, RAM, and disk usage and display a formatted diagnostic report.

### Example Output

```text
╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                          SYSTEM DIAGNOSTIC REPORT                                                   ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

                                              RESOURCE STATUS
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

CPU       25%     ✓ NORMAL
RAM       67%     ✓ NORMAL
Disk      82%     ⚠ WARNING

                                           LIKELY PERFORMANCE ISSUES
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

• Disk space is getting low.

                                                RECOMMENDATIONS
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

→ Disk space is getting low. Consider removing unnecessary files or uninstalling unused applications.

                                               OVERALL ASSESSMENT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

⚠ Your system may be experiencing performance issues primarily due to low available disk space.

=======================================================================================================================
                                                END OF REPORT
=======================================================================================================================
```

## 🧪 Testing

The project uses `pytest` to test the main functions.

Run the tests with:

```bash
pytest test_project.py
```

### Tested Functions

* `analyze_performance()`
* `overall_assessment()`
* `generate_recommendations()`

### Test Scenarios

The test suite covers:

* Normal resource usage
* Warning resource usage
* Critical resource usage
* Mixed resource statuses
* Boundary values such as 69%, 70%, 89%, and 90%
* Different combinations of CPU, RAM, and disk problems
* Recommendations for warning and critical resources

### Current Test Result

```text
18 passed
```

## 🛠️ Design Choices

I divided the program into separate functions instead of putting everything inside `main()`. This makes the code easier to understand and allows individual parts of the program to be tested independently.

The `get_system_stats()` function collects the current CPU, RAM, and disk usage. The `analyze_performance()` function then determines the status of each resource.

The `overall_assessment()` function looks at the resource statuses and identifies the main performance problems. The `generate_recommendations()` function creates recommendations for resources that are in a warning or critical state.

Finally, `display_report()` presents the results in a formatted terminal report.

I chose 70% and 90% as the thresholds for the three resource states. Usage below 70% is considered normal, usage from 70% to 89% is considered a warning, and usage of 90% or higher is considered critical.

I used `psutil` because it provides a straightforward way to access system information such as CPU, memory, and disk usage from Python.

I also used Unicode symbols such as `✓`, `⚠`, and `✗` to make the different resource states easier to identify in the terminal.

## 📄 Requirements

* Python 3
* `psutil`
* `pytest`

Install the required libraries with:

```bash
pip install -r requirements.txt
```

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome.

If you find a bug or have an idea for a feature, feel free to open an issue or submit a pull request.

## 👤 Author

**Syed Shams Junaid**

GitHub: [Azaucifer](https://github.com/Azaucifer)

---

⭐ If you find this project useful, consider giving it a star!
