import ParentClass

class GardenParentSingular( ParentClass.ParentClass ):

    def __init__( self ):

        ParentClass.ParentClass.__init__( self )

class GardenParentPlural( ParentClass.ParentClass ):

    def __init__( self, child_att_name ):

        ParentClass.ParentClass.__init__( self )
        self.child_att = child_att_name

    def __len__( self ):

        return len( self.get_attr(self.child_att) )

    def __iter__( self ):

        self.i = -1
        return self

    def __next__( self ):

        self.i += 1

        if self.i < len(self):
            return self.get_attr(self.child_att)[ list(self.get_attr(self.child_att).keys())[self.i] ]
        else:
            raise StopIteration

    def _add_Child( self, Child ):

        Children_dict = self.get_attr( self.child_att )
        Children_dict[ Child.name ] = Child
        self.set_attr( self.child_att, Children_dict )

    def install( self ):

        for Child in self:
            Child.install()

    def install_user( self ):

        for Child in self:
            Child.install_user()

    def update( self ):

        for Child in self:
            Child.update()

    def update_user( self ):

        for Child in self:
            Child.update_user()

    def first_time_setup( self ):

        for Child in self:
            Child.first_time_setup()

    def first_time_setup_user( self ):

        for Child in self:
            Child.first_time_setup_user()
