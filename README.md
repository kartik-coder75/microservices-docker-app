# Build, Deploy and Analyze a Containerized Microservice Application Under Varying Workloads

> **Lab Evaluation Experiment** — Microservices, Docker, Docker Compose and Performance Analysis

---

## Table of Contents

1. [Aim](#aim)
2. [Project Overview](#project-overview)
3. [General Instructions Followed](#general-instructions-followed)
4. [Architecture](#architecture)
5. [Repository Structure](#repository-structure)
6. [Technology Stack](#technology-stack)
7. [Checkpoint 1 — Design and Develop the Microservices](#checkpoint-1--design-and-develop-the-microservices)
8. [Checkpoint 2 — Containerize and Deploy the Application](#checkpoint-2--containerize-and-deploy-the-application)
9. [Checkpoint 3 — Establish and Demonstrate Microservice Communication](#checkpoint-3--establish-and-demonstrate-microservice-communication)
10. [Checkpoint 4 — Generate Varying Workloads and Monitor Performance](#checkpoint-4--generate-varying-workloads-and-monitor-performance)
11. [Checkpoint 5 — Analyze and Present the Results](#checkpoint-5--analyze-and-present-the-results)
12. [How to Run the Project](#how-to-run-the-project)
13. [Evaluation Scheme](#evaluation-scheme)
14. [Final Deliverables Checklist](#final-deliverables-checklist)
15. [Conclusion](#conclusion)
16. [Author](#author)

---

## Aim

To develop a microservice-based application containing three independent services, containerize and deploy the services using Docker, establish inter-service communication, generate varying workloads, monitor resource utilization, and analyze application performance.

---

## Project Overview

| Item | Details |
|------|---------|
| **Application Domain** | Order Management |
| **Number of Microservices** | 3 |
| **Programming Language / Framework** | Python Flask |
| **Containerization** | Docker |
| **Orchestration / Deployment** | Docker Compose |
| **Load Testing Tool** | Custom Python script |
| **Monitoring Tool** | docker stats |

**Short description of the application:**

A 3-tier microservice application simulating an e-commerce order workflow. The order-service acts as an entry API gateway that orchestrates end-to-end order processing by synchronously querying user-service for customer profile verification and triggering notification-service to deliver status alerts over an isolated Docker bridge network.

---

## General Instructions Followed

- The application contains **exactly three independent microservices**.
- Each microservice has a **clear responsibility** and **at least one working REST API endpoint**.
- **Docker** is used to containerize every service, and **Docker Compose** is used for deployment.
- Workload testing was performed and **actual measured values** were used for the analysis.
- Each checkpoint was demonstrated to the evaluator before proceeding to the next one.

---

## Architecture

### Minimum Required Architecture

```
Client → Service 1 → Service 2 / Service 3
```

### Architecture of This Project

```
                      ┌──────────────────────────┐
                      │          Client          │
                      │ (Browser / curl / Tool)  │
                      └────────────┬─────────────┘
                                   │  HTTP
                                   ▼
                      ┌──────────────────────────┐
                      │ Service 1: order-service   │
                      │ Port: 5001                 │
                      └─────┬──────────────┬─────┘
                            │              │
              (service name)│              │(service name)
                            ▼              ▼
          ┌───────────────────────┐   ┌───────────────────────┐
          │ Service 2: user-service│   │ Service 3: notification-service│
          │ Port: 5002             │   │ Port: 5003                     │
          └───────────────────────┘   └───────────────────────┘

            All services run on the same Docker Compose network
```


### Communication Flow

Client calls order-service at http://localhost:5001/order → order-service calls user-service (http://user-service:5000/user) for user profile details → order-service calls notification-service (http://notification-service:5000/notify) to trigger order notifications → combined aggregated response is returned to the client.

---

## Repository Structure

```
<FILL: adjust to match your repository>
.
├── service1/
│   ├── app.py (or index.js / Main.java)
│   ├── requirements.txt (or package.json / pom.xml)
│   └── Dockerfile
├── service2/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── service3/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── load_test/
│   └── <load testing script / results>
├── results/
│   ├── observations.csv
│   └── docker_stats_logs/
├── images/
│   └── <screenshots and graphs>
└── README.md
```

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language / Framework | `<FILL>` |
| Containerization | Docker `<version>` |
| Deployment | Docker Compose `<version>` |
| Load Testing | `<FILL>` |
| Monitoring | `docker stats` |
| Graph Plotting | `<FILL: e.g., Excel / Matplotlib / Google Sheets>` |

---

## Checkpoint 1 — Design and Develop the Microservices

### Tasks

1. Select an application domain.
2. Identify three independent microservices.
3. Define the responsibility of each service.
4. Implement the three services using a suitable programming language/framework.
5. Create REST API endpoints for each service.
6. Run and test each service independently.
7. Verify that the APIs return the expected responses.

> **Completion condition:** All three microservices are independently working and their APIs can be demonstrated.

### Selected Domain

`<FILL: domain name and a brief justification>`

### Microservices and Their Responsibilities

| Service | Name | Responsibility | Port |
|---------|------|----------------|------|
| Service 1 | `<FILL>` | `<FILL>` | `<FILL>` |
| Service 2 | `<FILL>` | `<FILL>` | `<FILL>` |
| Service 3 | `<FILL>` | `<FILL>` | `<FILL>` |

### REST API Endpoints

**Service 1 — `<FILL NAME>`**

| Method | Endpoint | Description | Sample Response |
|--------|----------|-------------|-----------------|
| `GET` | `<FILL>` | `<FILL>` | `<FILL>` |

**Service 2 — `<FILL NAME>`**

| Method | Endpoint | Description | Sample Response |
|--------|----------|-------------|-----------------|
| `GET` | `<FILL>` | `<FILL>` | `<FILL>` |

**Service 3 — `<FILL NAME>`**

| Method | Endpoint | Description | Sample Response |
|--------|----------|-------------|-----------------|
| `GET` | `<FILL>` | `<FILL>` | `<FILL>` |

### Independent Testing of Each Service

```bash
# Example — replace with your own commands
curl http://localhost:<PORT1>/<endpoint>
curl http://localhost:<PORT2>/<endpoint>
curl http://localhost:<PORT3>/<endpoint>
```

📸 **Screenshots:** `<FILL: add screenshots of each service responding independently>`

`![Service 1 Test](images/service1_test.png)`
`![Service 2 Test](images/service2_test.png)`
`![Service 3 Test](images/service3_test.png)`

---

## Checkpoint 2 — Containerize and Deploy the Application

### Tasks

1. Create a separate Dockerfile for each microservice.
2. Create the required dependency/configuration files.
3. Build a Docker image for each microservice.
4. Verify that all three images are available using Docker commands.
5. Create a `docker-compose.yml` file.
6. Configure all three services in Docker Compose.
7. Deploy the complete application using Docker Compose.
8. Verify that all three containers are running.

> **Completion condition:** Three Docker images are built successfully and all three microservices are running as containers.

### Dockerfiles

A separate Dockerfile is provided for each service:

- [`service1/Dockerfile`](service1/Dockerfile)
- [`service2/Dockerfile`](service2/Dockerfile)
- [`service3/Dockerfile`](service3/Dockerfile)

### Dependency / Configuration Files

`<FILL: e.g., requirements.txt / package.json / pom.xml for each service>`

### Build Docker Images

```bash
docker build -t <service1-image-name> ./service1
docker build -t <service2-image-name> ./service2
docker build -t <service3-image-name> ./service3
```

### Verify Images

```bash
docker images
```

📸 `![Docker Images](images/docker_images.png)`

### docker-compose.yml

See [`docker-compose.yml`](docker-compose.yml).

```yaml
# <FILL: paste your docker-compose.yml here for quick reference>
```

### Deploy Using Docker Compose

```bash
docker compose up --build -d
```

### Verify Running Containers

```bash
docker ps
docker compose ps
```

📸 `![Running Containers](images/docker_ps.png)`

---

## Checkpoint 3 — Establish and Demonstrate Microservice Communication

### Tasks

1. Create/configure the Docker network through Docker Compose.
2. Connect all three services to the same application network.
3. Configure service-to-service communication using Docker service names.
4. Test communication between the microservices.
5. Perform an end-to-end request involving multiple services.
6. Verify that the final response is successfully returned to the client.

> **Completion condition:** Students demonstrate successful communication between the three microservices and an end-to-end request.

### Docker Network Configuration

- **Network name:** `<FILL>`
- **Network driver:** `bridge` `<FILL: confirm>`
- All three services are attached to the same network through `docker-compose.yml`.

```bash
docker network ls
docker network inspect <network-name>
```

📸 `![Docker Network](images/docker_network.png)`

### Service-to-Service Communication (Using Docker Service Names)

| Caller | Callee | URL Used (Docker Service Name) | Purpose |
|--------|--------|--------------------------------|---------|
| Service 1 | Service 2 | `http://<service2-name>:<port>/<endpoint>` | `<FILL>` |
| Service 1 | Service 3 | `http://<service3-name>:<port>/<endpoint>` | `<FILL>` |

### End-to-End Request

```bash
curl http://localhost:<PORT>/<end-to-end-endpoint>
```

**Sample Response:**

```json
{
  "FILL": "paste the final combined response here"
}
```

📸 `![End-to-End Request](images/end_to_end.png)`

---

## Checkpoint 4 — Generate Varying Workloads and Monitor Performance

### Tasks

1. Select an API suitable for workload testing.
2. Use a load-testing tool or create a suitable workload generator.
3. Test the application using at least five workload levels.
4. A suggested workload is 1, 2, 4, 8, and 16 concurrent requests.
5. Record response time and throughput for every workload.
6. Monitor all three containers using `docker stats` or another suitable monitoring method.
7. Record CPU and memory utilization.
8. Record successful and failed requests, if applicable.

> **Completion condition:** Performance measurements are collected for all workload levels.

### API Selected for Workload Testing

- **Endpoint:** `<FILL>`
- **Reason for selection:** `<FILL: e.g., it involves all three services, so it reflects the full end-to-end load>`

### Load-Testing Tool / Workload Generator

- **Tool:** `<FILL>`
- **Total requests per workload:** `<FILL>`
- **Test duration (if applicable):** `<FILL>`

### Suggested Workload Levels

| Test | Concurrent Requests |
|------|---------------------|
| W1 | 1 |
| W2 | 2 |
| W3 | 4 |
| W4 | 8 |
| W5 | 16 |

### Commands Used

```bash
# Load test command (replace with yours)
<FILL: e.g., ab -n 1000 -c 1 http://localhost:<PORT>/<endpoint>>

# Container monitoring
docker stats
```

### Monitoring Method

All three containers were monitored using `docker stats` `<FILL: or other method>` while each workload was running. The peak/average CPU and memory utilization of each container was recorded.

📸 `![Docker Stats](images/docker_stats.png)`

### Raw Measurements — Per-Container Resource Utilization

**Service 1 — `<FILL NAME>`**

| Workload | Concurrency | CPU (%) | Memory (MiB / %) |
|----------|-------------|---------|------------------|
| W1 | 1 | | |
| W2 | 2 | | |
| W3 | 4 | | |
| W4 | 8 | | |
| W5 | 16 | | |

**Service 2 — `<FILL NAME>`**

| Workload | Concurrency | CPU (%) | Memory (MiB / %) |
|----------|-------------|---------|------------------|
| W1 | 1 | | |
| W2 | 2 | | |
| W3 | 4 | | |
| W4 | 8 | | |
| W5 | 16 | | |

**Service 3 — `<FILL NAME>`**

| Workload | Concurrency | CPU (%) | Memory (MiB / %) |
|----------|-------------|---------|------------------|
| W1 | 1 | | |
| W2 | 2 | | |
| W3 | 4 | | |
| W4 | 8 | | |
| W5 | 16 | | |

---

## Checkpoint 5 — Analyze and Present the Results

### Tasks

1. Prepare an observation table containing workload, concurrency, response time, throughput, failed requests, CPU utilization, and memory utilization.
2. Create suitable graphs from the measured results.
3. Compare application performance at different workload levels.
4. Identify how increasing workload affects the application.
5. Identify which microservice consumes more resources.
6. Explain any performance degradation or failures observed.
7. Demonstrate the complete application to the evaluator.
8. Explain the architecture, containerization, communication, workload testing, and performance results.

> **Completion condition:** Students demonstrate the complete experiment and explain their measured results.

### Performance Observation Table

| Workload | Concurrency | Avg. Response Time (ms) | Throughput (req/s) | Failed Requests | CPU (%) | Memory (MiB) |
|----------|-------------|-------------------------|--------------------|-----------------|---------|--------------|
| W1 | 1 | | | | | |
| W2 | 2 | | | | | |
| W3 | 4 | | | | | |
| W4 | 8 | | | | | |
| W5 | 16 | | | | | |

> *CPU and Memory here can be the total across all three containers, or you can refer to the per-container tables in Checkpoint 4.*

### Performance Graphs

**1. Concurrent Requests vs Average Response Time**

`![Concurrency vs Response Time](images/graph_response_time.png)`

**2. Concurrent Requests vs Throughput**

`![Concurrency vs Throughput](images/graph_throughput.png)`

**3. Concurrent Requests vs CPU Utilization**

`![Concurrency vs CPU](images/graph_cpu.png)`

**4. Concurrent Requests vs Memory Utilization**

`![Concurrency vs Memory](images/graph_memory.png)`

### Analysis

**Comparison of performance at different workload levels:**

`<FILL>`

**Effect of increasing workload on the application:**

- Response time: `<FILL>`
- Throughput: `<FILL>`
- CPU utilization: `<FILL>`
- Memory utilization: `<FILL>`
- Failed requests: `<FILL>`

**Microservice consuming the most resources:**

`<FILL: name the service and justify it using your measured CPU/memory values>`

**Performance degradation / failures observed and their explanation:**

`<FILL: e.g., point at which response time rose sharply, saturation of throughput, errors/timeouts, and the likely cause>`

### Architecture, Containerization, Communication and Workload Testing — Summary

| Area | Summary |
|------|---------|
| Architecture | `<FILL>` |
| Containerization | `<FILL>` |
| Communication | `<FILL>` |
| Workload Testing | `<FILL>` |
| Performance Results | `<FILL>` |

---

## How to Run the Project

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed
- `<FILL: any load-testing tool needed, e.g., Apache Bench / Locust / k6>`

### Steps

```bash
# 1. Clone the repository
git clone <FILL: your-repo-url>
cd <FILL: repo-folder>

# 2. Build and start all three services
docker compose up --build -d

# 3. Verify that all three containers are running
docker compose ps

# 4. Test the end-to-end API
curl http://localhost:<PORT>/<endpoint>

# 5. Run the load test (example)
<FILL: your load test command or script>

# 6. Monitor resource usage in another terminal
docker stats

# 7. Stop and remove the containers
docker compose down
```

---

## Evaluation Scheme

**Final Evaluation — 5 Marks**

| Checkpoint | Evaluation Area | Marks |
|------------|-----------------|-------|
| 1 | Design and develop 3 microservices | 1 |
| 2 | Containerize and deploy using Docker | 1 |
| 3 | Establish and demonstrate inter-service communication | 1 |
| 4 | Generate varying workloads and monitor performance | 1 |
| 5 | Analyze results and demonstrate the complete experiment | 1 |
| | **TOTAL** | **5** |

---

## Final Deliverables Checklist

- [ ] Source code of the three microservices
- [ ] Three Dockerfiles
- [ ] `docker-compose.yml`
- [ ] Running Docker containers
- [ ] Demonstration of inter-service communication
- [ ] Workload test results
- [ ] CPU and memory observations
- [ ] Performance observation table
- [ ] Performance graphs
- [ ] Brief analysis and conclusion

---

## Workflow

```
DEVELOP → CONTAINERIZE → DEPLOY → CONNECT → LOAD TEST → MONITOR → ANALYZE → DEMONSTRATE
```

---

## Conclusion

`<FILL: 4–6 lines summarizing what was built, how the application behaved as workload increased from 1 to 16 concurrent requests, which service was the bottleneck, and what you learned about containerized microservices.>`

---

## Author

| | |
|---|---|
| **Name** | `<FILL>` |
| **Register / Roll No.** | `<FILL>` |
| **Course / Department** | `<FILL>` |
| **Institution** | `<FILL>` |
