# ZEOTAP-Assignment


Here’s a comprehensive README file for both assignments, including build instructions and design choices.

Project 1: Rule Engine with AST
Overview
This project implements a 3-tier rule engine for evaluating user eligibility based on various attributes such as age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent, create, combine, and evaluate dynamic conditional rules. The engine provides a simple UI, API, and backend to support rule evaluations.

Features
AST-based rule representation for dynamic rule creation and evaluation.
Combining rules to form complex conditions.
Efficient rule evaluation against user-provided data (e.g., age, salary).
Support for operand changes and sub-expression modifications.
Error handling for invalid rule formats and data types.
Rule modification functionalities.
Design Choices
The use of Abstract Syntax Trees (AST) enables dynamic construction and evaluation of rules.
Rules are stored as AST nodes where operators like AND/OR and conditions (operands) are represented as different node types.
Efficiency: Combining rules leverages strategies such as eliminating redundant checks and using frequent operator heuristics to optimize rule evaluation.
Modular approach: Separate functions for rule creation (create_rule), rule combination (combine_rules), and rule evaluation (evaluate_rule) allow for easy extension and modification of the system.



Project 2: Real-Time Data Processing System for Weather Monitoring
Overview
This project implements a real-time data processing system that continuously monitors weather conditions in major Indian cities using data from the OpenWeatherMap API. The system aggregates and stores daily summaries, triggers alerts for threshold breaches, and provides visualizations of the weather data.

Features
Real-time data processing: Fetches weather data at regular intervals from OpenWeatherMap.
Rollups and Aggregates: Calculates daily summaries including average, max, and min temperature, and dominant weather condition.
Threshold alerting: Configurable thresholds trigger alerts if exceeded (e.g., temperature exceeding 35°C).
Data visualization: Displays historical weather trends using Matplotlib graphs.
Email notifications: Sends alert emails for threshold breaches.
Design Choices
The system uses the OpenWeatherMap API for retrieving weather data and processes it at regular intervals (configurable).
Data processing includes converting temperatures from Kelvin to Celsius, storing daily summaries, and calculating aggregates for further analysis.
Alerting system: Alerts are triggered after consecutive threshold breaches to avoid false positives.
Scalability: The design can be extended to handle more cities or other weather parameters such as humidity or wind speed.
Email integration allows users to receive real-time notifications.






Here’s a comprehensive README file for both assignments, including build instructions and design choices.

Project 1: Rule Engine with AST
Overview
This project implements a 3-tier rule engine for evaluating user eligibility based on various attributes such as age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent, create, combine, and evaluate dynamic conditional rules. The engine provides a simple UI, API, and backend to support rule evaluations.

Features
AST-based rule representation for dynamic rule creation and evaluation.
Combining rules to form complex conditions.
Efficient rule evaluation against user-provided data (e.g., age, salary).
Support for operand changes and sub-expression modifications.
Error handling for invalid rule formats and data types.
Rule modification functionalities.
Design Choices
The use of Abstract Syntax Trees (AST) enables dynamic construction and evaluation of rules.
Rules are stored as AST nodes where operators like AND/OR and conditions (operands) are represented as different node types.
Efficiency: Combining rules leverages strategies such as eliminating redundant checks and using frequent operator heuristics to optimize rule evaluation.
Modular approach: Separate functions for rule creation (create_rule), rule combination (combine_rules), and rule evaluation (evaluate_rule) allow for easy extension and modification of the system.
Project 2: Real-Time Data Processing System for Weather Monitoring
Overview
This project implements a real-time data processing system that continuously monitors weather conditions in major Indian cities using data from the OpenWeatherMap API. The system aggregates and stores daily summaries, triggers alerts for threshold breaches, and provides visualizations of the weather data.

Features
Real-time data processing: Fetches weather data at regular intervals from OpenWeatherMap.
Rollups and Aggregates: Calculates daily summaries including average, max, and min temperature, and dominant weather condition.
Threshold alerting: Configurable thresholds trigger alerts if exceeded (e.g., temperature exceeding 35°C).
Data visualization: Displays historical weather trends using Matplotlib graphs.
Email notifications: Sends alert emails for threshold breaches.
Design Choices
The system uses the OpenWeatherMap API for retrieving weather data and processes it at regular intervals (configurable).
Data processing includes converting temperatures from Kelvin to Celsius, storing daily summaries, and calculating aggregates for further analysis.
Alerting system: Alerts are triggered after consecutive threshold breaches to avoid false positives.
Scalability: The design can be extended to handle more cities or other weather parameters such as humidity or wind speed.
Email integration allows users to receive real-time notifications.
Installation and Setup Instructions (Both Projects)
Prerequisites
Python 3.x: Make sure Python is installed.
Docker or Podman: For running services in containers if needed (e.g., for database services).
API Key: For Project 2, sign up for a free API key from OpenWeatherMap.
Dependencies
Install the required Python packages by running:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file should contain the following dependencies:

txt
Copy code
requests
matplotlib
smtplib
For Project 1: Rule Engine with AST
No external libraries are required.
Ensure Python 3.x is installed and accessible from your terminal.
For Project 2: Real-Time Weather Monitoring
Matplotlib is used for data visualization.
Requests library is required for interacting with the OpenWeatherMap API.
Smtplib is used to send alert emails.
If you'd like to run a database to store weather summaries, Docker can be used to set up a MongoDB or MySQL container (optional).
Running with Docker (for Project 2):
Set up MongoDB or MySQL for storing weather summaries:

bash
Copy code
docker run -d -p 27017:27017 --name weatherdb mongo:latest
OR

bash
Copy code
docker run -d -p 3306:3306 --name weatherdb -e MYSQL_ROOT_PASSWORD=root mysql:latest
Update your code to connect to the database and store daily summaries.

Running the Applications
Project 1: Rule Engine with AST
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/rule-engine-ast.git
cd rule-engine-ast
Run the Python script:

bash
Copy code
python rule_engine.py
Use the provided API functions to create, combine, and evaluate rules.

Project 2: Real-Time Data Processing System for Weather Monitoring
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/weather-monitoring.git
cd weather-monitoring
Update your API key in the Python script (weather_monitoring.py):

python
Copy code
API_KEY = 'YOUR_API_KEY'
Run the Python script to start fetching and processing weather data:

bash
Copy code
python weather_monitoring.py
Visualize weather trends by calling:

bash
Copy code
python visualize_weather.py
Testing
Project 1: Rule Engine with AST
Unit tests for rule creation, combination, and evaluation can be found in the tests/ folder.
To run tests:
bash
Copy code
python -m unittest discover tests
Project 2: Real-Time Weather Monitoring
Simulate API calls and test various weather scenarios.
Ensure daily summaries are generated and threshold alerts are triggered as expected.
Visualize the weather data and ensure the trends are accurate.
Future Enhancements
Project 1: Rule Engine
Support for more complex rule types (e.g., user-defined functions within rules).
Integration with a UI for better rule creation and management.
Project 2: Weather Monitoring
Add support for additional weather parameters such as humidity and wind speed.
Extend the system to include forecasting and predictive weather analytics.
Improve alerting system with SMS or push notifications.
