# Conversational IT Inventory MCP Server

This repository contains an MCP server that lets you query an IT inventory database in natural language. It uses Groq’s Llama 4 model to generate valid MySQL queries and converts database results into human-friendly answers.

## Features
- Natural language ➜ SQL ➜ database ➜ human answer
- Uses FastMCP for tool registration
- Connects to a local MySQL database with `employees` and `inventory` tables

## Prerequisites
- Python 3.8 or newer
- Dependencies: `httpx`, `pymysql`, `mysql-connector-python`, `python-dotenv`, `fastmcp`

## Setup Instructions
1. Install Python packages:
   ```bash
   pip install httpx pymysql mysql-connector-python python-dotenv fastmcp
   ```
2. Add a `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key
   GROQ_BASE_URL=https://api.groq.com/openai/v1
   ```
3. Ensure your local MySQL server has:
   - Database: `it`
   - Tables:
     - `employees(empid, empname, laptopid, mouseid, headphoneid)`
     - `inventory(id, accessory_name)`

## Running the Server
Run your script with:
```bash
python your_script.py
```

## License
MIT License. Feel free to use and adapt.

