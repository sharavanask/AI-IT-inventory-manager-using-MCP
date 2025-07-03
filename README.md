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


## Example input 
what are the  diff types of mouse models available in the inventory

## Workflow

1.INput natural language query
2.get database and schemea info
3.generate query to fetch the data 
4.exevute the query
5.return the output data from your database 

## Output
Mice:

Apple Magic Mouse, Apple Magic Mouse2, Apple Magic Mouse3
Apple Pro Mouse, Apple Wireless Mouse
Corsair Dark Core RGB Pro, Corsair Harpoon RGB Wireless, Corsair Katar Pro XT, Corsair M65 RGB Elite, Corsair Sabre RGB Pro
Dell Alienware AW610M, Dell Laser Mouse, Dell Mobile Wireless Mouse, Dell MS116 Wired Mouse, Dell Premier Wireless Mouse, Dell WM126 Wireless Mouse
HP Comfort Grip Wireless Mouse, HP Dual Mode Mouse, HP Spectre Rechargeable Mouse, HP X3000 Wireless Mouse, HP X500 Wired Mouse, HP Z3700 Wireless Mouse
Lenovo300 Wireless Compact Mouse, Lenovo Legion M200, Lenovo N700 Wireless Touch Mouse, Lenovo ThinkPad Bluetooth Laser Mouse, Lenovo Yoga Mouse
Logitech G305 Lightspeed, Logitech G502 Hero, Logitech M185, Logitech M590 Multi-Device Silent, Logitech M720 Triathlon, Logitech MX Master3
Microsoft Arc Mouse, Microsoft Bluetooth Mouse, Microsoft Classic IntelliMouse, Microsoft Mobile Mouse1850, Microsoft Modern Mobile Mouse, Microsoft Sculpt Ergonomic Mouse
Razer Atheris, Razer Basilisk X Hyperspeed, Razer DeathAdder V2, Razer Naga Trinity, Razer Orochi V2, Razer Viper Mini
SteelSeries Aerox3, SteelSeries Prime Wireless, SteelSeries Rival3, SteelSeries Rival600, SteelSeries Sensei Ten
The system also returned all laptops and headphones in the inventory as part of the comprehensive list.
## License
MIT License. Feel free to use and adapt.

