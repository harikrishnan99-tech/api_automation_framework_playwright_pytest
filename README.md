```sh
# API Automation Framework

A robust API test automation framework built with **pytest** and **Playwright**, featuring async test execution, structured reporting via Allure, and seamless CI/CD integration through Jenkins.

---

## 📁 Project Structure

```
project-root/
├── tests/                    # Test files
├── reports/
│   └── allure-results/       # Allure test results output
├── pytest.ini                # Pytest configuration
├── Jenkinsfile               # CI/CD pipeline definition
├── requirements.txt          # Python dependencies
└── README.md
```

---

## ⚙️ Prerequisites

- Python 3.9+
- pip
- Java (required for Allure CLI)
- Jenkins (for CI/CD pipeline)
- Allure Jenkins Plugin

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/harikrishnan99-tech/api_automation_framework_playwright_pytest.git
cd api_automation_framework_playwright_pytest
```

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🐳 Running with Docker

For easy setup and execution without installing dependencies locally, use Docker.

### Prerequisites
- Docker installed on your system

### Build and Run

1. **Build the Docker image:**
   ```bash
   docker build -t api-automation .
   ```

2. **Run tests with report output:**
   ```bash
   docker run --rm -v $(pwd)/reports:/app/reports api-automation
   ```

   This command:
   - Builds and runs the tests in a container
   - Mounts your local `reports/` directory to access Allure results
   - Generates Allure reports that you can view locally

3. **View the Allure report:**
   ```bash
   allure serve reports/allure-results
   ```

### Alternative: Run without mounting reports
If you don't need to access reports locally:
```bash
docker run --rm api-automation
```

---

## 🧪 Running Tests

### Run All Tests

```bash
pytest
```

### Run with Allure Reporting

```bash
pytest --alluredir=reports/allure-results
```

### Run by Marker

```bash
# Run healthcheck suite
pytest -m healthcheck

# Run smoke tests
pytest -m smoke
```

### View Allure Report Locally

```bash
allure serve reports/allure-results
```

---

## 🔖 Test Markers

Markers are defined in `pytest.ini` and can be used to target specific test groups:

| Marker | Description |
|---|---|
| `healthcheck` | Full API Healthcheck Suite |
| `smoke` | Smoke tests — Critical happy path scenarios |

---

## 📋 Configuration — `pytest.ini`

```ini
[pytest]
addopts =
    -v
    --alluredir=reports/allure-results
testpaths = tests
pythonpath = .
asyncio_mode = auto
log_cli = true
log_level = DEBUG
markers =
    healthcheck: Full API Healthcheck Suite
    smoke: Smoke tests (Critical happy path)
```

| Setting | Purpose |
|---|---|
| `asyncio_mode = auto` | Enables async test support without explicit decorators |
| `log_cli = true` | Streams logs to the console during test execution |
| `log_level = DEBUG` | Captures verbose output for debugging |
| `testpaths = tests` | Scopes test discovery to the `tests/` directory |
| `pythonpath = .` | Adds the project root to the Python path |

---

## 🔁 CI/CD Pipeline — Jenkins

The `Jenkinsfile` defines a declarative Jenkins pipeline with the following stages:

```
Checkout Code → Setup Python Environment → Run Tests → Generate Allure Report
```

### Pipeline Stages

| Stage | Description |
|---|---|
| **Checkout Code** | Clones the `main` branch from the repository |
| **Setup Python Environment** | Creates a virtualenv and installs dependencies |
| **Run Tests** | Executes all pytest tests with Allure output |
| **Generate Allure Report** | Publishes the Allure report via the Jenkins plugin |

### Post-Build Notifications

| Status | Behaviour |
|---|---|
| Always | Prints execution completed message |
| Success ✅ | Prints test passed confirmation |
| Failure ❌ | Prints test failure alert |

### Setup in Jenkins

1. Install the **Allure Jenkins Plugin** from the Plugin Manager.
2. Create a new **Pipeline** job.
3. Point the pipeline to your repository's `Jenkinsfile`.
4. Trigger a build — the Allure report will be published automatically after each run.

---

## 📊 Reporting

This framework uses **Allure** for rich, interactive test reports.






































This project is for internal use. Please refer to your organization's licensing policy.## 📄 License---4. Follow the existing project structure and naming conventions.3. Ensure all tests pass locally before raising a PR.2. Write tests with appropriate markers (`smoke` or `healthcheck`).1. Create a feature branch from `main`.## 🤝 Contributing---```playwright install```bashInstall Playwright browsers after pip install:```allure-pytestpytest-asynciopytest-playwrightpytest```Key packages expected in `requirements.txt`:## 📦 Dependencies---- For local viewing, run `allure serve reports/allure-results`.- The Jenkins pipeline publishes the Allure report automatically after the test stage.- Results are written to `reports/allure-results/` on every test run.- Results are written to `reports/allure-results/` on every test run.
- The Jenkins pipeline publishes the Allure report automatically after the test stage.
- For local viewing, run `allure serve reports/allure-results`.

---

## 📦 Dependencies

Key packages expected in `requirements.txt`:

```
pytest
pytest-playwright
pytest-asyncio
allure-pytest
```

Install Playwright browsers after pip install:

```bash
playwright install
```

---

## 🤝 Contributing

1. Create a feature branch from `main`.
2. Write tests with appropriate markers (`smoke` or `healthcheck`).
3. Ensure all tests pass locally before raising a PR.
4. Follow the existing project structure and naming conventions.

---

## 📄 License

This project is for internal use. Please refer to your organization's licensing policy.
```