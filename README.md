# Bijira Documentation

This is the Bijira documentation repository. This repository is open and we welcome your contributions!

To see the Bijira documentation site, go to [https://wso2.com/bijira/docs/](https://wso2.com/bijira/docs/)

## Local Development Setup

This documentation site is built using [MkDocs](https://www.mkdocs.org/) with the Material theme. Follow these steps to set up and run the documentation locally.

### Prerequisites

- **Python 3.12** (required)
- **Node.js** (for spell checking and link validation tools)
- **Git** (for version control)

### Setup Instructions

#### Option 1: Automated Setup (Recommended)

Run the setup script for automatic environment configuration:

```bash
./setup-dev.sh
```

This script will:
- Check for Python 3.12+ 
- Create a virtual environment
- Install all Python dependencies
- Install Node.js validation tools (if Node.js is available)
- Provide next steps

#### Option 2: Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wso2/docs-bijira.git
   cd docs-bijira
   ```

2. **Create and activate a Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   cd en
   pip install -r requirements.txt
   ```

4. **Install Node.js tools for spell checking and link validation (optional):**
   ```bash
   npm install -g markdown-spellcheck markdown-link-check
   ```

### Running the Documentation Locally

#### Quick Start (Documentation Only)
To start the development server with live reload:

```bash
cd en
python -m mkdocs serve
```

The documentation will be available at: [http://localhost:8000/bijira/docs/](http://localhost:8000/bijira/docs/)

#### Custom Port
If port 8000 is already in use, specify a different port:

```bash
python -m mkdocs serve --dev-addr localhost:8001
```

#### Full Validation (with spell check and link validation)
If you have the Node.js tools installed, you can run the complete validation script:

```bash
./serve.sh
```

This script will:
- Run spell checking on all markdown files
- Validate all links in the documentation
- Build the static site
- List the generated files

### Building for Production

To build the static site for deployment:

```bash
cd en
python -m mkdocs build
```

The built site will be generated in the `site/` directory.

### Project Structure

```
docs-bijira/
├── en/                          # English documentation
│   ├── docs/                    # Documentation source files
│   ├── theme/                   # Custom theme files
│   ├── mkdocs.yml               # MkDocs configuration
│   ├── requirements.txt         # Python dependencies
│   └── serve.sh                 # Validation and build script
├── devportal-theming/           # Theming assets
└── README.md                    # This file
```

### Making Changes

1. Edit markdown files in the `en/docs/` directory
2. The development server will automatically reload changes
3. Preview your changes at the local development URL
4. Test links and spelling using the validation tools
5. Submit a pull request with your changes

### Troubleshooting

**Virtual environment activation issues:**
- On macOS/Linux: `source venv/bin/activate`
- On Windows: `venv\Scripts\activate`

**Port conflicts:**
Use a different port with `--dev-addr localhost:XXXX`

**Missing Node.js tools:**
The spell checking and link validation are optional. You can still build and serve the documentation without them.

**Python version issues:**
This project requires Python 3.12. Check your version with `python3 --version`
