import dir_ops as do
from dir_ops import Path, Dir
import py_starter as ps

import garden_params as params
import GardenParent

class Installations( GardenParent.GardenParentPlural ):

    def __init__( self, Medium, dict = {} ):

        GardenParent.GardenParentPlural.__init__( self, 'Installations' )
        self.Installations = {}
        self.Medium = Medium

        self.dict = dict
        if dict == {}:
            self.dict = self.Medium.dict[ 'installations' ]

        self.load_Installations()

    def print_imp_atts( self, print_off = True ):

        string = self._print_imp_atts_helper( atts = [], print_off = False )
        string += 'Installations:\n'

        for Installation_inst in self:
            string += Installation_inst.print_one_line_atts() + '\n'

        string = string[:-1]
        return self.print_string( string, print_off = print_off )

    def print_one_line_atts( self, **kwargs ):

        self.set_attr( 'len_Installations', len(self) )
        return self._print_one_line_atts_helper( atts = ['type','len_Installations'], **kwargs )

    def load_Installations( self ):

        for package in self.dict:
            new_Installation = Installation( self, package )
            self._add_Child( new_Installation )

    def install( self ):

        for Installation_inst in self:
            Installation_inst.install()

class Installation( GardenParent.GardenParentSingular ):

    def __init__( self, Installations, package_name, version = None, dict = {}, **kwargs):

        GardenParent.GardenParentSingular.__init__( self )

        self.Installations = Installations
        self.name = package_name

        self.dict = dict
        if dict == {}:
            self.dict = self.Installations.dict[ self.name ]

        self.version = version
        if self.version == None:
            self.version = self.dict[ 'version' ]

    def print_imp_atts( self, **kwargs ):

        return self._print_imp_atts_helper( atts = ['name','version'], **kwargs )

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_imp_atts_helper( atts = ['type','name','version'], **kwargs )

    def install( self ):

        self.print_atts()
        print ('Installing ', end = '')

        string = self.Installations.Medium.name + ' install ' + self.name
        if self.version != None:
            string += ('='+self.version)

        ps.command_line( string )
        print ()
