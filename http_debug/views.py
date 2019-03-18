from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def detect(request):
    if 'all' in request.GET:
        return render(
            request,
            'http_debug/info.html',
            context={
                'filtered_meta_data': request.META
            }
        )
    else:
        desired_keys = {
            'SERVER_PORT',
            'SERVER_PROTOCOL',
            'REMOTE_ADDR',
            'REQUEST_METHOD',
            'PATH_INFO',
            'CONTENT_TYPE',
            'CONTENT_LENGTH',
        }
        desired_keys.update({k for k in request.META.keys() if k.startswith('HTTP')})

        query = request.GET.copy()
        query['all'] = ''
        all_url = request.build_absolute_uri(request.path) + '?' + query.urlencode()

        return render(
            request,
            'http_debug/info.html',
            context={
                'all_url': all_url,
                'filtered_meta_data': {
                    k: [v]
                    for k, v in request.META.items()
                    if k in desired_keys
                },
                'get_dict': {
                    k: request.GET.getlist(k)
                    for k in request.GET.keys()
                },
                'post_dict': {
                    k: ','.join(request.POST.getlist(k))
                    for k in request.POST.keys()
                },
            }
        )
