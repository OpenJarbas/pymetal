from distutils.core import setup

setup(
    name='pymetal',
    version='0.5.0',
    packages=[],
    install_requires=["requests", "bs4", "requests_cache",
                      "random-user-agent", "lxml"],
    url='https://www.github.com/OpenJarbas/pymetal',
    license='Apache2.0',
    author='jarbasAi',
    author_email='jarbasai@mailfence.com',
    description='metal archives, dark lyrics api'
)
