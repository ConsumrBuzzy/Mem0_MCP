# Mem0 MCP Server

An open-source Memory Control Protocol (MCP) server powered by [mem0](https://github.com/mem0ai/mem0), designed to provide a robust, extensible memory layer for Windsurf and other applications.

## Project Overview

This project aims to implement an MCP server using the mem0 library as the backend memory engine. The goal is to enable Windsurf and other clients to interact with a flexible, high-performance memory layer via standard MCP interfaces.

## About Model Context Protocol (MCP)

This project implements the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), an open standard for memory and context management in AI systems. MCP defines how clients and servers communicate to store, retrieve, and manage contextual information for large language models and related applications.

By supporting MCP, this server enables seamless interoperability between memory backends (like mem0) and clients (such as Windsurf), making it easy to build, extend, and integrate memory solutions across the AI ecosystem.

Learn more about MCP at the [official introduction](https://modelcontextprotocol.io/introduction).

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

## Agent/AI Integration & Usage Example

To interact with the MCP server programmatically (for example, from an agentic AI or LLM), use the provided example Python client:

```bash
python examples/python_client.py
```

This script demonstrates how to store, retrieve, update, delete, and search for memories using the MCP API. You can adapt it for your own AI agent or use it as a reference for integrating with Cascade, Windsurf, or other systems.

See [examples/python_client.py](examples/python_client.py) for details.

*This project is in active development. Stay tuned for updates!*
