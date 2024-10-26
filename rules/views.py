from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .rules_engine import create_rule, combine_rules, evaluate_rule

class RuleCreateView(APIView):
    def post(self, request):
        rule_string = request.data.get('rule_string')
        root = create_rule(rule_string)
        return Response({'message': 'Rule created', 'root_id': root.id}, status=status.HTTP_201_CREATED)

class RuleCombineView(APIView):
    def post(self, request):
        rules = request.data.get('rules')
        combined_root = combine_rules(rules)
        return Response({'message': 'Rules combined', 'root_id': combined_root.id}, status=status.HTTP_200_OK)

class RuleEvaluateView(APIView):
    def post(self, request):
        ast_root_id = request.data.get('ast_root_id')
        data = request.data.get('data')
        # Fetch the AST node based on the ID
        ast_root = Node.objects.get(id=ast_root_id)  # Implement proper fetching logic
        result = evaluate_rule(ast_root, data)
        return Response({'result': result}, status=status.HTTP_200_OK)
