from django.shortcuts import redirect
from django.shortcuts import render
from .models import Donors
from .forms import DonorsForm
from django.contrib import messages
# Create your views here.
def donor_info(request):
    return render(request, 'donor/donor_info.html', {})

# def donor_new(request):
# 	if request.method == "POST":
# 	    form = DonorsForm(request.POST)
# 	    if form.is_valid():
# 		    post = form.save(commit=False)
# 		    post.save()
# 		    return redirect('donor_new', pk=post.pk)

# 	else:
# 		form = DonorsForm()
# 	return render(request, 'donor/donor_info.html', {'form': form})

# def item(request):
#     form = DonorsForm()
#     return render(request, 'donor/item.html', {'form': form})


def item(request):
    if request.method == "POST":
        form = DonorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor:item',)
    else:
        form = DonorsForm()
    return render(request, 'donor/item.html', {'form': form})