# Spectrum

Spectrum is a comprehensive Individualized Curriculum Plan (ICP) management system designed to streamline the process of creating, managing, and tracking ICPs for students with diverse learning needs.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/bNfoqV?referralCode=NC4Tt6)

## Project Status

🚧 **Work in Progress** 🚧

This project is currently under active development. Features and documentation are being added and refined regularly.

## Features (Planned/In Progress)

- Student profile management
- ICP creation and customization
- Goal setting and tracking
- Progress monitoring
- Document generation (PDF ICPs)
- Collaborative team input
- Reporting and analytics

## Getting Started

If you are trying to run this application, please use the deployment button above to deploy the application to Railway. If you are trying to run this application locally, you can follow the instructions below.

### Prerequisites

- Docker
- Docker Compose
- UV

### Running the Development Environment

First run redis and postgres containers that are required for the application to run.

```bash
sudo docker rm -f $(sudo docker ps -aq) && sudo docker compose -f dev.docker-compose.yml up -d
```

Then install the dependencies and run the application.

```bash
uv sync
```

## Contributing

As this project is still in development, we're not yet accepting external contributions. We will however be open to contributions in the future.
