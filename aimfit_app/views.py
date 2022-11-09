import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from aimfit_app.models import Trainer, Login, Physician, Equipments, Batch, Complaint, Customer, DietPlan, Attendance, \
    HealthCondition, Notification, Payment

# Create your views here.
from aimfit_app.forms import LoginForm, TrainerForm, PhysicianForm, EquipmentsForm, CustomerForm, BatchForm, \
    ComplaintForm, DietForm, AttendanceForm, HealthForm, NotificationForm, PaymentForm


def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_trainer:
                return redirect('trainer_home')
            elif user.is_physician:
                return redirect('physician_home')
            elif user.is_user:
                return redirect('student_home')
            elif user.is_customer:
                return redirect('user_home')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'login.html')


#############ADMINTEMP##########################
@login_required(login_url='login_view')
def admin_home(request):
    return render(request, 'admintemp/admin_home.html')


def trainer_register(request):
    login_form = LoginForm()
    trainer_form = TrainerForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        trainer_form = TrainerForm(request.POST, request.FILES)
        if login_form.is_valid() and trainer_form.is_valid():
            user = login_form.save(commit=False)
            user.is_trainer = True
            user.save()
            trainer = trainer_form.save(commit=False)
            trainer.user = user
            trainer.save()
            messages.info(request, 'Trainer Registered Successful')
            return redirect('trainer_view')
    return render(request, 'admintemp/trainer_register.html', {'login_form': login_form, 'trainer_form': trainer_form})


def trainer_view(request):
    register = Trainer.objects.all()
    return render(request, 'admintemp/trainer_view.html ', {'register': register})


def trainer_delete(request, id):
    data1 = Trainer.objects.get(id=id)
    data = Login.objects.get(trainer=data1)
    if request.method == "POST":
        data.delete()
        return redirect('trainer_view')
    else:
        return redirect('trainer_view')


def physician_register(request):
    login_form = LoginForm()
    physician_form = PhysicianForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        physician_form = PhysicianForm(request.POST, request.FILES)
        if login_form.is_valid() and physician_form.is_valid():
            user = login_form.save(commit=False)
            user.is_physician = True
            user.save()
            physician = physician_form.save(commit=False)
            physician.user = user
            physician.save()
            messages.info(request, 'Registration Successful')
            return redirect('physician_view')
    return render(request, 'admintemp/physician_register.html',
                  {'login_form': login_form, 'physician_form': physician_form})


def physician_view(request):
    physician = Physician.objects.all()
    return render(request, 'admintemp/phy_view.html', {'physician': physician})


def physician_delete(request, id):
    data1 = Physician.objects.get(id=id)
    data = Login.objects.get(physician=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('physician_view')
    else:
        return redirect('physician_view')


def add_equipments(request):
    equipment_form = EquipmentsForm()
    if request.method == 'POST':
        equipment_form = EquipmentsForm(request.POST, request.FILES)
        if equipment_form.is_valid:
            equipment = equipment_form.save()
            equipment.save()
            messages.info(request, 'Equipment Added Successful')
            return redirect('equipments_view')
    return render(request, 'admintemp/add_equipments.html', {'equipment_form': equipment_form})


def equipments_view(request):
    equipments = Equipments.objects.all()
    return render(request, 'admintemp/equipments_view.html', {'equipments': equipments})


def equipments_delete(request, id):
    data = Equipments.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('equipments_view')
    else:
        return redirect('equipments_view')


def add_batch(request):
    batch_form = BatchForm()
    if request.method == 'POST':
        batch_form = BatchForm(request.POST)
        # print(batch_form)
        if batch_form.is_valid():
            batch_form.save()
            messages.info(request, 'Batch Added Successful')
            return redirect('batch_view')
    return render(request, 'admintemp/batch_add.html', {'batch_form': batch_form})


def batch_view(request):
    batch = Batch.objects.all()
    return render(request, 'admintemp/batch_view.html', {'batch': batch})


def batch_delete(request, id):
    data = Batch.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('batch_view')
    else:
        return redirect('batch_view')


def batch_update(request, id):
    data = Batch.objects.get(id=id)
    if request.method == 'POST':
        form = BatchForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, 'Batch update Succesfully')
            return redirect('batch_view')
    else:
        form = BatchForm(instance=data)
    return render(request, 'admintemp/batch_update.html', {'form': form})


