import subprocess
import gitlab, os, sys

GITLAB_USER = "root"
GITLAB_TOKEN = "glpat-Bdxa8eQQ3R2HRd3ay7ZM"
GITLAB_HOST = "http://gitlab.formation.lan"
GITLAB_PROJECT = "devops"

gl = gitlab.Gitlab(
  url=GITLAB_HOST,
  private_token=GITLAB_TOKEN
)

if not gl.projects.list(search=GITLAB_PROJECT):
  project = gl.projects.create({
    "name": GITLAB_PROJECT,
    "visibility": "public"
  })
  print(f"- project {GITLAB_PROJECT} created !")

ssh_path, key = f"C:/Users/{os.getlogin()}/.ssh", GITLAB_PROJECT


if not os.path.exists(f"{ssh_path}/{key}"):
  r = subprocess.run(["ssh-keygen", "-f", f"{ssh_path}/{key}"])
  print("- pubkey / privkey generated !")

try:
  gl.auth()
  with open(f"{ssh_path}/{key}.pub", "r", encoding="utf8") as f:
    gl.user.keys.create({
      "title":f"{GITLAB_PROJECT}_ssh_key", 
      "key": f.read()
    })
except Exception as e:
  print(e, type(e))
  sys.exit(0)
else:
  print("- pubkey uplopaded !!")

# pubkey upload
# with open(f"{ssh_path}/{key}.pub", "r", encoding="utf8") as f:
#   data = {
#     "title":f"{GITLAB_PROJECT}_ssh_key", 
#     "key": requests.utils.quote(f.read())
#   }
# headers = {"content-type": "application/json"}
# try:
#   r = requests.post(
#     url=f"{GITLAB_HOST}/api/v4/user/keys?private_token={GITLAB_TOKEN}",
#     data=data, headers=headers  
#   )
#   if 200 <= r.status_code < 300:
#     print("pubkey uploaded !")
#   else: raise ValueError(r.status_code)
# except Exception as e:
#   print(e, type(e))
#   print(r.request)
#   sys.exit(0)
  

# privkey config
with open(f"{ssh_path}/config", "r+") as f:
  if f"Host {GITLAB_HOST[7:]}\n" not in f.readlines():
    f.writelines([
      f"\n\nHost {GITLAB_HOST[7:]}\n",
      f" IdentityFile {ssh_path}/{GITLAB_PROJECT}\n",
      f" UserKnownHostsFile /dev/null\n",
      f" StrictHostKeyChecking no"
    ])
    print("- privkey config done !")

if not os.path.exists("./git/refs/remotes/gitlab"):
  subprocess.run(f"git remote add gitlab git@{GITLAB_HOST[7:]}:{GITLAB_USER}/{GITLAB_PROJECT}.git".split())
  with open("README.md", "w") as f:
    f.write("# WELCOME on GITLAB !!\n")
  subprocess.run("git add .".split())
  subprocess.run("git commit -m 'README!'".split())
  subprocess.run("git push -u gitlab HEAD".split())
  print("- first push done !")