# одним запросом сможем запихать список
class CreateListModelMixin(object):

    def get_serializer(self, *args, **kwargs):
        """ если передается массив, установить для сериализатора значение many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)
