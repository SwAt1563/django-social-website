from django.contrib.auth.models import User

# if the user when make login
# enter email instead of his username
# in the username field
# then we make custom validation depend on email rather
# on username if he didn't enter the username
# so the system will check the username=form.username
# if not exist then will check email=form.usernmae
class EmailAuthBackend(object):

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None