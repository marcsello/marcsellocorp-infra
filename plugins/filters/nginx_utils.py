import os.path

class FilterModule(object):
    """
    Some helper filters for the nginx role
    """

    def filters(self):
        return {
            'need_static_dir': self.need_static_dir
        }

    def need_static_dir(self, vhost_config):
        if result := vhost_config.get('always_create_static_dir', False):
            return True
        
        for loc in vhost_config['locations']:
            if loc['type'] == 'static':
                result = True

        return result