def replyadmin(request, id):
    rid = Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        rid.reply = r
        rid.save()
        messages.info(request, 'Reply added Successfuly')
        return redirect('complaint_admview')
    return render(request, 'admintemp/admin_reply.html', {'rid': rid})


def complaint_admview(request):
    complaint2 = Complaint.objects.all()
    return render(request, 'admintemp/cmp_admview.html', {'complaint2': complaint2})


def customer_view(request):
    cust = Customer.objects.all()
    return render(request, 'admintemp/customer_view.html', {'cust': cust})


def customer_del(request, id):
    cust = Customer.objects.get(id=id)
    if request.method == 'POST':
        cust.delete()
        return redirect('customer_view')
    else:
        return redirect('customer_view')


def add_attendance(request):
    customer = Customer.objects.all()
    return render(request, 'admintemp/add_attendance.html', {'customer': customer})


now = datetime.datetime.now()


def mark_attendance(request, id):
    user = Customer.objects.get(id=id)
    add = Attendance.objects.filter(name=user, date=datetime.date.today())
    if add.exists():
        messages.info(request, "Today's Attendance is already Marked!")
        return redirect('add_attendance')
    else:
        if request.method == 'POST':
            attendance = request.POST.get('attendance')
            Attendance(name=user, date=datetime.date.today(), attendance=attendance, time=now.time()).save()
            messages.info(request, "Attendance added Succesfully")
            return redirect('add_attendance')
        return render(request, 'admintemp/mark_attendance.html')


def view_attendance(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'admintemp/view_attendance.html', {'attendance': attendance})


def day_attendance(request, date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendance': attendance,
        'date': date
    }
    return render(request, 'admintemp/day_attendance.html', context)

def add_notification(request):
    notification=NotificationForm()
    if request.method=='POST':
        notification=NotificationForm(request.POST)
        if notification.is_valid():
            notification.save()
            messages.info(request,'notification added successfully!')
            return redirect('view_notification')
    return render(request,'admintemp/add_noti.html',{'notification':notification})

def view_notification(request):
    notif=Notification.objects.all()
    return render(request,'admintemp/view_noti.html',{'notif':notif})

