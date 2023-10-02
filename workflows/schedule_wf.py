from flytekit.remote import FlyteRemote
from flytekit.configuration import Config
from workflows.example import wf


remote = FlyteRemote(config=Config.auto())
execution = remote.execute(wf, inputs={"name": "Kermit"})
