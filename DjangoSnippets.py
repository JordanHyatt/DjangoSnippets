class SaveFilterMixin:
    """ This Mixin Can be used with a FilterView SingleTable in order to save
    the users filter selections after navegating away from the lookup page"""
    def get_filterset_kwargs(self,*args):
        class_name = self.__class__
        kwargs = super().get_filterset_kwargs(*args)
        if kwargs['data']:
            filter_data = kwargs['data']
            self.request.session[f'{class_name}_filter_data']=filter_data
            print(self.request.session[f'{class_name}_filter_data'])
        else:
            if f'{class_name}_filter_data' in self.request.session.keys():
                kwargs['data']=self.request.session[f'{class_name}_filter_data']
        return kwargs  

    def get_table_data(self,*args,**kwargs):
        print(self.get_filterset(self.filterset_class).qs)
        return self.get_filterset(self.filterset_class).qs
