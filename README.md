# Simple Term Deposit Calculator

This repository contains the Simple Term Deposit Calculator application, available as both a Command-Line Interface (CLI) and a Python Package Dependency.

<img src="https://github.com/mattcoulter7/Simple-Term-Deposit-Calculator/blob/master/assets/icon.png?raw=true" alt="icon" width="400"/>

## Running the Application

The CLI application can be run in **three** different environments:
- CLI
- Windows Executable
- Docker Container

Please ensure your system is set up with the necessary environment requirements for each environment respectively.

### Assumptions
To run this application, the following system environment setup is assumed:

1. For **CLI**:
   - **Python version**: Ensure Python 3.9 or later is installed:
      ```bash
      python --version
      ```
   - **Pip installation**: Ensure pip is installed:
      ```bash
      python -m ensurepip
      ```
   - **Update pip**: Upgrade pip to the latest version:
      ```bash
      python -m pip install --upgrade pip
      ```
   - **Install Poetry**: Install the Poetry package manager:
      ```bash
      pip install poetry
      ```
2. For **[Optional] Docker (*for Docker environment only*)**:
   - **Docker**: Ensure Docker is installed and available from the command line.
   - **Docker Compose**: Ensure Docker Compose is installed and available from the command line.
3. For **[Optional] Windows (*for Windows Executable environment only*)**:
   - **Support for .exe**: Ensure you can run Windows executables.

### How to run the code

Start by cloning this repository:
```bash
git clone https://github.com/mattcoulter7/Simple-Term-Deposit-Calculator
cd Simple-Term-Deposit-Calculator
```

#### CLI

To run the CLI, first set up the environment:

1. **Install dependencies**: Install project dependencies:
   ```bash
   poetry install --with dev
   ```

Once the environment is set, you can explore the available commands by running:
```bash
poetry run simple_term_deposit_calculator --help
```

To run the application in interactive mode:
```bash
poetry run simple_term_deposit_calculator
```

Alternatively, calculate the output with a single command:
```bash
poetry run simple_term_deposit_calculator --deposit-amount 10000 --interest-rate 1.1 --investment-term 36 --interest-paid AT_MATURITY
```

#### Windows Executable

For Windows users, the compiled executable is available for download from the zip file in the [latest release](https://github.com/mattcoulter7/Simple-Term-Deposit-Calculator/releases).

After unzipping, run the executable and the CLI will open in interactive mode.

#### Docker Container

You can also run the application within a Docker container named **simple-term-deposit-calculator-cli**:
```bash
docker compose -f docker-compose.yml up --build
```
*Note: The Docker container runs in non-interactive mode, and inputs are hard-coded in the Docker Compose file.*

### How to run the tests

Tests are located in the `./tests` directory. To run the tests:
```bash
pytest
```

Alternatively, you can run tests within the Docker container called **simple-term-deposit-calculator-test**:
```bash
docker compose -f docker-compose.yml up --build
```

There is also another test container called **simple-term-deposit-calculator-test-with-debugging**, which runs pytest with remote debugging. This is particularly useful if the tests pass on your local machine but not in the Docker container, or vice-versa.

---

## Using this repository as a Python package

To incorporate this package into your own Python application, add it as a dependency via the GitHub link.

### Installation

Install the package using pip as a Git dependency:
```bash
pip install "git+https://github.com/mattcoulter7/Simple-Term-Deposit-Calculator@master"
```

### Usage Example

Then, you can use the code as shown below:
```python
# 1. Import the calculator
from simple_term_deposit_calculator.calculator.simple import SimpleTermDepositCalculator

# 2. Import the InterestPaid enum
from simple_term_deposit_calculator.schemas.interest_paid import get_interest_paid_rule

# 3. Create a calculator instance
calculator = SimpleTermDepositCalculator()

# 4. Compute the term deposit
final_balance = calculator.calculate(
    deposit_amount=10000,      # float
    interest_rate=0.011,         # float
    investment_term=36,        # int (in months)
    interest_paid=get_interest_paid_rule("AT_MATURITY")  # support values: MONTHLY, QUARTERLY, ANNUALLY, AT_MATURITY
)
```

---

## Design Decisions

### Data Types
When choosing the data types for the various inputs/outputs of the calculator, some choices, like **Deposit Amount** and **Interest Rate**, were straightforward, while others required additional consideration. These considerations mainly came down to the future scalability of the application.

- **Investment Term Data Type**  
  Based on the web application at https://www.bendigobank.com.au/calculators/deposit-and-savings/, the smallest unit of time for the investment term is months. Therefore, supporting shorter time periods (e.g. weeks or days) or using a duration object seemed unnecessary. Separating months and years would also overcomplicate the solution, as their relationships are linear.

- **Interest Paid Data Type**  
  I considered either implementing a static enum or using a dynamic data type that would allow configuring the `InterestPaidType` (see *Code Abstraction section below*) and custom periods. While the latter is more scalable, it would require a factory pattern to instantiate based on user input. Given that the calculator is unlikely to support more `InterestPaid` values in the future, I implemented the static approach.

- **Calculator Output Data Type**  
  The web application outputs multiple values such as:
  - Final balance
  - Total interest earned
  - Interest earned present value

  However, since this project only requires the Final balance, I decided to return a float for simplicity. If future requirements expand to include additional outputs, it would be a good idea to upgrade the return type to `SimpleTermDepositCalculatorResult`.

### Input Validation

Typically, web-based applications include both front-end and back-end validation. In this CLI application, we have applied validations (string, range, and type) within the CLI using the `typer` module, which simplifies the process.

These validations are not applied in the calculator itself. This decision was made because the application currently interfaces only through the CLI. If someone uses this package as a dependency in their own application, they should not be limited by these validations. Incorrect types will raise a `TypeError`.

### Code Abstraction: How much is necessary?

In my resume, I highlighted my focus on expanding an application’s capabilities rather than meeting the bare minimum requirements. From my experience, not considering the bigger picture early on can create more work for developers down the line.

That said, for this single calculator project, I found that implementing additional abstraction would overcomplicate things. While I considered separating the `calculate(...)` method into different types based on `InterestPaid` (frequency-based vs event-based), the current implementation is already simple and abstraction would be unnecessary at this stage.

## Trade-offs

The two-hour time limit was generous for this project. Since I already had a Python CLI + Package template repository set up, I could quickly implement the solution with minimal effort. This allowed me more time to ensure a detailed README and to set up multiple runtime environments, demonstrating my understanding of application containerisation.
