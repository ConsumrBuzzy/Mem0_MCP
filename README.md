# Mem0 MCP Server

An open-source Memory Control Protocol (MCP) server powered by [mem0](https://github.com/mem0ai/mem0), designed to provide a robust, extensible memory layer for Windsurf and other applications.

## Project Overview

This project aims to implement an MCP server using the mem0 library as the backend memory engine. The goal is to enable Windsurf and other clients to interact with a flexible, high-performance memory layer via standard MCP interfaces.

## Features
- **Open-source**: MIT-licensed for community use and contribution.
- **MCP Protocol**: Implements the Memory Control Protocol for interoperability.
- **mem0 Integration**: Leverages the mem0 library for efficient memory storage and retrieval.
- **Extensible**: Modular architecture for adding new features and storage backends.

## Getting Started

### Prerequisites
- Python 3.8+
- [mem0](https://github.com/mem0ai/mem0) library

### Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/Mem0_MCP.git
cd Mem0_MCP

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Server
```bash
python src/server.py
```

The server will start and listen for MCP requests.

## Usage
- **Health Check**: Visit `http://localhost:8000/health` to verify the server is running.
- **MCP Endpoints**: Documentation coming soon.

## Contributing
Contributions are welcome! Please open issues or pull requests.

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
MIT License. See [LICENSE](LICENSE) for details.

## Community & Support
- [mem0 GitHub](https://github.com/mem0ai/mem0)
- Windsurf documentation (coming soon)

---

*This project is in active development. Stay tuned for updates!*
