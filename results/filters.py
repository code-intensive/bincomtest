# import django_filters
# from django import forms


# class BookFilters(django_filters.FilterSet):
#     book_author = django_filters.CharFilter(field_name="book_author__name", label="", lookup_expr="icontains",
#                                             label_suffix="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Search by author"}))

#     book_tags = django_filters.CharFilter(
#         field_name="book_tags__tag", label="", lookup_expr="exact", label_suffix="")

#     book_category = django_filters.CharFilter(
#         field_name="book_category__category", label="", lookup_expr="exact", label_suffix="")

#     book_title = django_filters.CharFilter(field_name="book_title", label="", lookup_expr="icontains", label_suffix="", widget=forms.TextInput(
#         attrs={"class": "form-control", "placeholder": "Search by book title"}))

#     rating = django_filters.NumberFilter(
#         field_name="rating", label="", label_suffix="", widget=forms.Select(attrs={"class": "form-control"}))

#     price = django_filters.CharFilter(
#         field_name="price", lookup_expr="lte", label="", label_suffix="")

#     class Meta:
#         ordering = ("-pk",)
#         model = Book
#         fields = ("book_author", "book_title", "rating",
#                   "price", "book_tags", "book_category")
