
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse,resolve
from Butta.views import *

# Create your tests here.

class Testurls(TestCase):
    def test_register_url_is_resolved(self):
        url=reverse("register")
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)
    
    def test_url_login(self):
        url=reverse("login")
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_user)
        
class Testviews(TestCase):
    def test_register_views(self):
        client=Client()
        url=reverse("register")
        response=client.post(url,{'username':'test','email':   })
        self.assertEquas(response.status_code,200)
        self.assertRedirects(response,"")

