import httpx
from mcp.server.fastmcp import FastMCP
import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
GROQ_BASE_URL=os.getenv("GROQ_BASE_URL")

MODEL_NAME="meta-llama/llama-4-scout-17b-16e-instruct" 
mcp=FastMCP("inventory")

@mcp.tool()
async def get_query(input:str):

    """
    A conversational IT inventory system that lets users ask who has which laptop, mouse, or headphone.
    It uses an LLM to generate SQL queries, runs them on a local MySQL database with employees and inventory tables, and returns clear natural language answers.
    Useful for quickly tracking who is assigned to which device without writing SQL manually.
    Input: string
    Output: string
"""
    prompt = f"""   
You are an expert SQL generator.

Generate a **valid MySQL query** for the following user input: "{input}"

Use the database named **it** with these tables and schema:
- employees(empid, empname, laptopid, mouseid, headphoneid)
- inventory(id, accessory_name)

**Relationships:**
- employees.laptopid, employees.mouseid, employees.headphoneid are FOREIGN KEYS referencing inventory.id.

Return ONLY the SQL query.
Do not return any explanation, code block, or extra characters — only the SQL query string without any ``` only query as words.
"""


    headers={
        "Authorization":f"Bearer {GROQ_API_KEY}",
        "Content-Type":"application/json"
    }
    payload={
        "model":MODEL_NAME,
        "messages":[
            {"role":"user","content":prompt}
        ],
        "temperature":0.7,
        # "max_tokens":
    }
    try:
        async with httpx.AsyncClient() as client:
            res=await client.post(f"{GROQ_BASE_URL}/chat/completions",headers=headers,json=payload)
            res.raise_for_status()
            data=res.json()
            response= data["choices"][0]["message"]["content"]
            raw_query = response.strip()
            if raw_query.startswith("```sql"):  
                raw_query = raw_query.replace("```sql", "").replace("```", "").strip()
            dbdata=await query_database(raw_query,input)
            return dbdata

    except httpx.HTTPStatusError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"  




import pymysql
# @mcp.tool()
async def query_database(sql_query: str,question:str) -> dict:
    """
    MCP Tool: Runs LLM-generated SQL on local MySQL
    Input: plain string SQL query
    Output: { "columns": [...], "rows": [[...], [...]] }
    """

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Sharak@2004",
        database="it"
    )

    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()
    data={"columns":columns,"rows":rows}
    reponse=await getresponse(data,question)
    return reponse






# @mcp.tool()
async def getresponse(dbdata:dict,question:str):
    prompt = f"""
You are a helpful IT inventory assistant.

You must answer the user's question based ONLY on the given database result.

Question: {question}

Database Result: {dbdata}

The database result is a Python dictionary with:
- 'columns': the column names
- 'rows': the rows returned

Rewrite this data as a clear natural language answer to the question.

Only return the answer — do not repeat the raw data or add any extra notes.
"""

    headers={
        "Authorization":f"Bearer {GROQ_API_KEY}",
        "Content-Type":"application/json"
    }
    payload={
        "model":MODEL_NAME,
        "messages":[
            {"role":"user","content":prompt}
        ],
        "temperature":0.7,
    }
    try:
        async with httpx.AsyncClient() as client:
            res=await client.post(f"{GROQ_BASE_URL}/chat/completions",headers=headers,json=payload)
            res.raise_for_status()
            data=res.json()
            return data["choices"][0]["message"]["content"]
    except httpx.HTTPStatusError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"




if __name__ == "__main__":
    mcp.run()   