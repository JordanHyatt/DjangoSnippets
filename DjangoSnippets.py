class SaveFilterMixin(SingleTableMixin):
    """ This Mixin Can be used with a FilterView SingleTable in order to save
    the users filter selections after navegating away from the lookup page"""
    def get_filterset_kwargs(self,*args):
        class_name = self.__class__
        kwargs = super().get_filterset_kwargs(*args)
        if kwargs['data']:
            filter_data = kwargs['data']
            table_sort = filter_data.get('sort')
            self.request.session[f'{class_name}_filter_data']=filter_data
            self.request.session[f'{class_name}_table_sort']=table_sort
        else:
            if f'{class_name}_filter_data' in self.request.session.keys():
                kwargs['data']=self.request.session[f'{class_name}_filter_data']
        return kwargs  

    def get_table_data(self,*args,**kwargs):
        return self.get_filterset(self.filterset_class).qs

    def get_table_kwargs(self,**kwargs):
        class_name = self.__class__
        kwargs['order_by']=self.request.session.get(f'{class_name}_table_sort')
        return kwargs
    
class SaveFormMixin:
    """ This Mixin Can be used with any view that uses a form mixin to 
    save a users form selection even if they navigate away from the page"""
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.view_name = self.__class__

    def get_form(self,**kwargs):
        form = super().get_form(**kwargs)
        if self.request.method == 'GET':
            if len(self.request.GET) > 0:
                qd=self.request.GET
                self.request.session[f'{self.view_name}_form_initial']=qd
            initial=self.request.session.get(f'{self.view_name}_form_initial')
            if initial not in [{},None]:
                form = self.form_class(initial=initial)
            
        if self.request.method == 'POST':
            self.request.session[f'{self.view_name}_form_initial']=form.data
        return form
