# SBF Week 4 - Authentication, Validation, and Best Practices

## Getting Started

### 1. Clone this repo
```bash
git clone https://github.com/helvenmarcia/sbf-auth.git
cd sbf-auth
```

### 2. Create a virtual environment
**Windows (PowerShell)**
```powershell
python -m venv env
.venv\Scripts\Activate
```
**macOS / Linux (bash/zsh)**
```bash
python3 -m venv env
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```
