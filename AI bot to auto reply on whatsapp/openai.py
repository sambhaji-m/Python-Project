from openai import OpenAI
 
# pip install openai 
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
 
  first copy your whatsapp chat contect from start to end (only visible in one window without scroll) 

'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named sam who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like sam"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)