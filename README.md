# Nuclear Fact‑Checking Platform

Fact‑checking platform focused on nuclear energy, policy, safety, technology, and public communication. Users submit statements, experts verify them, and the results are displayed publicly.

The project uses Django for backend logic and Poetry for dependency management.

## Installation & Launch Guide

### 1. Clone the repository
git clone https://github.com/jjakub542/I4N.git
cd I4N

### 2. Install dependencies using Poetry
poetry install

### 3. Activate the virtual environment
poetry shell

### 4. Apply database migrations
python manage.py migrate

### 5. Load mock data (recommended for development)
python manage.py load_mock_data

### 6. Run the development server
python manage.py runserver

Your app will be available at:
http://127.0.0.1:8000/

---

## Data Models

### Statement Model
Represents a single fact‑checked statement. Fields include:
• title — headline of the fact‑check  
• quote — the exact statement being verified  
• text — full explanation and verification  
• author_name — person who made the statement  
• author_role — political party, organization, or affiliation  
• read_time_minutes — estimated reading time  
• status — verdict (True, False, Misleading, etc.)  
• tags — thematic categories  
• created_at, updated_at — timestamps  
• author_initials — auto‑generated avatar initials

### Tag Model
Simple label used for filtering and categorization.

### VerificationStatus Enum
Defines allowed verdicts:
True, False, Misleading, Unverified, In Progress, Unverifiable.

---

## Frontend Components

### statement_card.html
A reusable Django template component rendering:
• verdict badge  
• date + read time  
• title  
• quote  
• author name + role  
• tags  
• avatar initials  
• responsive layout  
• equal‑height cards

### home.html
Displays all statements in a responsive grid using the card component.

---

## Mock Data

The project includes a management command:
python manage.py load_mock_data

It loads 10+ realistic nuclear‑energy statements with varied verdicts, authors, quotes, tags, and reading times.
