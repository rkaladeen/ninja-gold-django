from django.shortcuts import render, redirect
import random, datetime

# Create your views here.
def index(request):
  request.session['gold'] = 0
  request.session['location'] = ""
  request.session['message'] = []
  return render(request, "appone/index.html")

def home(request):
  return render(request, "appone/index.html")

def process_money(request):
  request.session['location'] = request.POST['select']
  return redirect("/process")

def process(request):
  selection = request.session['location']

  if selection == 'farm':
    ran = random.randrange(10, 20)
  elif selection == 'cave':
    ran = random.randrange(5, 10)
  elif selection == 'house':
    ran = random.randrange(2, 5)
  elif selection == 'casino':
    ran = random.randrange(-50, 50)

  # Calculating Gold Total
  request.session['gold'] += ran
  
  # Time Stamp Code Block
  timestamp = datetime.datetime.now()
  timestamp = timestamp.strftime("%D %I:%M:%S %p")
  
  if ran > 0:
    request.session['message'].append(f"<p class='text-success'>Earned {ran} golds from the {selection}! ({timestamp})</p>")
  elif ran <= 0:
    if request.session['gold'] > 0:
      request.session['message'].append(f"<p class='text-danger'>Entered a {selection} and lost {ran} golds... Ouch. ({timestamp})</p>")
    elif request.session['gold'] <= 0:
      request.session['message'].append(f"<p class='text-danger'>Entered a {selection} and you where kicked about because you have no gold. ({timestamp})</p>")

  # Win/Lose Cases
  if request.session['gold'] >= 500 and len(session['message']) <= 15:
    return redirect('/')
  elif len(request.session['message']) > 15:
    return redirect('/')
    
  return redirect('/refresh') 
