from django.urls import path
from  emp_app import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('user_login/',views.user_login,name='user_login'),
    path('all_emp/',views.all_emp,name='all_emp'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('remove_emp/',views.remove_emp,name='remove_emp'),
    path('filter_emp/',views.filter_emp,name='filter_emp'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('logout/',views.logout_page,name='logout_page'),
    
]
