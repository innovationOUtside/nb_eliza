# nb_eliza
Simple eliza chatbot for use in Jupyter notebooks.

Eliza code reused from [`dhconnelly/paip-python`](https://github.com/dhconnelly/paip-python)
 ([code explication](https://dhconnelly.com/paip-python/docs/paip/eliza.html)).
 
 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/innovationOUtside/nb_eliza/master)


## Installation

Install via:

`pip install --upgrade git+https://github.com/https://github.com/innovationOUtside/nb_eliza.git`


## Usage


```python
from eliza import eliza

eliza.hello_doctor()
```

If you want to hear Eliza speak the responses aloud to you, start the programme by passing in the parameter aloud=True in the following way:

`eliza.hello_doctor(aloud=True)`

