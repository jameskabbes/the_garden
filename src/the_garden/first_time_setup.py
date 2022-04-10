import garden_params as params
import os
import platform

# It is imperative that this repository works independently other modules/installations

print ('''

 .----------------. .----------------. .----------------. .-----------------..----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |     _____    | | |     ______   | | |  _________   | | | ____  _____  | | |  _________   | | |  _________   | | |  _______     | |
| |    |_   _|   | | |   .' ___  |  | | | |_   ___  |  | | ||_   \|_   _| | | | |  _   _  |  | | | |_   ___  |  | | | |_   __ \    | |
| |      | |     | | |  / .'   \_|  | | |   | |_  \_|  | | |  |   \ | |   | | | |_/ | | \_|  | | |   | |_  \_|  | | |   | |__) |   | |
| |      | |     | | |  | |         | | |   |  _|  _   | | |  | |\ \| |   | | |     | |      | | |   |  _|  _   | | |   |  __ /    | |
| |     _| |_    | | |  \ `.___.'\  | | |  _| |___/ |  | | | _| |_\   |_  | | |    _| |_     | | |  _| |___/ |  | | |  _| |  \ \_  | |
| |    |_____|   | | |   `._____.'  | | | |_________|  | | ||_____|\____| | | |   |_____|    | | | |_________|  | | | |____| |___| | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' 

''')

print ()
print ()
input('Welcome to the iCenter Garden! Press enter to get started: ')
print ()
print ()

###
#  1. Clone the Repos
###

OG_PYTHONPATH = os.getenv('PYTHONPATH')
pythonpaths = OG_PYTHONPATH.split( ';' )

cwd = os.getcwd().replace( '\\','/' ) 
parent_dir = '/'.join( cwd.split( '/' )[:-1] )

print ()
print ('1. Clone repositories')
print ()

for account in params.github_accounts:

    account_dict = params.github_accounts[ account ]

    print ()
    print ('---------------')
    print (account)
    print (account_dict['url_base'])
    print ('---------------')
    print ()

    for repo in account_dict[ 'repos' ]:
        
        print ()
        print ('---------------------------')

        url_clone = account_dict['url_base'] + '/' + repo + params.git_clone_suffix
        repo_dir = parent_dir + '/' + repo
        src_dir = repo_dir + '/src'
        
        print (repo)
        print (url_clone)

        if account_dict['add_to_pythonpath']:
            if src_dir not in pythonpaths:
                print ('Adding ' + src_dir + ' to PYTHONPATH')
                pythonpaths.append( src_dir )

        print ()
        if not os.path.exists( repo_dir ):
            print ( url_clone + '->\t' + repo_dir )
            if input( 'To clone, press enter. To skip, type something: ' ) == '':
                    print ('Cloning repository...')
                    os.system( 'git -C ' + parent_dir + ' clone ' + url_clone )

        else:
            print ('Skipping: directory already exists at: ' + repo_dir )


print ()
print ('2. Export src dirs to PYTHONPATH')
print ()

PYTHONPATH = ';'.join( pythonpaths )
print ('PYTHONPATH = ' + str(PYTHONPATH))

if PYTHONPATH != OG_PYTHONPATH:
    print ('Overwriting PYTHONPATH. You will need to RESTART your machine for changes to take effect.')
    
    if platform.system() == 'Windows':
        os.system( 'setx PYTHONPATH ' + PYTHONPATH )
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system( 'export PYTHONPATH=' + PYTHONPATH )
else:
    print ('No changes made to PYTHONPATH')


print ()
print ('3. Install Anaconda environments')
print ()

print ('Still in development')

