
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': '',
       'USER': '',
       'PASSWORD': '',
       'HOST': '',
       'PORT': '',
   },
   'mysql-inno-init': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': '',
       'USER': '',
       'PASSWORD': '',
       'HOST': '',
       'PORT': '',
       'OPTIONS': {
           'init_command': 'SET storage_engine=INNODB',
       }
   },
}