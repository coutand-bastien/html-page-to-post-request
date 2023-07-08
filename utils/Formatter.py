import requests
from bs4 import BeautifulSoup
from termcolor import colored

from utils.Randomer import Randomer

class Formatter:
    '''
    Class to format the HTML code of a page to be injected
    '''
    def __init__(self, url_list, headers, input_type, payload, other_function: callable = None):
        self.url_list       = url_list # list of URL to be injected
        self.headers        = headers # headers of the request
        self.input_type     = input_type # type of the input to be injected
        self.payload        = payload # payload to be injected
        self.other_function = other_function # other function to be called after the injection if there is some process to do
        
        self.common_url = ""
        self.randomer = Randomer()

    def get_html(self):
        '''
        Get the HTML code of a page

        Returns:
            str: HTML code to be injected
        '''
        return requests.get(self.common_url, headers=self.headers).content


    def format_html(self, html_content, input_type, payload):
        '''
        Format the inputs to be injected. For that we need to get all the forms and all the inputs of the forms
        and then we need to format them to be injected. The injectable inputs are inject with the payload and
        the other required inputs are inject with random value (with min and max if they have). Take also the select because
        can be required too.

        Args:
            html_content (str): HTML code of the page
            input_type (str): Type of the input to be injected
            payload (str): Payload to be injected

        Returns:
            dict: Formatted forms with their inputs
        '''
        forms_formatted = {}
        forms_formatted['inputs_elt'] = {} # init the inputs of the form

        soup  = BeautifulSoup(html_content, 'html.parser')
        forms = soup.find_all('form') # get all form

        for form in forms:
            form_action = form.get('action') # get the endpoint of the form
            
            # if the form doesn't have action, we take the url
            form_action = self.common_url if not form_action else self.common_url+form_action
            
            forms_formatted['endpoint'] = form_action 
            
            injectable_inputs = soup.find_all('input', {'type': input_type}) # get all the text inputs

            # format the injectable inputs with the payload
            for input_element in injectable_inputs:
                mini, maxi = 0, 150

                if input_element.get('min'): mini = input_element['min']
                if input_element.get('max'): maxi = input_element['max']
                
                if mini <= len(payload) <= maxi:
                    forms_formatted['inputs_elt'][input_element['name']] = payload
                else:
                    forms_formatted['inputs_elt'][input_element['name']] = self.randomer.generate_random_value(input_type=input_element['type'], min_length=mini, max_length=maxi)

            other_required_input = list(set(soup.find_all('input', {'required': True})) - set(injectable_inputs)) # remove the injectable inputs

            # format the other required inputs with random value
            for input_element in other_required_input:
                mini, maxi = 0, 150

                if input_element.get('min'): mini = input_element['min']
                if input_element.get('max'): maxi = input_element['max']

                if input_element.get('min') and input_element.get('max'):
                    forms_formatted['inputs_elt'][input_element['name']] = self.randomer.generate_random_value(input_type=input_element['type'], min_length=mini, max_length=maxi)
                else:
                    forms_formatted['inputs_elt'][input_element['name']] =  self.randomer.generate_random_value(input_type=input_element['type'])
 
            # format the select with the 1st option
            select = soup.find_all('select', {'required': True})
            for select_element in select:
                forms_formatted['inputs_elt'][select_element['name']] = select_element.find('option')[1]['value']
 
            self.send_inject_payload(form_formatted=forms_formatted) # send the request to the inject endpoint

        return forms_formatted
    
    def send_inject_payload(self, form_formatted):
        '''
        Format the request to be sent to the inject endpoint and perform other
        function if it's not None.

        Args:
            form_formatted (dict): Formatted forms with their inputs
        '''
        print(colored(f'[i]Test : {form_formatted["endpoint"]}', 'yellow'))
        response = requests.post(form_formatted['endpoint'], params=form_formatted['inputs_elt'], headers=self.headers)
        
        # if the other function is not None, call it
        if self.other_function: 
            self.other_function(response)

    def process(self):
        '''
        Process the injection
        '''
        for url in self.url_list:
            self.common_url = url

            html_content    = self.get_html()
            forms_formatted = self.format_html(html_content=html_content, input_type=self.input_type, payload=self.payload)
            print(forms_formatted)