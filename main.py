# Define imports needed
import alpha_config
# Define a variable with the API key. Eventually, use a config file to get the
# key or a system variable.
api_key = ''
format_='json'

microf = Company(api_key, 'MSFT', format_)
microf.PrintData()
