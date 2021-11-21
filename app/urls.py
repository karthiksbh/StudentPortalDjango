from django.urls import path
from app import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from app.forms import User_Login, Password_Change, Password_Reset, Password_Set

urlpatterns = [

    path('', views.main_page, name="mainpage"),

    path('home/', views.home, name="homepage"),

    path('class9/', views.class9, name="class9"),

    path('class8/', views.class8, name="class8"),

    path('class10/', views.class10, name="class10"),

    path('class1112/', views.class1112, name="class1112"),

    path('vid9/', views.vid9, name="vid9"),

    path('vid10/', views.vid10, name="vid10"),

    path('vid8/', views.vid8, name="vid8"),

    path('vid1112/', views.vid1112, name="vid1112"),

    path('register/', views.RegisterUserView.as_view(), name="userregistration"),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html',
         authentication_form=User_Login), name="login"),

    path('logout/', auth_views.LogoutView.as_view(next_page='mainpage'), name='logout'),

    path('profile/', views.profile, name="profile"),

    path('enterprofile/', views. StudentPro.as_view(), name='enterprofile'),

    path('editprofile/<profile_id>', views.edit_profile, name='editprofile'),

    path('todo/', views.AddTodo.as_view(), name="todo"),

    path('delete/<todo_id>', views.delete, name="delete"),

    path('done_todo/<todo_id>', views.done_todo, name="done_todo"),

    path('notdone_todo/<todo_id>', views.notdone_todo, name="notdone_todo"),

    path('edit/<todo_id>', views.edit, name="edit"),

    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='changepassword.html',
         form_class=Password_Change, success_url='/passwordsuccess/'), name='changepassword'),

    path('pdfs/', views.pdfs, name="pdfs"),

    path('videos/', views.videos, name="videos"),

    path('passwordsuccess/', views.passsuccess, name='passwordsuccess'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=Password_Reset), name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=Password_Set), name='password_reset_confirm',),

    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]
