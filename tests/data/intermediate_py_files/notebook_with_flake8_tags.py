from IPython import get_ipython


# In[1]


import not_a_package  # noqa: F401
{"1":1}  # noqa: F401


# In[2]


{"2":1}  # noqa: E231
{"2":2}


# In[3]


{"3":1}  # noqa: E231
{"3":2}  # noqa: E231


# In[4]


# flake8-noqa-cell-F401  # noqa: F401
import not_a_package  # noqa: F401
{"4":1}  # noqa: F401


# In[5]


# flake8-noqa-line-2-E231
{"5":1}  # noqa: E231
{"5":2}


# In[6]


# flake8-noqa-cell-E231  # noqa: E231
{"6":1}  # noqa: E231
{"6":2}  # noqa: E231


# In[7]


get_ipython().system('flake8_nb notebook_with_flake8_tags.ipynb')
