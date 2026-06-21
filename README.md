# ⚙️ AutoShip — CI/CD Pipeline with Automated Testing & Containerisation

<div align="center">

[![CI](https://github.com/Ayeshaa-w/ci-cd-python/actions/workflows/ci.yml/badge.svg?style=for-the-badge)](https://github.com/Ayeshaa-w/ci-cd-python/actions)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerised-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Manifest-326CE5?logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-2088FF?logo=github-actions&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-ubuntu--latest-E95420?logo=ubuntu&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-6%20Tests-green?logo=pytest&logoColor=white)
![Secrets](https://img.shields.io/badge/Secrets-GitHub_Vault-red?logo=github&logoColor=white)

</div>
<div align="center">
  
  **[🔗Read blog on Hashnode](https://ayeshaa.hashnode.dev/i-built-a-ci-cd-pipeline-from-scratch-as-a-beginner-here-s-every-error-i-hit-and-how-i-fixed-them)**
</div>

> A production-style DevOps pipeline built around a containerised Flask REST API.
> The focus isn't the app — it's the **engineering system** around it.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Flask | REST API framework |
| Pytest | Automated testing (6 tests) |
| Docker | Containerisation |
| GitHub Actions | CI/CD pipeline |
| Kubernetes | Container orchestration (2 replicas) |
| GitHub Secrets | Encrypted secrets management |
| Linux (ubuntu-latest) | Pipeline runtime |

---

## 🔄 Pipeline Flow

```
git push → GitHub Actions triggers
              ↓
         Ubuntu runner spins up
              ↓
         pip install dependencies
              ↓
         pytest runs 6 tests
              ↓
    ┌─────────────────────┐
    │  any test fails?    │
    └─────────────────────┘
         ↓ YES              ↓ NO
      ❌ STOP          Secrets injected
   never deploys       from GitHub Vault
                            ↓
                       docker build
                            ↓
                     ✅ Pipeline green
```

---

## 🚀 API Endpoints

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| `POST` | `/items` | Create a new item | `201 Created` |
| `GET` | `/items` | Retrieve all items | `200 OK` |
| `GET` | `/items/:id` | Retrieve one item | `200 OK` |
| `DELETE` | `/items/:id` | Delete an item | `200 OK` |

## 🔐 Secrets Management
```python
# ✅ Read from environment — secret never in code
import os
API_KEY = os.environ.get('API_KEY')
```
## 🧠 Key Engineering Decisions

**#Stateless design**
Any container can handle any request — essential for horizontal scaling.

**#Fail-fast pipeline**
Bad code is caught at the test stage. Docker never builds broken code. Problems surface immediately at the source, not in production.

**#2 Kubernetes replicas**
High availability.Zero downtime.

**#Structured logging**
In production this feeds into monitoring tools (Grafana, CloudWatch) for full observability.

**#GitHub Secrets over .env files**
`.env` files can accidentally get committed. GitHub Secrets are encrypted at rest, injected only at runtime, and never visible in logs or history — even to repo owners.

---

## 🔧 Local Setup

```bash
# Clone the repo
git clone https://github.com/Ayeshaa-w/ci-cd-python.git
cd ci-cd-python

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Run tests
pytest test_app.py -v

# Run with Docker
docker build -t autoship .
docker run -p 5000:5000 autoship
```

---

## 👩‍💻 Author

**Ayesha Zafreen S**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ayesha--Zafreen--S-blue?logo=linkedin)](https://linkedin.com/in/Ayesha-Zafreen-S)

---

*Built as part of a backend + cloud engineering learning path.*
*Every red ❌ in the Actions tab is a debugging story. Every green ✅ is a win.*
