### Repository Name
if __name__ == '__main__':
    import user_profile_import
    user_profile = user_profile_import.init()

import Garden
import params

def first_time_setup( Repo, *args, **kwargs ):
    pass

def update( Repo, *args, **kwargs ):
    pass

def repo_custom( Repo, *args, **kwargs ):
    pass

if __name__ == '__main__':

    G = Garden.Garden()
    G.called_from_repo( user_profile = user_profile, params = params )
