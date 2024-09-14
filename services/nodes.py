from typing import Annotated
from typing_extensions import TypedDict
from schema import db_schema_details
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.messages import ToolMessage, AIMessage
from langgraph.graph.message import AnyMessage, add_messages
from .tools import list_tables_tool, model_get_schema, get_schema_tool, create_tool_node, llm, db_query_tool

class State(TypedDict):
  messages: Annotated[list[AnyMessage], add_messages]

def query_rewrite(state: State):
  print("***** Query ReWrite Node *****")
  print("\n")
  print(state['messages'][-1])
  print("\n")

  rewrite_prompt = f"""
    Rewrite the given user input in more understandle format also remove any gramatical and other mistakes
    Updated text should be exctly same sementicaly.
    Only return equivilent text no extra words.

    User Input: {state['messages'][0].content} 
  """

  result = llm.invoke(rewrite_prompt).content

  print("\n")
  print(result)
  print("\n")
  print("***** END Query ReWrite Node *****")
  print("\n")

  state['messages'][0].content = result
  return state

def first_tool_call(state: State):
  print("***** First Tool Call Node *****")
  print("\n")
  print(state['messages'][-1])
  print("\n")
  print("***** END First Tool Call Node *****")
  print("\n")

  return {
    "messages": [
        AIMessage(
          content="",
          tool_calls=[
            {
              "name": "sql_db_list_tables",
              "args": {},
              "id": "tool_abcd123",
            }
          ],
        )
    ]
  }

list_table_node = create_tool_node([list_tables_tool])
get_schema_node = create_tool_node([get_schema_tool])

def model_schema_node(state: State):
  print("***** Model Schema Node *****")
  print("\n")
  print(state['messages'][-1])

  result = model_get_schema.invoke(state["messages"])

  print(result)
  print("\n")
  print("***** END Model Schema Node *****")
  print("\n")

  return {"messages": [result]}

def generate_query_node(state: State):
  print("***** Generate Query Node *****")
  print("\n")
  print(state['messages'][-1])

  system_message = f"""
    Imagine you are an MYSQL expert, and your task is to generate syntactically correct query
    on the basis of given input, In response just return the query no extra text.

    Here is my DB Structure, tables and columns details:
    {db_schema_details}

    NOTE: While generating query DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
    DO NOT include ```sql\n or \n``` in response.
  """

  query_gen_prompt = ChatPromptTemplate.from_messages(
    [("system", system_message), ("placeholder", "{messages}")]
  )
  print(query_gen_prompt)

  chain = query_gen_prompt | llm
  result = chain.invoke(state)

  print(result)
  print("\n")
  print("***** END Generate Query Node *****")
  print("\n")

  return {'messages': [result]}

def execute_query_node(state: State):
  print("***** Execute Query Node *****")
  print("\n")
  print(state['messages'][-1])

  result = db_query_tool(state['messages'][-1].content)

  print("\n")
  print(result)
  print("\n")
  print("***** END Execute Query Node *****")
  print("\n")

  return {'messages': [result]}

def finalize_answer(state: State):
  print("***** Finalize Answer Node *****")
  print("\n")
  print(state['messages'][-1])

  system_message = """
    You will be provided a query result and user input, Your job is to return final answer to 
    user in a more human understandable format.

    Remember: Don't give any extra info other than user query.
  """

  query_final_prompt = ChatPromptTemplate.from_messages(
    [("system", system_message), ("placeholder", "{messages}")]
  )
  print(query_final_prompt)

  chain = query_final_prompt | llm
  result = chain.invoke(state)

  print("\n")
  print(result)
  print("\n")
  print("***** END Finalize Answer Node *****")
  print("\n")

  return {'messages': [result]}
