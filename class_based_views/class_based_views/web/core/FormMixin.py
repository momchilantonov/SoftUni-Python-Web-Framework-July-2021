class BootStrapFormMixin:
    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        self.__apply_bootstrap_classes(form)
        return form

    @staticmethod
    def __apply_bootstrap_classes(form):
        for (_, field) in form.fields.items():
            field.widget.attrs = {
                'placeholder': 'Enter value',
            }
