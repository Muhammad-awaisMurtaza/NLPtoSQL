from services.graph_builder import app

def chat(query: str):
  messages = app.invoke({"messages": [("user", query)]})
  for m in messages["messages"]:
    print(m.content)

  return {
    'answer': messages['messages'][-1].content,
    'sql_query': messages['messages'][-3].content
  }
