import os
import dir_ops as do
from dir_ops import Path, Dir

params_Path = Path( os.path.abspath(__file__) )
garden_Dir = Dir( params_Path.ascend() )
repo_Dir = garden_Dir
repos_Dir = Dir( garden_Dir.ascend() )
data_Dir = Dir( repo_Dir.join('Data') )
templates_Dir = Dir( garden_Dir.join( 'Templates' ) )
garden_repo_template_Path = Path( templates_Dir.join('the_garden.py') )

base_iCenter_url = 'https://github.ameren.com/iCenter/'
base_iCenter_pages_url = 'https://github.ameren.com/pages/iCenter/'

repo_names = [
'The-Garden',
'User-Profile',
'Analytics-Packages',
'AWS-Credentials',
'ML-Pipeline',
'Smart-Documentation',
's3synchrony',
'Nanoid',
'Repository-Generator',
'Database-Playground'
]
