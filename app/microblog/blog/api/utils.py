
class ObjectDetailMixin:

    queryset = None
    serializer_class = None
    argument = None

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.kwargs[self.argument])
        self.check_object_permissions(self.request, obj)
        return obj
