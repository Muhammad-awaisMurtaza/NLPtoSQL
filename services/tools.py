import os
from typing import Any
from database import db
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from langchain_core.messages import ToolMessage
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_core.runnables import RunnableLambda, RunnableWithFallbacks

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()
list_tables_tool = next(tool for tool in tools if tool.name == "sql_db_list_tables")
get_schema_tool = next(tool for tool in tools if tool.name == "sql_db_schema")
model_get_schema = llm.bind_tools([get_schema_tool])

@tool
def db_query_tool(query: str) -> str:
  """
  Execute a SQL query against the database and get back the result.
  If the query is not correct, an error message will be returned.
  """

  print("DB Query Tool")
  print(query)

  result = db.run_no_throw(query)

  print(result)
  print("***** END DB Query Tool *****")
  print("\n")

  if not result:
    return "Error: Query failed. Please rewrite your query and try again."
  return result

def create_tool_node(tools):
  return ToolNode(tools)
