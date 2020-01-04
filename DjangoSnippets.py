class SaveFilterMixin:
    """ This Mixin Can be used with a FilterView in order to save
    the users filter selections after navegating away from the lookup page"""
    
    def get_filterset_kwargs(self,*args):
        kwargs = super().get_filterset_kwargs(*args)
        if kwargs['data']:
            bucket_filter_data = kwargs['data']
            self.request.session['table_filter_data']= bucket_filter_data
        else:
            if 'table_filter_data' in self.request.session.keys():
                kwargs['data']=self.request.session['table_filter_data']
        return kwargs  

    def get_table_data(self,*args,**kwargs):
        return self.get_filterset(self.filterset_class).qs
