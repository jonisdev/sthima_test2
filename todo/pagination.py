# from rest_framework import pagination
# from rest_framework.response import Response
# from .models import TodoList


# class TransferPagination(pagination.PageNumberPagination):
#     total_transfers = TodoList.objects.all()
#     total_tranfers_amount = 0

#     def get_paginated_response(self, data):

#         for i in self.total_transfers:
#             self.total_tranfers_amount += i.amount

#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'total_transfers': self.page.paginator.count,
#             'total_transfers_amount': self.total_tranfers_amount,
#             'results': data
#         })
