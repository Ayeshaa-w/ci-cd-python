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

</div>

> A production-style DevOps pipeline built around a containerised Flask REST API.
> The focus isn't the app — it's the **engineering system** around it.

---

## 🏭 The Factory Analogy

| Layer | What It Is |
|-------|-----------|
| 🧸 Flask API | The product being built |
| 🧪 Pytest | Quality control — tests every component |
| 🐳 Docker | The packaging line — same output everywhere |
| ⚡ GitHub Actions | The automated assembly line |
| ☸️ Kubernetes | The deployment manager — scales and self-heals |

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
      ❌ STOP          docker build
   never deploys        image ready
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

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Flask | REST API framework |
| Pytest | Automated testing |
| Docker | Containerisation |
| GitHub Actions | CI/CD pipeline |
| Kubernetes | Container orchestration |
| Linux (ubuntu-latest) | Pipeline runtime |

---

## 📁 Project Structure

```
autoship/
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline definition
├── k8s/
│   └── deployment.yaml     # Kubernetes manifests
├── app.py                  # Flask REST API
├── test_app.py             # Pytest test suite
├── Dockerfile              # Container definition
├── requirements.txt        # Python dependencies
├── .gitignore              # Git exclusions
└── README.md               # You are here
```

---

## 🧠 Key Engineering Decisions

**Why stateless design?**
Every request carries all needed data. No session state stored server-side. This means any container can handle any request — essential for horizontal scaling.

**Why fail-fast pipeline?**
Bad code is caught at the test stage. Docker never builds broken code. Servers never receive broken deployments. Problems surface immediately at the source.

**Why 2 Kubernetes replicas?**
High availability. If one container crashes, the other keeps serving users while Kubernetes restarts the crashed one. Zero downtime.

**Why structured logging?**
Every request logged with timestamp and severity level. In production this feeds into monitoring tools (Grafana, CloudWatch) for observability.

---

## 👩‍💻 Author

**Ayesha Zafreen S**
[![GitHub](https://img.shields.io/badge/GitHub-Ayeshaa--w-black?logo=github)](https://github.com/Ayeshaa-w)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ayesha--Zafreen--S-blue?logo=linkedin)](https://linkedin.com/in/Ayesha-Zafreen-S)

---

*Built as part of a backend + cloud engineering learning path. Every failure in the Actions tab is a debugging story.*
