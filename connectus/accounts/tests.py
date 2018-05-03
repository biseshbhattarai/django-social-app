from django.test import TestCase
from posts.models import Post
from django.contrib.auth.models import User
from django.test import Client
from accounts.models import Profile, Friends


class requestTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_data(self):
        response = self.client.post(
            '/login/', {'username': 'Bisesh bhattarai', 'password': 'Hello123'})
        self.assertTrue(response.status_code, 200)


class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()
     

    def test_register(self):
        response = self.client.post(
            '/register/', {"username": "Rahul", "email": "rahul@gmail.com", "password": "hello123"})
        self.assertTrue(response.status_code, 200)

class All_test_related_to_profileTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username="Surya")

    def test_update(self):
        response = self.client.get('/update/')
        self.assertTrue(response.status_code == 200)
    
    def test_update_post(self):
        response = self.client.post('/update/', {
            'education':'Bachelor',
            'status': 'Hello there i am watching you people',
            'profile_image': 'abc.jpeg',
            'cover_image':'',
            'user':User.objects.first()
        })
        self.assertTrue(response.status_code, 200)

    def test_logout(self):
        response = self.client.post('/logout/')
        self.assertTrue(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)

    def test_profile_view(self):
        response = self.client.get('/users/')
        self.assertTrue(response.status_code, 200)

    def test_profile_view(self, pk=None):
       # User.objects.get(pk=pk)
        response = self.client.get('/profile/<int:pk>')
        self.assertTrue(response.status_code, 200)   

    def test_add_url(self):
        response = self.client.post('/connect/add/<int:11>')
        self.assertTrue(response.status_code, 200)      

    
    def test_lose_url(self):
        response = self.client.post('/connect/subtract/<int:11>')
        self.assertTrue(response.status_code, 200)  


class PostTest(TestCase):

    def setUp(self):
        User.objects.create(username="Bisesh")

    def test_post(self):
        posts_object = Post.objects.create(
            user=User.objects.first(),
            status="hellekejururj"
        )

        self.assertFalse(posts_object.status == "hfhfhhfhfhfh")


class ProfileTest(TestCase):
    def setUp(self):
        User.objects.create(username="Bisesh")

    def test_profile(self):
        profile = Profile.objects.first()
        self.assertTrue(profile.user.username == "Bisesh")


class FriendTest(TestCase):
    def setUp(self):
        u1_obj = User.objects.create(username="Anuza")
 
        User.objects.create(username="Hima")

    def test_add_friend(self):
        u1 = User.objects.first()
        u2 = User.objects.last()
        Friends.make_friend(u1, u2)
        friends_objects = Friends.objects.all()
        self.assertTrue(len(friends_objects) == 1)
        Friends.lose_friend(u1, u2)
        friends_objects = Friends.objects.all()
        self.assertTrue(len(friends_objects) == 1)


# class LoseFriend(TestCase):
#     def setUp(self):
#         u1 = User.objects.create(username="Anuza")
#         u2 = User.objects.create(username="Hima")
#         Friends.make_friend(u1, u2)
        

#     def test_lose_friend(self):
#         user_first = User.objects.first()
#         user_second = User.objects.last()
#         Friends.lose_friend(user_first, user_second)
#         friends_objects = Friends.objects.all()
#         self.assertTrue(len(friends_objects) == 0)

    


