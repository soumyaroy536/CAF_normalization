Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import re
... 
... def normalize_company_name(company_name: str) -> str:
...     if not company_name or not company_name.strip():
...         return "Company Name Not Available"
... 
...     name = company_name.lower()
...     name = re.sub(r'\s+', ' ', name)
... 
...     if "caf" not in name:
...         return "Company Name Not Available"
... 
...     return "CAF SoftSol India Pvt Ltd."
