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

### Example Request
```bash
curl -X POST http://localhost:5000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "MacBook Pro"}'
```

### Example Response
```json
{
    "id": 1,
    "name": "MacBook Pro"
}
```

---

## 🧪 Test Coverage

```
test_create_item     ✅ POST creates item with correct ID
test_get_items       ✅ GET returns all stored items
test_get_single_item ✅ GET /id returns correct item
test_delete_item     ✅ DELETE removes item successfully
test_missing_field   ✅ POST without name returns 400
test_not_found       ✅ GET unknown ID returns 404
```

Run tests locally:
```bash
pytest test_app.py -v
```

---

## 🔐 Secrets Management

**The problem with hardcoding credentials:**
```python
# ❌ NEVER do this — anyone who sees your code sees your secrets
API_KEY = "my-secret-key-123"
DB_PASSWORD = "password123"
```

Leaked API keys can cost thousands in cloud bills or expose user data.

**How AutoShip handles it:**
```python
# ✅ Read from environment — secret never in code
import os
API_KEY = os.environ.get('API_KEY')
```

Secrets are stored **encrypted** in GitHub's vault:

```
GitHub repo Settings
    → Secrets and variables
        → Actions
            → API_KEY  (encrypted, never visible after saving)
```

During the pipeline, GitHub injects the secret as an environment variable:

```yaml
- name: Build Docker image
  run: docker build -t flask-api .
  env:
    API_KEY: ${{ secrets.API_KEY }}  ← injected at runtime, never logged
```

**What this means:**
- Secret never appears in code ✅
- Secret never appears in git history ✅
- Secret never appears in pipeline logs ✅
- Only the runner gets it, only at runtime ✅

This is production-standard secrets management used at every major tech company.

---

## 🐳 Run With Docker

```bash
# Build the image
docker build -t autoship .

# Run the container
docker run -p 5000:5000 autoship
```

One command. Any machine. Identical result.

---

## ☸️ Kubernetes Deployment

Manifests in `/k8s`:
- `deployment.yaml` — runs **2 replicas** for high availability
- Service exposes the API on port `80`, forwarding to Flask on `5000`

```bash
kubectl apply -f k8s/deployment.yaml
```

If one container crashes → Kubernetes auto-restarts it. Zero downtime.

---
## 📁 Project Structure

```
autoship/
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline definition + secrets injection
├── k8s/
│   └── deployment.yaml     # Kubernetes manifests (2 replicas)
├── app.py                  # Flask REST API (CRUD + logging + validation)
├── test_app.py             # Pytest test suite (6 tests)
├── Dockerfile              # Container definition
├── requirements.txt        # Python dependencies
├── .gitignore              # Git exclusions (no secrets, no pycache)
└── README.md               # You are here
```

---

## 🧠 Key Engineering Decisions

**Why stateless design?**
Every request carries all needed data. No session state stored server-side. Any container can handle any request — essential for horizontal scaling.

**Why fail-fast pipeline?**
Bad code is caught at the test stage. Docker never builds broken code. Problems surface immediately at the source, not in production.

**Why 2 Kubernetes replicas?**
High availability. If one container crashes, the other keeps serving users while Kubernetes restarts the crashed one. Zero downtime.

**Why structured logging?**
Every request logged with timestamp and severity level. In production this feeds into monitoring tools (Grafana, CloudWatch) for full observability.

**Why GitHub Secrets over .env files?**
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
[![GitHub](https://img.shields.io/badge/GitHub-Ayeshaa--w-black?logo=github)](https://github.com/Ayeshaa-w)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ayesha--Zafreen--S-blue?logo=linkedin)](https://linkedin.com/in/Ayesha-Zafreen-S)

---

*Built as part of a backend + cloud engineering learning path.*
*Every red ❌ in the Actions tab is a debugging story. Every green ✅ is a win.*
