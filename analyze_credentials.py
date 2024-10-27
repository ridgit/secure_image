# Créer le script directement dans le workflow
          import ast
          import os

          EXTERNAL_SERVICES = {
              'Minio': 'minio',
              'MongoClient': 'pymongo',
              'connect': 'nats',
              'boto3': 'boto3'
          }

          SECRET_SOURCES = ['os.getenv', 'hvac.Client']

          class ServiceConnectionAnalyzer(ast.NodeVisitor):
              def __init__(self):
                  self.service_security_report = {}

              def visit_Import(self, node):
                  for alias in node.names:
                      if alias.name in EXTERNAL_SERVICES.values():
                          self.service_security_report[alias.name] = True
                  self.generic_visit(node)

              def visit_ImportFrom(self, node):
                  if node.module in EXTERNAL_SERVICES.values():
                      for alias in node.names:
                          self.service_security_report[alias.name] = True
                  self.generic_visit(node)

              def visit_Call(self, node):
                  if isinstance(node.func, ast.Name):
                      service_name = node.func.id
                      if service_name in EXTERNAL_SERVICES:
                          self.check_service_security(service_name, node.args)
                  elif isinstance(node.func, ast.Attribute):
                      service_name = node.func.attr
                      if service_name in EXTERNAL_SERVICES:
                          self.check_service_security(service_name, node.args)
                  self.generic_visit(node)

              def check_service_security(self, service_name, args):
                  for arg in args:
                      if not self.check_secure_source(arg):
                          self.service_security_report[service_name] = False

              def check_secure_source(self, node):
                  if isinstance(node, ast.Call):
                      func_name = self.get_full_func_name(node.func)
                      if func_name in SECRET_SOURCES:
                          return True
                  elif isinstance(node, ast.Str):
                      return False
                  return True

              def get_full_func_name(self, node):
                  if isinstance(node, ast.Name):
                      return node.id
                  elif isinstance(node, ast.Attribute):
                      return f'{self.get_full_func_name(node.value)}.{node.attr}'
                  return ''

              def analyze(self, code):
                  tree = ast.parse(code)
                  self.visit(tree)
                  return self.service_security_report

          def main():
              file_to_analyze = 'function_image1/day.py'
              with open(file_to_analyze, 'r') as f:
                  code = f.read()
                  analyzer = ServiceConnectionAnalyzer()
                  service_security_report = analyzer.analyze(code)
                  for service, is_secure in service_security_report.items():
                      if not is_secure:
                          print(f'Les identifiants pour le service {service} ne sont pas sécurisés.')
                          exit(1)  # Quitte avec une erreur si un identifiant non sécurisé est trouvé
                  print('Tous les services sont sécurisés pour le fichier:', file_to_analyze)

          if __name__ == '__main__':
              main()
         
