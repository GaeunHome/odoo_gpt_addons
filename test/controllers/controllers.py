# -*- coding: utf-8 -*-
from odoo import http
import requests
import json

# class OdooPackageAddon(http.Controller):
#     @http.route('/odoo_package_addon/odoo_package_addon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_package_addon/odoo_package_addon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_package_addon.listing', {
#             'root': '/odoo_package_addon/odoo_package_addon',
#             'objects': http.request.env['odoo_package_addon.odoo_package_addon'].search([]),
#         })

#     @http.route('/odoo_package_addon/odoo_package_addon/objects/<model("odoo_package_addon.odoo_package_addon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_package_addon.object', {
#             'object': obj
#         })

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
