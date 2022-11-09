from django.urls import path
from aimfit_app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login_view',views.loginview,name='login_view'),


################################ ADMIN ######################################################

    path('trainer_register',views.trainer_register,name='trainer_register'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('trainer_view',views.trainer_view,name='trainer_view'),
    path('trainer_delete/<int:id>',views.trainer_delete,name='trainer_delete'),
    path('physician_register',views.physician_register,name='physician_register'),
    path('physician_view',views.physician_view,name='physician_view'),
    path('physician_delete/<int:id>',views.physician_delete,name='physician_delete'),
    path('add_equipments',views.add_equipments,name='add_equipments'),
    path('equipments_view',views.equipments_view,name='equipments_view'),
    path('equipments_delete/<int:id>',views.equipments_delete,name='equipments_delete'),
    path('add_batch',views.add_batch,name='add_batch'),
    path('batch_view',views.batch_view,name='batch_view'),
    path('batch_delete/<int:id>',views.batch_delete,name='batch_delete'),
    path('batch_update/<int:id>',views.batch_update,name='batch_update'),
    path('replyadmin/<int:id>', views.replyadmin, name='replyadmin'),
    path('complaint_admview', views.complaint_admview, name='complaint_admview'),
    path('customer_view', views.customer_view, name='customer_view'),
    path('customer_del/<int:id>',views.customer_del,name='customer_del'),
    path('add_attendance', views.add_attendance, name='add_attendance'),
    path('mark_attendance/<int:id>', views.mark_attendance, name='mark_attendance'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
    path('day_attendance/<date>', views.day_attendance, name='day_attendance'),
    path('add_notification',views.add_notification,name='add_notification'),
    path('view_notification',views.view_notification,name='view_notification'),
    path('notifi_update/<int:id>',views.notifi_update,name='notifi_update'),
    path('notification_delete/<int:id>',views.notification_delete,name='notification_delete'),
    path('add_payment',views.add_payment,name='add_payment'),
    path('payment_view',views.payment_view,name='payment_view'),

################################ USER ######################################################

    path('user_home',views.user_home,name='user_home'),
    path('usertrainer_view',views.usertrainer_view,name='usertrainer_view'),
    path('userphysician_view',views.userphysician_view,name='userphysician_view'),
    path('userequipments_view',views.userequipments_view,name='userequipments_view'),
    path('customer_register',views.customer_register,name='customer_register'),
    path('add_complaint',views.add_complaint,name='add_complaint'),
    path('complaint_view', views.complaint_view, name='complaint_view'),
    path('userdiet_view', views.userdiet_view, name='userdiet_view'),
    path('customer_viewnoti',views.customer_viewnoti,name='customer_viewnoti'),
    path('user_payview',views.user_payview,name='user_payview'),
    path('add_card/<int:id>',views.add_card,name='add_card'),
    path('cardpay_view',views.cardpay_view,name='cardpay_view'),


    ################################ TRAINER ######################################################

    path('trainer_home',views.trainer_home,name='trainer_home'),
    path('view_healthc',views.view_healthc,name='view_healthc'),
    path('add_healthc',views.add_healthc,name='add_healthc'),
    path('update_healthc/<int:id>',views.update_healthc,name='update_healthc'),
    path('diet_add',views.diet_add,name='diet_add'),
    path('diet_view',views.diet_view,name='diet_view'),
    path('trainercust_view',views.trainercust_view,name='trainercust_view'),
    path('profile_view',views.profile_view,name='profile_view'),
    path('profile_update/<int:id>',views.profile_update,name='profile_update')



################################ ADMIN ######################################################





]