# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.contrib.auth.decorators import user_passes_test

# def authenticated_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login_1'):
    
#     actual_decorator = user_passes_test(
#         lambda u: u.is_authenticated,
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator