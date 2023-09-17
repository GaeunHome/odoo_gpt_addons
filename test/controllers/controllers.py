# -*- coding: utf-8 -*-
from odoo import http
import requests
import json

class GPTtest(http.Controller):
    @http.route('/extraaddons/', type='http', auth='public', website=True)
    
    def complete_text(self, **kw):
        prompt = kw.get('prompt', '')
        response = requests.post(
            'https://api.openai.com/v1/completions',
            headers={
                'Authorization': 'Bearer Your API Key', 
                'Content-Type': 'application/json'
            },
            data=json.dumps({
                'model': 'text-davinci-003',
                'prompt': prompt,
                'max_tokens': 100,
                'temperature': 0,
                'top_p': 1,
                'frequency_penalty': 0,
                'presence_penalty': 0
            })
        ) 
        if response.ok:
            text = response.json()['choices'][0]['text']
            return text
        else:
            return "Error: {}".format(response.text)
