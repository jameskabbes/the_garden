import dir_ops as do
from dir_ops import Path, Dir
import py_starter as ps

import garden_params as params
import GardenParent
import os
import sys
import shutil

class Repos( GardenParent.GardenParentPlural ):

    def __init__( self, Garden_inst ):

        GardenParent.GardenParentPlural.__init__( self, 'Repos' )

        self.Garden = Garden_inst
        self.Dir = self.Garden.repos_Dir
        self.Repos = {}
        self.load_Repos()

    def print_imp_atts( self, print_off = True ):

        string = self._print_imp_atts_helper( atts = [], print_off = False )
        string += 'Repos:\n'

        for Repo_inst in self:
            string += Repo_inst.print_one_line_atts( print_off = False ) + '\n'

        string = string[:-1]
        return self.print_string( string, print_off = print_off )

    def print_one_line_atts( self, **kwargs ):

        self.set_attr( 'len_Mediums', len(self) )
        return self._print_one_line_atts_helper( atts = ['type','len_Mediums'], **kwargs )

    def cd( self ):

        ps.command_line( 'cd ' + str(self.Dir.p) )

    def load_Repos( self ):

        for repo_name in params.repo_names:
            self._add_Child( Repo( self, repo_name ) )

    def clone( self ):

        for Child in self:
            Child.print_atts()
            Child.clone()
            print ()

    def export_support_packages( self ):

        string = ''
        for Child in self:
            string += Child.export_support_packages() + '\n'

        print (string)
        return string

    def get_Repo_from_params( self, params ):

        valid = False
        if hasattr( params, 'repo_Dir' ):
            repo_Dir = params.repo_Dir
            valid = True

        if hasattr( params, 'repo_dir' ):
            repo_Dir = Dir(params.repo_dir)
            valid = True

        if not valid:
            print ('Cannot get Repo from given params')
            return None

        return self.Repos[ repo_Dir.dirs[-1] ]


class Repo( GardenParent.GardenParentSingular ):

    def __init__( self, Repos_inst, name = None, repo_Dir = None ):

        GardenParent.GardenParentSingular.__init__( self )

        self.Repos = Repos_inst

        if repo_Dir == None and name == None:
            assert False

        # If they have given us the Dir for the Repo, use that as first priority
        if repo_Dir != None:
            name = repo_Dir.dirs[-1]
        else:
            # otherwise, use the name given
            repo_Dir = Dir( self.Repos.Dir.join( name ) )

        self.name = name
        self.Dir = repo_Dir 
        self.pages_Dir = Dir( self.Dir.join( 'docs' ) ) 

        # set the URL's 
        self.url = params.base_iCenter_url + self.name
        self.clone_url = self.url + '.git'
        self.pages_url = params.base_iCenter_pages_url + self.name
        
        # Set the Paths
        self.garden_Path = Dir( self.Dir.join( params.garden_repo_template_Path.filename ) )
        self.README_Path = Path( self.Dir.join( 'README.md' ) )
        self.html_index_Path = Path( self.Dir.join('docs','index.html') )

    def print_imp_atts( self, **kwargs ):

        return self._print_imp_atts_helper( atts = ['name','url','Dir'], **kwargs )

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_line_atts_helper( atts = ['type','name','url'], **kwargs )

    def git_command_line_string( self, following_string, *args, **kwargs ):

        return 'git -C ' + self.Dir.p + ' ' + following_string

    def git_command_line( self, *args, **kwargs ):

        string = self.git_command_line_string( *args, **kwargs )
        ps.command_line( string )

    def open_url( self, **kwargs ):

        return ps.open_url( self.url, **kwargs )

    def clone_user(self):
        ps.confirm_wrap( 'This will clone repo ' + self.name + '.' )( self.clone )()

    def pull( self ):

        self.git_command_line('pull')

    def add( self, file = '.' ):

        self.git_command_line('add ' + file)

    def commit( self, message = 'commit message' ):

        self.git_command_line('commit -m "' + message + '"')

    def checkout( self, branch ):

        self.git_command_line('checkout ' + branch)

    def checkout_master( self ):

        self.checkout( 'master' )

    def push( self ):

        self.git_command_line( 'push' )

    def clone( self ):

        if not self.Dir.exists():
            ps.command_line( 'git -C ' + self.Repos.Dir.p + ' clone ' + self.clone_url )

        else:
            print ('Repository ' + self.name + ' already exists at ' + self.Dir.p)

    def make_garden_path( self, overwrite = False ):

        if not self.garden_Path.exists() or overwrite:
            params.garden_repo_template_Path.copy( self.garden_Path )

    def import_garden_module( self ):

        self.make_garden_path()
        sys.path.append( self.Dir.p )
        self.garden_module = ps.import_module_from_path( self.garden_Path.p )

    def run_repo_method( self, method_name, *args, **kwargs ):

        self.import_garden_module()
        self.print_atts()

        print()
        print ('Running ' + method_name)
        print ('Loading Repository ' + str(self.name) )
        print()

        method_pointer = getattr( self.garden_module, method_name )
        return method_pointer( self, *args, **kwargs )

    def update( self, *args, **kwargs ):

        self.checkout_master()
        self.pull()
        self.run_repo_method( 'update', *args, **kwargs )

    def update_user( self ):
        ps.confirm_wrap( 'This will update the repo ' + self.name + '.' )( self.update )()

    def first_time_setup( self, *args, **kwargs ):
        self.run_repo_method( 'first_time_setup', *args, **kwargs )

    def first_time_setup_user( self ):
        ps.confirm_wrap( 'This will run first time setup for Repository ' + self.name + '.' )( self.first_time_setup )()

    def repo_custom( self, *args, **kwargs ):
        self.run_repo_method( 'repo_custom', *args, **kwargs )

    def repo_custom_user( self ):
        ps.confirm_wrap( 'This will run the custom method for Repository ' + self.name + '.' )( self.repo_custom )()

    def export_support_packages( self ):

        string = "default_repo_parent_path + '/" + self.name + "',\t #" + self.url
        return string

