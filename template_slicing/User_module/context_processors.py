from sliced.models import photography_type

def add_variable_to_context(request):
    return {
        'data': photography_type.objects.all()
    }