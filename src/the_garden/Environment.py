import dir_ops as do
from dir_ops import Path, Dir
import py_starter as ps

import garden_params as params
import default_envs
import InstallMedium
import GardenParent


class Envs( GardenParent.GardenParentPlural ):

    def __init__( self, Garden_inst, dict = {} ):

        GardenParent.GardenParentPlural.__init__( self, 'Envs' )

        self.Garden = Garden_inst
        self.Envs = {}

        self.dict = dict
        if dict == {}:
            self.dict = default_envs.envs

        self.load_Envs()

    def print_imp_atts( self, print_off = True ):

        string = self._print_imp_atts_helper( atts = [], print_off = False )
        string += 'Envs:\n'

        for Env_inst in self:
            string += Env_inst.print_one_line_atts( print_off = False ) + '\n'

        string = string[:-1]
        return self.print_string( string, print_off = print_off )

    def print_one_line_atts( self, **kwargs ):

        self.set_attr( 'len_Envs', len(self) )
        return self._print_one_line_atts_helper( atts = ['type','len_Envs'], **kwargs )

    def load_Envs( self ):

        for env_name in self.dict:
            new_Env = Env( self, env_name )
            self._add_Child( new_Env )


class Env( GardenParent.GardenParentSingular ):

    BASE_ENV_NAME = 'base'

    def __init__( self, Envs, name, python_version = None, dict = {}, **kwargs ):

        GardenParent.GardenParentSingular.__init__( self )

        self.Envs = Envs
        self.name = name

        self.dict = dict
        if dict == {}:
            self.dict = self.Envs.dict[ self.name ]

        self.python_version = python_version
        if python_version == None:
            self.python_version = self.dict[ 'python_version' ]

        self.Mediums = InstallMedium.Mediums( self )

    def print_imp_atts( self, **kwargs ):

        return self._print_imp_atts_helper( atts = ['name','python_version','Mediums'], **kwargs )

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_line_atts_helper( atts = ['type','name','python_version','Mediums'], **kwargs )

    def create( self ):

        """creates the anaconda environment with self.name"""

        string = 'conda create --name ' + self.name
        if self.python_version != None:
            string += (' python=' + self.python_version )

        ps.command_line( string )

    def delete( self ):

        """deletes the environment from Anaconda"""

        ps.command_line( 'conda env remove -n ' + self.name )

    def delete_user( self ):
        ps.confirm_wrap( 'This will delete the environment ' + self.name + '.' )( self.delete )()

    def activate( self ):

        ps.command_line( 'conda activate ' + self.name )

    def deactivate( self ):

        ps.command_line( 'conda deactivate' )

    def install_on_jupyter( self ):

        ps.activate()
        ps.command_line( 'python -m ipykernel install --user --name=' + self.name )

    def update( self ):

        self.print_atts()
        self.install_on_jupyter()
        print ()

    def update_user( self ):
        ps.confirm_wrap( 'This will update the Environmnet ' + self.name + '.' )( self.update )()

    def first_time_setup( self ):

        self.print_atts()
        print ()

        if self.name != self.BASE_ENV_NAME:
            self.create()

        self.activate()
        self.Mediums.install()
        self.install_on_jupyter()
        self.deactivate()

    def first_time_setup_user( self ):
        ps.confirm_wrap( 'This will perform first time setup for environment ' + self.name + '.' )( self.first_time_setup )()
