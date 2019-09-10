from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def get_random_user_agent():
    # you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
    # you can also set number of user agents required by providing `limit` as parameter

    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

    return user_agent_rotator.get_random_user_agent()


def merge_dict(base, delta):
    """
        Recursively merging dictionaries.

        Args:
            base:  Target for merge
            delta: Dictionary to merge into base
    """

    for k, dv in delta.items():
        bv = base.get(k)
        if isinstance(dv, dict) and isinstance(bv, dict):
            merge_dict(bv, dv)
        else:
            base[k] = dv
