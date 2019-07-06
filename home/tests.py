from django.test import TestCase
from . import views
# Create your tests here.

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        responce = self.client.get('/')
        self.assertEquals(responce.status_code, 200)
    def test_home_page_contains_correct_html(self):
        responce = self.client.get('/')
        self.assertContains(responce,'<h1>Homepage</h1>')
    
    def test_home_page_does_not_contain_incorect_html(self):
        responce = self.client.get('/')
        self.assertNotContains(
            responce,'Hi there! I should not be on the page.')
        
    def test_view_uses_correct_template(self):
        responce= self.client.get('/')
        self.assertTemplateUsed(responce, 'testpage.html')