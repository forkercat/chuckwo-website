from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.template import loader, Context
from django.http import HttpResponse
from petvs.models import Pet, Statistics
from random import Random

# random_str
def random_str(randomlength): 
    str = '' 
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789' 
    length = len(chars) - 1 
    random = Random() 
    for i in range(randomlength): 
        str+=chars[random.randint(0, length)] 
    return str


# startVS
def startVS(request):
    s = Statistics.objects.get()
    pet1_post = request.POST.get('pet1')
    pet2_post = request.POST.get('pet2')
    newKey = '';
    if pet1_post != None:
        newKey = pet1_post.split(',,,')[2]
    elif pet2_post != None:
        newKey = pet2_post.split(',,,')[2]

    # print 'new key -----------' + newKey
    # print 'seesion key -------' + request.session['post_key']

    if request.method == "POST" and newKey == request.session['post_key']:
        # POST
        if pet1_post != None:
            # click pet1
            # print 'click 1 - ' + pet1_post
            # restore last time data
            last_pets_name = pet1_post.split(',,,')
            last_pet1 = Pet.objects.get(name=last_pets_name[0])
            last_pet2 = Pet.objects.get(name=last_pets_name[1])
            # hot++
            last_pet1.hot += 1
            last_pet1.save()
            s.clicks += 1;
            print "Clicks:" + str(s.clicks)
            s.save()
            # generate a new pet for 2
            pet1 = last_pet1
            pets = Pet.objects.order_by('?')[:1]
            pet2 = pets[0]
            while pet1 == pet2 or pet2 == last_pet2:
                pets = Pet.objects.order_by('?')[:1]
                pet2 = pets[0]
        elif pet2_post != None:
            # click pet2
            # print 'click 2 - ' + pet2_post
            # restore last time data
            last_pets_name = pet2_post.split(',,,')
            last_pet1 = Pet.objects.get(name=last_pets_name[0])
            last_pet2 = Pet.objects.get(name=last_pets_name[1])
            # hot++
            last_pet2.hot += 1
            last_pet2.save()
            s.clicks += 1;
            print "Clicks:" + str(s.clicks)
            s.save()
            # generate a new pet for 1
            pet2 = last_pet2
            pets = Pet.objects.order_by('?')[:1]
            pet1 = pets[0]
            while pet1 == pet2 or pet1 == last_pet1:
                pets = Pet.objects.order_by('?')[:1]
                pet1 = pets[0]
    else:
        # FIRST TIME
        s.visits += 1;
        print 'Visits: ' + str(s.visits)
        s.save()

        pets = Pet.objects.order_by('?')[:2]
        pet1 = pets[0]
        pet2 = pets[1]

        while pet1 == pet2:
            pets = Pet.objects.order_by('?')[:2]
            pet1 = pets[0]
            pet2 = pets[1]

    
    print pet1, pet2
    request.session['post_key'] = random_str(10)
    cont = Context({
        'pet1': pet1,
        'pet2': pet2,
        'key': request.session['post_key']
    })

    cont.update(csrf(request))

    return render_to_response('index.html', cont)


def rank(request):
    # Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]
    top5_pets = Pet.objects.order_by('-hot')[:10]
    cont = Context({
        'pets': top5_pets,
    })
    print top5_pets
    return render_to_response('rank.html', cont)














