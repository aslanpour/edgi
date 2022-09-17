#build manifest 
#always required: api_version, kind, object_name, namespace
def manifest_builder(**kwargs):
    results = None
    msg =""
    error = ""

    msg += '\nmanifest_builder started.'

    #check basic requirements to build a manifest
    if 'api_version' not in kwargs or 'kind' not in kwargs or 'object_name' not in kwargs or 'namespace' not in kwargs:
        error += '\n required fields are not given, i.e., api_version, kind, object_name, or namespace.'
        return results, msg, error

    #pick a builder

    #TrafficSplit
    if kwargs['kind'] == 'TrafficSplit':
        manifest, msg_child, error = trafficSplit(**kwargs)
        msg += msg_child
    elif kwargs['kind'] == 'Function':
        manifest, msg_child, error = function(**kwargs)
        msg += msg_child
    else:
        error +='\nKind: ' + kwargs['kind'] + ' not implemented'
    
    msg += '\nmanifest_builder stopped'
    return manifest, msg, error



# manifest builder for trafficSplit
def trafficSplit(**kwargs):
    results= None; msg=""; error=""
    msg +="manifest builder for trafficSplit started."

    #verify especial fileds for a TrafficSplit, e.g., backend and service
    if not 'backends' in kwargs or not 'service' in kwargs:
        error += '\nNo backends and/or service are given in kwargs'
        return results, msg, error


    #manifest
    manifest = {
        "apiVersion": kwargs['api_version'],
        "kind": kwargs['kind'],
        "metadata": {
            "name": kwargs['object_name'],
            "namespace": kwargs['namespace']
        },
        "spec": {
            "backends": kwargs['backends'],
            "service": kwargs['service']
        }
    }

    msg += '\ntrafficSplit: stopped'
    return manifest, msg, error


# manifest builder for Function
def function(**kwargs):
    results= None; msg=""; error=""
    msg +="manifest builder for Function started."

    #verify especial fileds for a Function, e.g., image
    if not 'image' in kwargs:
        error += '\nNo image is given in kwargs'
        return results, msg, error


    #manifest
    manifest = {
        "apiVersion": kwargs['api_version'],
        "kind": kwargs['kind'],
        "metadata": {
            "name": kwargs['object_name'],
            "namespace": kwargs['namespace']
        },
        "spec": {
            "name": kwargs['object_name'],
            'image':  kwargs['image'],
            'labels': kwargs['labels'],
            'annotations': kwargs['annotations'],
            'constraints': kwargs['constraints'],
        }
    }

    msg +="\nmanifest builder for Function stopped"
    return manifest, msg, error