def notifi_update(request,id):
    data=Notification.objects.get(id=id)
    if request.method=='POST':
        form=NotificationForm(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            messages.info(request,'notification Updated')
            return redirect('view_notification')
    else:
        form=NotificationForm(instance=data)
    return render(request,'admintemp/noti_update.html',{'form':form})

def notification_delete(request,id):
    data=Notification.objects.get(id=id)
    if request.method=='POST':
        data.delete()
        return redirect('view_notification')
    else:
        return redirect('view_notification')



def add_payment(request):
    pay_form=PaymentForm()
    if request.method=='POST':
        pay_form=PaymentForm(request.POST)
        if pay_form.is_valid():
            pay_form.save()
            messages.info(request,'Payment has been assigned !')
            return redirect('payment_view')
    return render(request,'admintemp/add_payment.html',{'pay_form':pay_form})

def payment_view(request):
    pay=Payment.objects.all()
    return render(request,'admintemp/view_payment.html',{'pay':pay})


######################################################### USER #############################################################################################3


def user_home(request):
    return render(request, 'usertemp/user_home.html')


def usertrainer_view(request):
    register = Trainer.objects.all()
    return render(request, 'usertemp/usertrainer_view.html ', {'register': register})


def userphysician_view(request):
    physician = Physician.objects.all()
    return render(request, 'usertemp/userphy_view.html', {'physician': physician})


def userequipments_view(request):
    equipments = Equipments.objects.all()
    return render(request, 'usertemp/userequipments_view.html', {'equipments': equipments})


def customer_register(request):
    login_form = LoginForm()
    customer_form = CustomerForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        customer_form = CustomerForm(request.POST, request.FILES)
        if login_form.is_valid() and customer_form.is_valid():
            user = login_form.save(commit=True)
            user.is_customer = True
            user.save()
            customer = customer_form.save(commit=True)
            customer.user = user
            customer.save()
            messages.info(request, 'Registration Successful')
            return redirect('login_view')
    return render(request, 'usertemp/reg.html', {'login_form': login_form, 'customer_form': customer_form})


def add_complaint(request):
    complaint_form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        complaint_form = ComplaintForm(request.POST)
        if complaint_form.is_valid():
            obj = complaint_form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Comlaint Added Successful')
            return redirect('complaint_view')
    return render(request, 'usertemp/cmp_add.html', {'complaint_form': complaint_form})


def complaint_view(request):
    complaint = Complaint.objects.filter(user=request.user)
    return render(request, 'usertemp/cmp_view.html', {'complaint': complaint})


def userdiet_view(request):
    diet = DietPlan.objects.all()
    return render(request, 'usertemp/userdiet_view.html', {'diet': diet})

def customer_viewnoti(request):
    notification=Notification.objects.all
    return render(request,'usertemp/cust_noti.html',{'notification':notification})

def user_payview(request):
    # u=request.user
    # print(u)
    payment=Payment.objects.filter(name=request.user.customer)
    # print(pay)
    return render(request,'usertemp/userpay_view.html',{'payment':payment})

def add_card(request,id):
    pay=Payment.objects.get(id=id)
    if request.method=='POST':
        c=request.POST.get('card_no')
        cn=request.POST.get('card_name')
        cvv=request.POST.get('cvv')
        pay.card_no=c
        pay.card_name=cn
        pay.cvv=cvv
        pay.save()
        messages.info(request,'Payment Done Successfully!')
        return redirect('cardpay_view')
    return render(request,'usertemp/add_card.html',{'pay':pay})



def cardpay_view(request):
    return render(request, 'usertemp/cardpay.html')


############################################################### Trainer ###################################################################################

def diet_add(request):
    diet_form = DietForm()
    if request.method == 'POST':
        diet_form = DietForm(request.POST, request.FILES)
        if diet_form.is_valid():
            diet_form.save()
            messages.info(request, 'New Diet Plan Added Succesfully!')
            return redirect('diet_view')
    return render(request, 'trainertemp/diet_add.html', {'diet_form': diet_form})


def diet_view(request):
    diet = DietPlan.objects.all()
    return render(request, 'trainertemp/diet_view.html', {'diet': diet})


def add_healthc(request):
    health_form = HealthForm()
    if request.method == 'POST':
        health_form = HealthForm(request.POST)
        if health_form.is_valid():
            health_form.save()
            messages.info(request, 'Health Condition updated')
        return redirect('view_healthc')
    return render(request, 'trainertemp/add_healthc.html', {'health_form': health_form})


def view_healthc(request):
    health = HealthCondition.objects.all()
    return render(request, 'trainertemp/healthview.html', {'health': health})


def update_healthc(request, id):
    data = HealthCondition.objects.get(id=id)
    if request.method == 'POST':
        health = HealthForm(request.POST or None, instance=data)
        if health.is_valid():
            health.save()
            messages.info(request, 'health condition updated successfully!')
            return redirect('view_healthc')
    else:
        health = HealthForm(instance=data)
    return render(request, 'trainertemp/update_healthc.html', {'health': health})


def delete_healthc(request, id):
    data = HealthCondition.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('view_healthc')
    else:
        return redirect('view_healthc')


def trainer_home(request):
    return render(request, 'trainertemp/trainer_home.html')


def trainercust_view(request):
    cust = Customer.objects.all()
    return render(request, 'trainertemp/trainercust_view.html', {'cust': cust})

def profile_view(request):
    prof=Trainer.objects.get(user=request.user)
    return render(request,'trainertemp/trainer_profview.html',{'prof':prof})

def profile_update(request,id):
    data=Trainer.objects.get(id=id)
    if request.method=='POST':
        trform=TrainerForm(request.POST,request.FILES or None,instance=data)
        if trform.is_valid():
            trform.save()
            messages.info(request,'Profile Updated Suuccessfully!')
            return redirect('profile_view')
    else:
        trform=TrainerForm(instance=data)
    return render(request,'trainertemp/prof_update.html',{'trform':trform})



