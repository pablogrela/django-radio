from invoke import Collection

from . import heroku, radioco, docker, docs, locale


ns = Collection()
ns.add_collection(heroku)
ns.add_collection(docker)
ns.add_collection(docs)
ns.add_collection(locale)
ns.add_task(radioco.quickstart)
ns.add_task(radioco.commit_changes)
ns.add_task(radioco.checkout_latest)
