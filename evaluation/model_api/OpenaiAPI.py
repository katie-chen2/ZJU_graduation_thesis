from openai import OpenAI
import time
import json
import sys
import requests
sys.path.append('./model_api')
from BaseAPI import BaseAPI

class OpenaiAPI(BaseAPI):
    def __init__(self, model_name, generation_config={}):
        super().__init__(generation_config)
        self.model_name = model_name
        self.base_url="your_url"
        self.api_key="your_key"
        
        self.sys_prompt = self.without_strict_jsonformat_sys_prompt
        self.sys_prompt = self.revised_prompt
        # self.sys_prompt = self.sys_prompt_with_failure_modes_without_strict_jsonformat
        # self.sys_prompt = self.sys_prompt_with_simple_failure_modes_without_strict_jsonformat

    def response(self, messages): #, tools):
        #if not tools: tools = None
        for _ in range(10):
            try:
                '''
                completion = self.client.chat.completions.create(
                    model=self.model_name,
                    #tools=tools,
                    messages=messages,
                    **self.generation_config
                )
                '''
                payload = json.dumps({
                    "model": self.model_name,
                    "messages": messages
                })
                url = self.base_url + "/v1/chat/completions"
                headers = {
                    'Accept': 'application/json',
                    'Authorization': f'Bearer {self.api_key}',
                    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
                    'Content-Type': 'application/json'
                }
                response = requests.request("POST", url, headers=headers, data=payload)
                data = response.json()
                print(f'completion: {data}')
                if data is None or data['choices'] is None:
                    continue
                return data
            except Exception as e:
                print(e)
                time.sleep(1)

    def generate_response(self, messages): #, tools):
        print(messages)
        completion = self.response(messages) #, tools)
        # print(f'messages: {messages}\ncompletion: {completion}')

        if completion is None: return None

        ## tool call part
        '''
        print(f'completion: {completion}')
        if completion.choices[0].message.tool_calls is not None:
            tool_call = completion.choices[0].message.tool_calls[0]
            tool_call_id = tool_call.id
            tool_name = tool_call.function.name
            if tool_call.function.arguments:
                arguments = json.loads(tool_call.function.arguments)
            else:
                arguments = {}
            return {'type': 'tool', 'tool_call_id': tool_call_id, 'tool_name': tool_name, 'arguments': arguments}
        '''
        ## normal content part
        #else:
        content = completion['choices'][0]['message']['content']
        print(content)
        return {'type': 'content', 'content': content}
