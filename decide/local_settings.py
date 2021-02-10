ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ferlopmor1db',
        'USER': 'ferlopmor1',
        'PASSWORD': 'Sergiollull23',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
BASEURL = 'http://localhost:8000'
APIS = {
    'authentication': BASEURL,
    'base': BASEURL,
    'booth': BASEURL,
    'census': BASEURL,
    'mixnet': BASEURL,
    'postproc': BASEURL,
    'store': BASEURL,
    'visualizer': BASEURL,
    'voting': BASEURL,
}




# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
