import math
from django.http import HttpResponse
from django.views import generic


from .models import Shelter


def index(request):
    return HttpResponse("Hello world!")


def GetNearbyShelters(request):
    if request.method == 'GET':
        results = request.GET.get('results')
    return HttpResponse("foo")


def SortShelterQueryResults(user_coordinates, results):
    distance_sorted = SortByDistance(user_coordinates, results)
    capacity_sorted = SortByCapacity(distance_sorted)
    return capacity_sorted


def SortByDistance(user_coordinates, results):
    distance_result_dict = []
    for result in results:
        geometry = result['geometry']
        coordinates = geometry['location']
        coordinates = (coordinates['lat'], coordinates['lng'])

        distance = ComputeDistance(user_coordinates, coordinates)
        distance_result_dict.append((distance, result))

    distance_result_dict.sort()
    sorted_results = list(map(lambda x: x[1], distance_result_dict))
    return sorted_results


def SortByCapacity(results):
    full_shelters = []
    shelters = Shelter.objects.all()
    for result in results:
        place_id = result['place_id']
        try:
            shelter = shelters.get(google_place_id=place_id)
        except Shelter.DoesNotExist as err:
            print(err)

        if shelter.capacity >= shelter.num_guests:
            full_shelters.append(result)
            del result
    results += full_shelters
    return results


def ComputeDistance(user_coordinates, place_coordinates):
    return math.sqrt((user_coordinates[0] - place_coordinates[0])**2 +
                     (user_coordinates[1] - place_coordinates[1])**2)


class IndexView(generic.TemplateView):
    template_name = 'gh_app/form.html'
