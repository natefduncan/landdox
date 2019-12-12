# Landdox
Basic wrapper of Landdox API in Python.

## API Documentation
https://api.landdox.com/documentation#section/Welcome-to-Landdox-API

## Usage
```pip install landdox```

```python
from landdox import Client

ld = Client(CLIENT_ID, CLIENT_SECRET) #Get this from LD website. 
```

## Endpoints

```python
ld.contacts().list()
ld.wells().list()
ld.leases().list()
ld.tracts().list()
ld.units().list()
ld.custom(name="custom_form_name").list()
```





