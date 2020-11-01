# fundamental_analisis
## Basic idea
In order to design a good architecture and to guide the development process, it is interesting to unravel the big picture idea that is behind this repo.
Instead of trying to delineate modules, functionality and such, it seems more insighful to explain the basic idea:

Idea: the software would be a tool to gather fundamental information from companies as well as information about the price and how it fluctuates. 
Once that data is gathered, it would be fed to some analysis tool (something as simple as Excel spreadsheet, so csv format should be allowed, or as complex
as Scala or Python notebooks running on Spark, so json or parquet formats are interesting) that would give guidance about investing options.

The original interest is to automatically gather some fundamental information that would allow the design and implementation of medium to long term strategies for
investment.

That being said, some basic points are clear:  
1. Software should ingest a list of variable number of tickers (company symbols used in the markets).
1. When gathering information, it uses alpha_vantage wrapper for AlphaVantage API. So it shouldn't be a wrapper on top of a wrapper.
1. It should use concurrency in same form.
1. It should allow to save the results in some format of choice.  

## TODO List
