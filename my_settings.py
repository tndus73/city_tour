DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'citytourdata',  #mysql
        'USER': 'admin', #root
        'PASSWORD': 'citytour', #사용자의 비밀번호
        'HOST': '', #공백으로 냅두면 default localhost
        'PORT': '3306' #공백으로 냅두면 default 3306
    }
}
SECRET_KEY = 'django-insecure-8dit_*w58t+e!n)s-d%6*)k5^vw3v-oxe@ru-zkn!vdhyx4(*d'