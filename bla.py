def bla(event, context):
    try:
        a, b = event['data']['a'], event['data']['b']
    except Exception:
        a, b = 0, 0

    print(event['params'])
    return {
        'status': 202,
        'data': {
            'sum': a + b,
            'event': event,
            'context': context,
        },
    }


