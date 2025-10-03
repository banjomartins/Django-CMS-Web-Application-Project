from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import UserInfo, Product
from .forms import UserInfoForm
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied

# Create your views here.

# Public pages
def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, 'contact.html')

# Authentication
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

# User info form
@login_required
def user_form(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            messages.success(request, "Your information was saved successfully!")
            return redirect("user_list")
    else:
        form = UserInfoForm()
    return render(request, "user_form.html", {"form": form})

# User list
@login_required
def user_list(request):
    users = UserInfo.objects.all()
    return render(request, "user_list.html", {"users": users})

@login_required
def user_update(request, pk):
    user_info = get_object_or_404(UserInfo, pk=pk)

    # ✅ Only the owner OR a superuser may edit
    if request.user != user_info.user and not request.user.is_superuser:
        raise PermissionDenied  # returns HTTP 403

    if request.method == "POST":
        form = UserInfoForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            messages.success(request, "User information updated successfully.")
            return redirect("user_list")  # or redirect to 'user_form' or a detail page
    else:
        form = UserInfoForm(instance=user_info)

    return render(request, "user_form.html", {"form": form})
    # user_info = get_object_or_404(UserInfo, pk=pk)
    # if request.method == "POST":
    #     form = UserInfoForm(request.POST, instance=user_info)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("user_list")
    # else:
    #     form = UserInfoForm(instance=user_info)
    # return render(request, "user_form.html", {"form": form})

@login_required
def user_delete(request, pk):
    # Only superusers (admin) can delete
    if not request.user.is_superuser:
        raise PermissionDenied  # returns 403

    obj = get_object_or_404(UserInfo, pk=pk)

    if request.method == "POST":
        messages.success(request, f"Deleted user info for {obj.user.username}.")
        obj.delete()
        return redirect("user_list")

    # Show a small confirmation screen to avoid accidental deletes
    return render(request, "confirm_delete.html", {"obj": obj})
    # user_info = get_object_or_404(UserInfo, pk=pk)
    # user_info.delete()
    # messages.success(request, f"User '{user_info.user.username}' was deleted.")
    # return redirect("user_list")

# Products
@login_required
def product_list(request):
    products = Product.objects.filter(is_available=True)
    return render(request, "product_list.html", {"products": products})

