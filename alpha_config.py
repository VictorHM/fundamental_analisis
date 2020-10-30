from alpha_vantage.alpha_vantage.fundamentaldata import FundamentalData

# Class to load data from an specific company

class Company: 
  '''Obtains finantial data of a company using AlphaVantage library for
  obtaining updated information. Depending on the funciton used, it will contain
  different information relevant for Fundamental analysis.'''

  def Initialize(self, akey, company, formato='pandas'):
    '''Initialize the object. It requires the API key to connect to AV and the
    company we want information about. Optional is the format. Default is pandas.'''
    self.key = akey
    self.company = company
    self.format = formato
  
# TODO: create a version that accepts a list of company tickers and stores the
# results in an array of 'overview's.
  def get_company_info(self)
    fs = FundamentalData(self.akey, self.format)
    self.overview = fs.get_company_overview(self.company)

# TESTING FUNCTION
  def PrintData(self):
    print('Overview or metadata:')
    print(self.overview)
