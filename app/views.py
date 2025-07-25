from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Std
from .form import Stdform
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail


@login_required
def home(request):
    send_mail(
    "Message!",
    "Anybody Login at your Project",
    "muhammadabuhurairah22@gmail.com",
    ["muhammadabuhurairah88@gmail.com"],
    fail_silently=False,
)
#    data = {
#     "Page": "This is our home page!",
#     "Game": ['Cricket', 'Football', 'Hockey', 'Kabaddi'],
#    'std' :[
#     {'Name': 'Abu Hurairah', 'Class': 'BSCS7A', 'Phone': '03116085400'},
#     {'Name': 'Ali', 'Class': 'BSCS7B', 'Phone': '03116085401'},
#     {'Name': 'Ahmed', 'Class': 'BSCS7C', 'Phone': '03116085402'},
#     {'Name': 'Sara', 'Class': 'BSCS7D', 'Phone': '03116085403'},
#     {'Name': 'Fatima', 'Class': 'BSCS7E', 'Phone': '03116085404'},
#     {'Name': 'Usman', 'Class': 'BSCS7F', 'Phone': '03116085405'},
#     {'Name': 'Zain', 'Class': 'BSCS7G', 'Phone': '03116085406'},
#     {'Name': 'Ayesha', 'Class': 'BSCS7H', 'Phone': '03116085407'},
#     {'Name': 'Omer', 'Class': 'BSCS7I', 'Phone': '03116085408'},
#     {'Name': 'Maryam', 'Class': 'BSCS7J', 'Phone': '03116085409'}
# ]

#         }

    # data = Std.objects.all() # for display only 3 item on page
    data = Std.objects.all().order_by('-id')[:3] # for display only 3 item on page
    
    
    
    # Corrected query   come data fom database
    return render(request, 'home.html', {'Std': data}) 
def about(request):
    data = Std.objects.all().order_by('-id')[:3]
    return  render (request,'about.html',{'Std': data})

def contact(request):
    return render(request,'contact.html')
from django.shortcuts import render, redirect
from .models import Std  # Import the model

def add(request):
    if request.method == 'POST':  # Check if form is submitted
        # Retrieve form data
        n = request.POST.get('name')
        r = request.POST.get('roll')
        a = request.POST.get('add')
        m = request.POST.get('mail')

        # Create and save the record in the database
        record = Std(name=n, roll=r, address=a, mail=m)  # Use the Std model
        record.save()  # Save the record to the database

        # Redirect to a new page or reload
        return redirect('home')  # Replace 'home' with your URL name

    return render(request, 'add.html')  # Render the form page


def validate(request):
    if request.method == 'POST':
        form = Stdform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with your URL name
    else:
        form = Stdform()
    
    content = {
        'form': form
    }
    return render(request, 'validate.html', content)



def delete(request, id):
    remove = get_object_or_404(Std, id=id)  # Provide the model 'Std' explicitly
    remove.delete()  # Call the delete method with parentheses
    return redirect('home')  # Redirect to the 'home' page


def edit(request,id):
    edit = get_object_or_404(Std, id=id)
    if request.method == 'POST':
        form = Stdform(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with your URL name
    else:
        form = Stdform(instance=edit)
    
    content = {
        'form': form
    }
    return render(request, 'editrecord.html', content)
def logout_user(request):
    logout(request)
    return redirect('home')