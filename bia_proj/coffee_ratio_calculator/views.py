from django.shortcuts import render, redirect

def calculator(request):
    if request.method == "GET":
        return render(request, "calculator.html")

def save_calculation(request):
    if request.method == "POST":
        request.session['ratio'] = request.POST['input-ratio']
        request.session['input_amount'] = request.POST['input-amount']
        request.session['result_amount'] = request.POST['result-amount']
        request.session['w_or_c'] = request.POST.get('w_or_c')

        request.session['skip_to_create'] = True

        if request.user.is_authenticated:
            return redirect("new_recipe")
        else:
            return redirect("login")
