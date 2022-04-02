import dir_ops as do
from dir_ops import Path, Dir
import py_starter as ps

import garden_params as params
import Repository
import Environment
import GardenParent

class Garden (GardenParent.GardenParentSingular) :

    def __init__( self ):

        GardenParent.GardenParentSingular.__init__( self )

        self.Dir = params.garden_Dir
        self.repos_Dir = params.repos_Dir
        self.Envs = Environment.Envs( self )
        self.Repos = Repository.Repos( self )

    def print_imp_atts( self, print_off = True ):

        string = self._print_imp_atts_helper( atts = ['Dir','repos_Dir'] ) + '\n'
        string += self.Envs.print_one_line_atts( print_off = False ) + '\n'
        string += self.Repos.print_one_line_atts( print_off = False ) + '\n'

        string = string[:-1]
        return self.print_string( string, print_off = print_off )

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_imp_atts_helper( atts = ['type','Dir','Envs','Repos'], **kwargs )

    @ps.confirm_wrap('This script only works from inside an anaconda prompt.')
    def confirm_anaconda( self ):
        return True

    @ps.confirm_wrap('As of now, all repositories will be cloned in the following repository: ' + str(params.repos_Dir.p) + '.')
    def confirm_dir( self ):
        return True

    def run( self ):

        options = [
         'update',
         'first_time_setup'
        ]

        ps.print_for_loop( options )
        ind = ps.get_int_input( 1, len(options), 'Choose which to run' ) - 1
        self.run_method( options[ind] )

    def first_time_setup( self ):

        print ('----------------')
        print ('First Time Setup')
        print ('----------------')
        print ()

        if not self.confirm_anaconda():
            return
        if not self.confirm_dir():
            return

        print ()
        self.Envs.print_atts()
        self.Envs.first_time_setup_user()
        print ()

        self.Repos.print_atts()
        self.Repos.clone()
        self.Repos.clone_Wikis()
        self.Repos.first_time_setup_user()
        print ()

    def update( self ):

        print ('------')
        print ('UPDATE')
        print ('------')
        print ()

        self.Envs.update_user()
        self.Repos.update_user()

    def called_from_repo( self, *args, params = None, **kwargs ):

        ps.print_for_loop( [ Repo.name for Repo in self.Repos ] )
        ind = ps.get_int_input( 1, len(self.Repos), prompt = 'Choose which Repository\'s custom method to run' ) - 1

        calling_Repo = self.Repos.get_Repo_from_params( params )

        Repo_choice = list(self.Repos)[ind]
        Repo_choice.repo_custom( *args, params = params, calling_Repo = calling_Repo, **kwargs )
