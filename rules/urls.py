from django.urls import path
from .views import RuleCreateView, RuleCombineView, RuleEvaluateView

urlpatterns = [
    path('create_rule/', RuleCreateView.as_view(), name='create_rule'),
    path('combine_rules/', RuleCombineView.as_view(), name='combine_rules'),
    path('evaluate_rule/', RuleEvaluateView.as_view(), name='evaluate_rule'),
]