import os

template = '''---
version: 1
component:
  name: Micro Service {num}
  type: service
  lifecycle:
  tier:
  product:
  owner:
  system:
  language:
  framework:
  description:
  aliases:
  tags:
  repositories:
  - name: derek-etherton-opslevel/MicroReadmes
    path: "/{dirname}"
    provider: github
    display_name: derek-etherton-opslevel/MicroReadmes
  tools:
  dependencies:
  alert_sources:
'''

root = os.path.dirname(os.path.abspath(__file__))
for i in range(1, 1001):
    dname = f"service_{i:04d}"
    dpath = os.path.join(root, dname)
    os.makedirs(dpath, exist_ok=True)
    yml_path = os.path.join(dpath, "opslevel.yml")
    with open(yml_path, "w") as f:
        f.write(template.format(num=i, dirname=dname))
    readme_path = os.path.join(dpath, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {dname}\n\nThis is the README for {dname}. Unique placeholder content {i}.")
