import pynecone as pc

class VirtuejingleConfig(pc.Config):
    pass

config = VirtuejingleConfig(
    app_name="virtuejingle",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)