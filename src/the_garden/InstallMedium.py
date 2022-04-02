import dir_ops as do
from dir_ops import Path, Dir
import py_starter as ps

import garden_params as params
import GardenParent
import Installation


class Mediums( GardenParent.GardenParentPlural ):

    def __init__( self, Env, dict = {} ):

        GardenParent.GardenParentPlural.__init__( self, 'Mediums' )
        self.Env = Env
        self.Mediums = {}

        self.dict = dict
        if dict == {}:
            self.dict = self.Env.dict[ 'mediums' ]

        self.load_Mediums()

    def print_imp_atts( self, print_off = True ):

        string = self._print_imp_atts_helper( atts = [], print_off = False )
        string += 'Mediums:\n'

        for Medium_inst in self:
            string += Medium_inst.print_one_line_atts( print_off = False ) + '\n'

        string = string[:-1]
        return self.print_string( string, print_off = print_off )

    def print_one_line_atts( self, **kwargs ):

        self.set_attr( 'len_Mediums', len(self) )
        return self._print_one_line_atts_helper( atts = ['type','len_Mediums'], **kwargs )

    def load_Mediums( self ):

        for medium in self.dict:
            new_Medium = Medium( self, medium )
            self._add_Child( new_Medium )

class Medium( GardenParent.GardenParentSingular ):

    def __init__( self, Mediums, name, dict = {} ):

        GardenParent.GardenParentSingular.__init__( self )
        self.Mediums = Mediums
        self.name = name

        self.dict = dict
        if dict == {}:
            self.dict = self.Mediums.dict[ self.name ]

        self.Installations = Installation.Installations( self )

    def print_imp_atts( self, **kwargs ):

        return self._print_imp_atts_helper( atts = ['name','Installations'], **kwargs )

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_imp_atts_helper( atts = ['type','name','Installations'], **kwargs )

    def install( self ):

        self.print_atts()
        print ()

        self.Installations.install()
